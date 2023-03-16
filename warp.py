import atexit
import subprocess
import threading
import time
import signal


def background_process(stop_server, command):
    """
    Manager of background process
    :param stop_server: This boolean flag is used to signal the stopping of the background process
    :param command: Command that should be executed to start background process
    """
    while True:
        # Start process
        proc = subprocess.Popen(['python', command])
        print()
        print(f"Started new server subprocess {proc.pid}")

        # Check to see if process is still running
        while proc.poll() is None and not stop_server():
            # TODO: Maybe use a gRPC health check here to see if the process is up?
            # Don't use readline since it will block!
            print(f"doing health check for process {proc.pid}")

            time.sleep(1)

        if stop_server():
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                pass
            finally:
                proc.kill()
                print('Cleaning up parent thread')
                break


class Warp:
    stop_server = False

    def __init__(self, command: str):
        """
        Initializes a Warp object
        :param command: Command to execute to start subprocess
        """
        self.command = command
        self.t = None

    def start(self):
        """
        Starts the background process
        """
        stop_server = False

        def stop_server_gracefully_atexit():
            nonlocal stop_server
            stop_server = True

        def stop_server_gracefully_on_signal(signal, frame):
            stop_server_gracefully_atexit()

        atexit.register(stop_server_gracefully_atexit)
        signal.signal(signal.SIGTERM, stop_server_gracefully_on_signal)
        signal.signal(signal.SIGINT, stop_server_gracefully_on_signal)

        t = threading.Thread(target=background_process, args=(lambda: stop_server, self.command,))

        self.kill_function = stop_server_gracefully_atexit

        t.start()
        self.t = t
        print('Cleaning up main process')

    def stop(self):
        self.kill_function()

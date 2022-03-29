from warp import Warp

def test_start_process_sdk():
    wp = Warp(command="dummy_server.py")
    wp.start()
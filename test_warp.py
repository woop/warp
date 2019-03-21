from warp import Warp
import os
import time

PATH_TO_OUTPUT_FILE="dummy_server.log"


def test_start_process_sdk():
    wp = Warp(command="dummy_server.py")
    wp.start()

    if not os.path.exists(PATH_TO_OUTPUT_FILE):
        raise Exception("Dummy server isn't producing any output")

    with open(PATH_TO_OUTPUT_FILE) as f:
        initial_lines = f.readlines()

    # We expect about one log line per second
    time.sleep(5)

    with open(PATH_TO_OUTPUT_FILE) as f:
        final_lines = f.readlines()

    assert len(initial_lines) + 5 == len(final_lines)
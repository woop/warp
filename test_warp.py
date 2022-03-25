from warp import Warp
import os
import time

PATH_TO_OUTPUT_FILE = "dummy_server.log"
PATH_TO_OUTPUT_FILE_SHORT_LIVED = "short_lived_dummy_server.log"


def test_start_process_sdk():
    try:
        os.remove(PATH_TO_OUTPUT_FILE)
    except:
        pass

    wp = Warp(command="dummy_server.py")
    wp.start()
    time.sleep(1)

    if not os.path.exists(PATH_TO_OUTPUT_FILE):
        raise Exception("Dummy server isn't producing any output")

    with open(PATH_TO_OUTPUT_FILE) as f:
        initial_lines = f.readlines()

    # We expect about one log line per second
    time.sleep(5)

    with open(PATH_TO_OUTPUT_FILE) as f:
        final_lines = f.readlines()

    assert len(initial_lines) + 5 == len(final_lines)

    wp.stop()

    try:
        os.remove(PATH_TO_OUTPUT_FILE)
    except:
        pass


def test_self_healing_of_process():
    try:
        os.remove(PATH_TO_OUTPUT_FILE_SHORT_LIVED)
    except:
        pass

    wp = Warp(command="short_lived_dummy_server.py")
    wp.start()
    time.sleep(1)

    if not os.path.exists(PATH_TO_OUTPUT_FILE_SHORT_LIVED):
        raise Exception("Dummy server isn't producing any output")

    time.sleep(5)

    with open(PATH_TO_OUTPUT_FILE_SHORT_LIVED) as f:
        all_ids = f.readlines()

    wp.stop()

    unique_ids = set(all_ids)
    amount_of_unique_ids = len(unique_ids)
    assert amount_of_unique_ids == 2

    try:
        os.remove(PATH_TO_OUTPUT_FILE_SHORT_LIVED)
    except:
        pass

from time import sleep

PATH_TO_OUTPUT_FILE = "dummy_server.log"

while True:
    try:
        message = f'Currently running server subprocess\n'
        print(message)
        with open(PATH_TO_OUTPUT_FILE, 'a') as f:
            f.write(message)
        sleep(1)

    except KeyboardInterrupt as e:
        print("Cleaning up subprocess")
        exit(0)

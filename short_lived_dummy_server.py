from time import sleep

PATH_TO_OUTPUT_FILE = "short_lived_dummy_server.log"

import random
import string

id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

count = 0
while True:
    try:
        message = f'{id}\n'
        print(message)
        with open(PATH_TO_OUTPUT_FILE, 'a') as f:
            f.write(message)
        sleep(1)
        count += 1

        # Kill the process every 3 iterations
        if count == 3:
            print('Server subprocess kills itself')
            exit(5)

    except KeyboardInterrupt as e:
        print("Cleaning up subprocess")
        exit(0)

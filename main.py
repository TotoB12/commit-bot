import os
import time

while True:
    with open('file.txt', 'w') as f:
        f.write('0')
    os.system('git add .')
    os.system('git commit -m "updated file with 0"')
    print("updated file with 0")
    os.system('git push')
    print("pushed")
    # time.sleep(1)

    with open('file.txt', 'w') as f:
        f.write('1')
    os.system('git add .')
    os.system('git commit -m "updated file with 1"')
    print("updated file with 1")
    os.system('git push')
    print("pushed")
    # time.sleep(1)

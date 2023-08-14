import os

while True:
    with open('file.txt', 'w') as f:
        f.write('0')
    os.system('git commit -am "updated file with 0"')
    print("updated file with 0")
    os.system('git push')
    print("pushed")

    with open('file.txt', 'w') as f:
        f.write('1')
    os.system('git commit -am "updated file with 1"')
    print("updated file with 1")
    os.system('git push')
    print("pushed")

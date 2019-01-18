with open('string.bin', 'rb') as stringFile:
    with open('string.txt', 'w') as f:
        for byte in stringFile.read():
            print('byte %s' % hex(byte), file=f)

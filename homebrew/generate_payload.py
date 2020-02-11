with open('payload.bin', 'rb') as stringFile:
    with open('payload.s', 'w') as f:
        for byte in stringFile.read():
            print('byte %s' % hex(byte), file=f)

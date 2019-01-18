# ROBChain
PoC exploit for Super Smash Brothers Wii U to get arbitrary ROP execution under userland

Can go over any fighter (and possibly article) to gain arbitrary code execution (Only ROP atm). This is a variation of contenthax based around MSC (the main character scripting language) exploiting a heap overflow to gain arbitrary read/write within the MSC script. Use [pymsc](https://github.com/jam1garner/pymsc) to build.

### Build PoC

Required:

* Python 3.6 or greater in path as python3 (Edit Makefile for other configs)
* make

```
git clone --recurse-submodules https://github.com/jam1garner/ROBChain.git && \
cd ROBChain/poc && \
make clean && make
```

### Install

Take the generated exploit.mscsb and install it in a patch over

```
/data/fighter/[fighter]/script/msc/[fighter].mscsb
```

then install via SDCafiine or fs contents replacement.

### Video of PoC

https://youtu.be/u3qKsbGPgn0

### Write up

https://github.com/jam1garner/ROBChain/blob/master/WRITE-UP.md

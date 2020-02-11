PYTHON       := python3
ifeq (, $(shell which python3))
	# if no python3 alias, fall back to `python` and hope it's py3
	PYTHON   := python
endif

all: exploit.mscsb

clean:
	rm -f exploit.mscsb payload.s payload.bin main.s

exploit.mscsb: payload.s Scripts main.s
	$(PYTHON) ../pymsc/asm.py

payload.s: payload.bin
	$(PYTHON) generate_payload.py

payload.bin: crashText.txt
	cp -f crashText.txt payload.bin
	printf "\0" >> payload.bin

main.s: rop_setup.s
	$(PYTHON) generate_rop.py


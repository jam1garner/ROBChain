python=python3

all: exploit.mscsb

clean:
	rm -f exploit.mscsb payload.s payload.bin main.s

exploit.mscsb: payload.s Scripts main.s
	$(python) ../pymsc/asm.py

payload.s: payload.bin
	$(python) generate_payload.py

payload.bin: crashText.txt
	cp -f crashText.txt payload.bin
	printf "\0" >> payload.bin

main.s: rop_setup.s
	$(python) generate_rop.py


all: exploit.mscsb

clean:
	rm -f exploit.mscsb payload.s payload.bin main.s

exploit.mscsb: payload.s Scripts main.s
	python3 ../pymsc/asm.py

payload.s: payload.bin
	python3 generate_payload.py

payload.bin: crashText.txt
	cp -f crashText.txt payload.bin
	printf "\0" >> payload.bin

main.s: rop_setup.s
	python3 generate_rop.py


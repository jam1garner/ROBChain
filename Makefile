python=python3
POC_PATH=poc/exploit.mscsb

poc: $(POC_PATH)
	$(python) inject.py $<

clean:
	rm -r data
	$(MAKE) --directory=poc clean

$(POC_PATH):
	$(MAKE) --directory=poc

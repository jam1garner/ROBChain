PYTHON       := python3
ifeq (, $(shell which python3))
	# if no python3 alias, fall back to `python` and hope it's py3
	PYTHON   := python
endif
EXPLOIT_DIR  := homebrew
EXPLOIT_PATH := $(EXPLOIT_DIR)/exploit.mscsb

homebrew: $(EXPLOIT_PATH)
	$(PYTHON) inject.py $<

clean:
	rm -r data
	$(MAKE) --directory=$(EXPLOIT_DIR) clean

$(EXPLOIT_PATH):
	$(MAKE) --directory=$(EXPLOIT_DIR)

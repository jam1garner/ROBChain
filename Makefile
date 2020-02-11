python       := python3
EXPLOIT_DIR  := homebrew
EXPLOIT_PATH := $(EXPLOIT_DIR)/exploit.mscsb

homebrew: $(EXPLOIT_PATH)
	$(python) inject.py $<

clean:
	rm -r data
	$(MAKE) --directory=$(EXPLOIT_DIR) clean

$(EXPLOIT_PATH):
	$(MAKE) --directory=$(EXPLOIT_DIR)

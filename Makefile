.PHONY: all deploy lib

DEST := /media/${USER}/CIRCUITPY
ifeq ("$(wildcard $(DEST))", "")
	DEST = /run/media/${USER}/CIRCUITPY
	ifeq ("$(wildcard $(DEST))", "")
	@echo "Deployment not possible"
	endif
endif

all: deploy lib

deploy:
	cp code.py $(DEST)
lib:
	cp -r lib/* $(DEST)/lib

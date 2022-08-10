.PHONY: deploy lib all

DEST := /media/${USER}/CIRCUITPY

deploy:
	cp code.py $(DEST)
lib:
	cp -r keyboard/ $(DEST)/lib

all: deploy lib

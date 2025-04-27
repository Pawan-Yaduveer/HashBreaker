DESTDIR ?= /usr/local/bin

install:
	@sudo cp hash.py $(DESTDIR)/hashbreaker
	@sudo chmod +x $(DESTDIR)/hashbreaker
	@echo "Installation Successful! HashBreaker is installed as 'hashbreaker'"

uninstall:
	@sudo rm -f $(DESTDIR)/hashbreaker
	@echo "HashBreaker has been removed"

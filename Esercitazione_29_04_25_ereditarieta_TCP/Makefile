# Makefile

# Comandi base
run-client:
	python3 -m client.MagazzinoProxy

run-server:
	python3 -m server.MagazzinoServer

# Pulizia dei file .pyc e __pycache__
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
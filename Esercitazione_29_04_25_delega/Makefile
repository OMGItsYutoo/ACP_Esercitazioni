# Makefile

# Comandi base
run-client-preleva:
	python3 -m client.Client preleva 12122

run-client-deposita:
	python3 -m client.Client deposita 12122

run-server:
	python3 -m server.MagazzinoServer

# Pulizia dei file .pyc e __pycache__
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
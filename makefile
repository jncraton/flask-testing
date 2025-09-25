all:

clean:
	rm -rf __pycache__
	rm -rf webapp/__pycache__
	rm -rf tests/__pycache__

test:
	pytest

run:
	flask --app webapp/app.py run

prod:
	python3 -m gunicorn -w 4 "webapp.app:app"

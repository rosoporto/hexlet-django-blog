start:
	python3 manage.py runserver 0.0.0.0:8080

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

test: migrate
	python3 manage.py test tests/

console:
	python3 manage.py shell_plus --ipython
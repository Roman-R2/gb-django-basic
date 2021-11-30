start:
	python3.10 shop/manage.py runserver

collectstatic:
	python3.10 shop/manage.py collectstatic

migrate:
	python3.10 shop/manage.py makemigrations
	python3.10 shop/manage.py migrate

superuser:
	python3.10 shop/manage.py createsuperuser --noinput

loaddata:
	python3.10 shop/manage.py loaddata category
	python3.10 shop/manage.py loaddata product

restore-db:
	rm -f shop/db.sqlite3
	rm -fr shop/mainapp/migrations
	mkdir shop/mainapp/migrations
	touch shop/mainapp/migrations/__init__.py
	make migrate
	make superuser
	make loaddata
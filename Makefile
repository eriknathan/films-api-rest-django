# ----------------------------------------------------------------
# Comandos para subir a aplicação

run:
	@python3 manage.py runserver

# ----------------------------------------------------------------
# Comandos para banco de dados

makemigrations :
	@python3 manage.py makemigrations 

migrate:
	@python3 manage.py migrate

dball: makemigrations migrate

# ----------------------------------------------------------------
# Criar novo Super Usuário

superuser:
	@python3 manage.py createsuperuser
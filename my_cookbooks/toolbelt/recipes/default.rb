include_recipe "python::pip"

# Installs django-toolbelt (django + psycopg2 + dburl)
python_pip "django-toolbelt"

# Installs south (DB migrations)
python_pip "south"

# Installs south (DB migrations)
python_pip "pil"

For an ideal development environment, the entire project is set up for automatic reloading of all assets in development.

### Starting the Frontend Server

```
cd theme/
yarn run watch
```

### Starting the Django Livereload Server

```
poetry run python manage.py livereload --ignore-static-dirs
```

### Starting the Django Dev Server

``` 
poetry run python manage.py runserver
```
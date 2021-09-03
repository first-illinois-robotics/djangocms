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

### Getting initial data

By default, the website will not load since there is no data for the required pages (program main pages, home page, etc).
This can be fixed by loading the provided default fixture after apply database migrations:

```
poetry run python manage.py migrate
poetry run python manage.py loaddata initial_data
```

If the initial data is our of date, a new fixture can be overwritten using this command from the home directory of 
the repository:

```
poetry run python manage.py dumpdata -o firweb/fixtures/initial_data.json --exclude contenttypes --exclude admin.logentry --exclude sessions --exclude auth.permission
```
Keep in mind that this command will store all current data, including a default user and their (hashed) password. 
There should be a super user in this data with the username "admin" and the password "first-robotics" for testing.

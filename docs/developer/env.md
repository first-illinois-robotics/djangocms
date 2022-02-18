For an ideal development environment, the entire project is set up for automatic reloading of all assets in development.

### Install

This project uses the [Poetry](https://python-poetry.org/) project management tools. This is essentially a combined 
version of Pip and venv tools. To install the dependencies in the project and also create a virtual environment for the 
project to use, execute the following command:

``` 
poetry install
```

### Starting/building the Frontend Server
There are two options for how to run the frontend system using development. 
If you are changing anything in the `frontend/` directory with your work, you should run webpack/yarn
in watch mode, with the following commands:

```
cd frontend/
yarn run watch
```

This spawns a separate server on port 9000 to serve the front end materials. If you kill the `yarn run watch` command, 
this server will die and your assets (JS, CSS, etc) will stop being available, rendering the site... very hard to use.

If you are not modifying the `frontend/` directory at all, and only modifying or testing the python side of the project,
you can simply build a developer version to be served locally:


```
cd frontend/
yarn run build_dev
```

### Starting the Django Livereload Server

This isn't necessary, but if you're modifying templates or views and want to see your results reflected immediately 
on file save without having to reload your browser, this can make your life much easier. If not, you can just ignore 
this command entirely. You'll notice an error in the browser console, but this can be safely ignored. 

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

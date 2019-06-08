This project was bootstrapped with [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/).

## Available Scripts

In the project directory, you can run:

### `./manage.py migrate`

Once the clone is completed, run the above command to create a db file (using sqlite 3 for development purpsose).
Although, you can change it to other database such as mysql, postgress from the settings.py file

### `./manage.py runserver`

Runs the app in the development mode.<br>
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


### `./manage.py createsuperuser`
Run this command to create a super user - with this you can login on admin site:
Open [http://localhost:8000/admin/](http://localhost:8000/admin/) to view it in the browser.


### `./manage.py fixtures` (Optional)
Run this command to create rows in database tables.


## Project API URLs
All APIS can be called if the user is authenticated else it will throw validation error


### `http://localhost:8000/rest-auth/login/`
This url accepts only post request will check if the Table Login has a specific ip address from where only the can login.
If there is no such object for that user then the user can login from anywhere

### `http://localhost:8000/api/statistics/class?data=<class/standand name>`
This url expects the class/standard name. This can get from Report table - col: std.
### `http://localhost:8000/api/statistics/student?data=<class/standand name>`
This url expects the student name or id. This can get from IdMapping table - col: id, name.
### `http://localhost:8000/api/statistics/year?data=<class/standand name>`
This url expects passing year of student. This can get from Report table - col: year.
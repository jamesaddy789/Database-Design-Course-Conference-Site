James Curtis Addy

How to get to site as user:
- python needs to be installed
- install django using "pip install django" in command shell
- go to conference_site folder where manage.py is located and open a command shell there
- run the command "python manage.py runserver" to start the local server
- copy and paste the ip address url "http://127.0.0.1:8000/" into a browser's url bar
- now you should be at the site


How to log into the Admin page:
- to log into the admin page, run "python manage.py createsuperuser" in a command shell in the conference_site folder where manage.py is located
- after creating the username and password, copy and paste the url "http://127.0.0.1:8000/admin"
- enter the username and password to log in

The database tables are defined in conference_site/conferences/models.py file.
Most of the application logic is handled in conference_site/conferences/views.py.
The html templates are in conference_site/conferences/templates/conferences.
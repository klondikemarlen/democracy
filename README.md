# Tenacity [a.k.a. 10-ant-city]
A web based interactive democracy platform.

Live at at (though still pre-Alpha): https://tenacity.pythonanywhere.com/static/login.html<br>
Frontend repository located at: https://github.com/klondikemarlen/tenacity-frontend

> Recently migrated from https://democracy.pythonanywhere.com/static/login.html.

For more information see the [Wiki](https://github.com/klondikemarlen/tenacity/wiki)

Basic development usage:

`git clone https://github.com/klondikemarlen/tenacity.git`  # clone the repository

`cd tenacity`  # enter the repository

`virtualenv -p python3.6 ENV`  # create a virtual environment using python3.6

`source ENV/bin/activate`  # activate virtual environment

`pip install -r requirements.txt`  # install all project requirements

`python manage.py`  # list app management options.

`python manage.py reset_db`  # build a new database with junk data, may need to create the database manually.
Will need to setup and configure MySQL manually.

`python manage.py runserver`  # run the server

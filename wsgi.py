# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

# located on server at: /var/www/tenacity_pythonanywhere_com_wsgi.py

import sys

# add your project directory to the sys.path
project_home = u'/home/tenacity/tenacity'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from tenacity import app as application  # noqa

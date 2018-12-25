# tenacity/cache_buster/views.py
import os

from flask import Blueprint, current_app
from flask import current_app
# from tenacity import app

from .file_helpers import get_last_modified_time, \
    check_static_link


cache_buster_blueprint = Blueprint('cache_buster', __name__)


# cache busting algorithm from https://eskimon.fr/simple-flask-cache-buster
@cache_buster_blueprint.before_app_first_request
def startup():
    if not current_app.config['TESTING']:
        current_app.logger.info('Checking static link')
        last_modified_date = get_last_modified_time(current_app)
        check_static_link(last_modified_date, current_app)

        # import pdb;pdb.set_trace()
        # Cache Buster (return static url amended with last timestamp)
        @current_app.before_app_first_request
        def static_cache_buster(endpoint, values):
            import pdb;pdb.set_trace()
            if endpoint in 'static':
                values['filename'] = os.path.join(last_modified_date, values['filename'])
                current_app.logger.info('Dynamically replacing static link?')

        # import pdb;pdb.set_trace()
        # current_app.url_value_preprocessors['static'] = static_cache_buster


# tenacity/cache_buster/views.py
import os

from flask import Blueprint, current_app

from tenacity.cache_buster.file_helpers import get_last_modified_time, \
    check_static_link


cache_buster_blueprint = Blueprint('cache_buster', __name__)


# cache busting algorithm from https://eskimon.fr/simple-flask-cache-buster
@cache_buster_blueprint.before_app_first_request
def startup():
    current_app.logger.info('Checking static link')
    last_modified_date = get_last_modified_time()
    check_static_link(last_modified_date, current_app)

    # Cache Buster (return static url amended with last timestamp)
    @cache_buster_blueprint.url_defaults
    def static_cache_buster(endpoint, values):
        if endpoint in 'static':
            values['filename'] = os.path.join(last_modified_date, values['filename'])

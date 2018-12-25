import os


def get_last_modified_time():
    """Get the timestamp of the most recent modified file"""
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames]
    timestamp = 0
    for f in files:
        if os.path.isfile(f):
            timestamp = max(timestamp, int(os.stat(f).st_mtime))
    return str(timestamp)


def check_static_link(timestamp, app):
    """
    Check that we have a link to the static folder
    The link should be <timestamp -> .> (ln -s . timestamp)
    inside static folder
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
    # Unlink previous links
    files = os.listdir(path)
    for f in files:
        if os.path.islink(os.path.join(path, f)):
            if os.readlink(os.path.join(path, f)) == path:
                app.logger.info('Remove old link {}'.format(f))
                os.unlink(os.path.join(path, f))
    # Create the newest link
    app.logger.info('Create link to static {}'.format(os.path.join(path, timestamp)))
    os.symlink(path, os.path.join(path, timestamp))

import os


def get_last_modified_time(app):
    """Get the timestamp of the most recently modified file.

    This only refers to files in the current app's static folder.
    """
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(app.static_folder) for f in filenames]
    timestamp = 0
    for f in files:
        if os.path.isfile(f):
            timestamp = max(timestamp, int(os.stat(f).st_mtime))
    return str(timestamp)


def check_static_link(timestamp, app):
    """Check that we have a link to the static folder.

    This only refers to files in the current app's static folder.
    The link should be <timestamp -> .> (ln -s . timestamp) inside static
    folder.
    """
    static_path = app.static_folder
    # Unlink previous links
    files = os.listdir(static_path)
    for name in files:
        abs_file_path = os.path.join(static_path, name)
        if os.path.islink(abs_file_path):
            if os.readlink(abs_file_path) == static_path:
                app.logger.info('Remove old link {}'.format(name))
                os.unlink(abs_file_path)
    # Create the newest link
    app.logger.info('Create link to static {}'.format(os.path.join(static_path, timestamp)))
    os.symlink(static_path, os.path.join(static_path, timestamp))

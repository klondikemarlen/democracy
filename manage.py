import pytest
from flask import current_app
from flask_script import Manager, Command
from tenacity import app, db


manager = Manager(app)


@manager.add_command
class TestCommand(Command):
    """Runs unit tests.

    This should be run:
    `python manage.py test`

    or to pass argmuents to pytest
    `python manage.py test -v`
    equivalent of
    `pytest tests -v`
    """
    name = 'test'
    capture_all_args = True

    def run(self, command=None):
        pytest.main(['tests'] + command)


@manager.command
def init_db():
    """Initialize the database."""
    db.create_all()
    print("Create all tables.")


@manager.command
def drop_db():
    """Drop the database."""
    # db.engine.execute("SET FOREIGN_KEY_CHECKS=0;")
    db.drop_all()
    # db.engine.execute("SET FOREIGN_KEY_CHECKS=1;")
    print("Drop all tables.")


@manager.command
def populate_db():
    """Add data to the database."""
    with current_app.open_resource('static/all.sql', 'rb') as f:
        for line in f:
            db.engine.execute(line.decode('utf8'))


@manager.command
def reset_db():
    """Drops then rebuilds the database."""
    # os.system('mysql --defaults-file=private_mysql_config.cnf -e "DROP DATABASE IF EXISTS {name};"'.format(
    #         name=private_config.DATABASE_NAME))
    #     print("Database deleted!")
    #     os.system(
    #         'mysql --defaults-file=private_mysql_config.cnf -e '
    #         '"CREATE DATABASE IF NOT EXISTS {name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"'.format(
    #             name=private_config.DATABASE_NAME))
    #     print("Database recreated!")
    drop_db()
    init_db()
    populate_db()
    print("Database recreated!")


if __name__ == '__main__':
    manager.run()

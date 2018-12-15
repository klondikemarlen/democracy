import setuptools

setuptools.setup(
    name="tenacity",
    packages=["tenacity"],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-JSON',
        'flask-sqlalchemy',
        'flask-wtf',
        'flask-login',
        'flask_mail',
        'sqlalchemy',
        'werkzeug',
        'wtforms',
        'flask-sslify',
        'mysqlclient',
        'pytest',
        'Flask-Testing',
        'pyjwt',
        'flask-bcrypt'
    ]
)

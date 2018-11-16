import setuptools

setuptools.setup(
    name="democracy",
    packages=["democracy"],
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
        'flask-sslify'
    ]
)

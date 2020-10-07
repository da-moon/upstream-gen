# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='upstream-gen',
    version='0.1.0',
    description='simple web server to be used as upstream for experimenting with load balancer traffic',
    python_requires='==3.*,>=3.7.0',
    author='da-moon',
    author_email='damoon.azarpazhooh@ryerson.ca',
    license='MIT',
    entry_points={"console_scripts": ["upstream-gen = main:main"]},
    packages=['upstream_gen', 'upstream_gen.defaults'],
    package_dir={"": "."},
    package_data={"upstream_gen": ["server/templates/*.html"]},
    install_requires=[
        'apispec==3.*,>=3.3.2', 'certifi==2020.*,>=2020.6.20',
        'chardet==3.*,>=3.0.4', 'click==7.*,>=7.1.2', 'docopt==0.*,>=0.6.2',
        'flasgger==0.*,>=0.9.5', 'flask==1.*,>=1.1.2',
        'flask-restful==0.*,>=0.3.8', 'gunicorn==20.*,>=20.0.4',
        'idna==2.*,>=2.10.0', 'itsdangerous==1.*,>=1.1.0',
        'jinja2==2.*,>=2.11.2', 'jsonschema==3.*,>=3.2.0',
        'markupsafe==1.*,>=1.1.1', 'marshmallow==3.*,>=3.8.0',
        'mistune==0.*,>=0.8.4', 'pbr==5.*,>=5.5.0',
        'python-dateutil==2.*,>=2.8.1', 'pytz==2020.*,>=2020.1.0',
        'pyyaml==5.*,>=5.3.1', 'requests==2.*,>=2.24.0', 'six==1.*,>=1.15.0',
        'urllib3==1.*,>=1.25.10', 'werkzeug==1.*,>=1.0.1'
    ],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
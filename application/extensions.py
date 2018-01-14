# -*- coding: utf-8 -*-
"""
    extensions.py
    ~~~~~~~~~~~~~
    flask extension instatiations
"""

from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_caching import Cache
from flask_celery import Celery


db = SQLAlchemy()
moment = Moment()
cache = Cache()
celery = Celery()

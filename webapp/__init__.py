# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position,wrong-import-order
"""Webapp module. Gateway to external apps."""

from flask import Flask

from .config import UPLOAD_FOLDER

app = Flask(__name__,
            template_folder='templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '0g1o2w3t4h5a6m'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from webapp import views  # noqa: F401

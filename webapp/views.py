# -*- coding: utf-8 -*-
"""View handler for the application."""
import os

from flask import flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

from webapp import app
from .config import ALLOWED_EXTENSIONS


def allowed_file(filename):
    """
    Helper to check for file name extensions.

    :param: None
    :return: Boolean
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Main route handler.

    Uploads the file to the server.

    :param: None
    :return: str
    """
    if request.method == 'POST':
        # Check if the POST request has the file part.
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_to_upload = request.files['file']
        # If user does not select file, browser submits an empty part without filename.
        if file_to_upload.filename == '':
            flash('No file selected!')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                             filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('index.html')

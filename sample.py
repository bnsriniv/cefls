# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'Hey its Python Flask application!'

# if __name__ == '__main__':
#   app.run()


import logging
from flask import Flask, current_app, render_template, redirect, url_for, request
from flask_session import Session
from pathlib import Path
import app_config
from ms_identity_web import IdentityWebPython
from ms_identity_web.adapters import FlaskContextAdapter
from ms_identity_web.errors import NotAuthenticatedError
from ms_identity_web.configuration import AADConfig


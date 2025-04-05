#!/usr/bin/python

import os

DEFAULT_TLD  = os.getenv('DEFAULT_TLD',  'co.jp')
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ja')

from flask import Flask, request, Response
from flask_cors import CORS  # Add flask-cors for CORS support
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing cross-origin requests

@app.route('/<path:text>.mp3')
def mp3(text):
    tld  = request.args.get('tld',  DEFAULT_TLD)
    lang = request.args.get('lang', DEFAULT_LANG)
    fp   = BytesIO()

    gTTS(text, tld, lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
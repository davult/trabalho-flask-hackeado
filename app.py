import os
import sys
import time

from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from werkzeug.utils import secure_filename

from arquivo import Arquivo, ArquivoBinario
from arquivo_dao import ArquivoDao, ArquivoBinarioDao

arquivo_dao = ArquivoDao()
arquivo_dao_bin = ArquivoBinarioDao()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

'''

Aqui voce ira programar 
toda a parte de uploads

'''

def main():
    app.env = 'development'
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()

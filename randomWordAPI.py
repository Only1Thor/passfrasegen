#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

alleOrd=[]
import codecs
with codecs.open('ordliste.txt','r','utf-8') as ordlisteFil:
    for line in ordlisteFil:
        alleOrd.append( line )


@app.route('/')
def get():
    return jsonify(random.choice(alleOrd)), 200

app.run(debug=True, host='0.0.0.0',port='8080')
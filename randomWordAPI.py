from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

alleOrd=[]
import codecs
with codecs.open('ordliste.txt', encoding='utf-8') as ordlisteFil:
    for line in ordlisteFil:
        alleOrd.append( line )


class RandomWord(Resource):
    def get(self,id=0):
        words=[]
        # for i in id:
        #     words.append(random.choice(alleOrd))
        return str(random.choice(alleOrd)), 200
    def get(self):
        words=[]
        # for i in id:
        #     words.append(random.choice(alleOrd))
        return str(random.choice(alleOrd)), 200

api.add_resource(RandomWord, "/randomWord", "/randomWord/<int:id>")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
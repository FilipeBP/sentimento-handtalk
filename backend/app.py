from flask import Flask, jsonify, request
from flask_cors import CORS
from preprocess import CustomTransformer
import joblib
import numpy as np

#Instância do app
app = Flask(__name__)

#Criando o pré-processador
pre_pt = CustomTransformer('portuguese')

#Modelos para análise de sentimento
model_pt = joblib.load('../modelos/model-pt.sav')

#Configurações da webpage
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        post_data = request.get_json()
        frase = 'A DEFINIR'
        print(frase)

        frase = pre_pt.transform(frase)
        classes = ['felicidade', 'raiva', 'tristeza']

        proba = model_pt.predict(frase)

        response_data = {'predicao': classes[np.argmax(proba)],
                        'probabilidades': {
                            'felicidade': round(proba[0], 4),
                            'raiva': round(proba[1], 4),
                            'tristeza': round(proba[2], 4)
                        }}
        return jsonify(response_data)
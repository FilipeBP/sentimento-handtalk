from flask import Flask, jsonify, request, make_response
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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        post_data = request.get_json()
        frase = [post_data['phrase']]

        frase = pre_pt.transform(frase)
        classes = ['felicidade', 'raiva', 'tristeza']

        proba = model_pt.predict_proba(frase)

        response_data = {'predicao': classes[np.argmax(proba)],
                        'probabilidades': {
                            'felicidade': round(float(proba[0 ,0])*100, 2),
                            'raiva': round(float(proba[0, 1])*100, 2),
                            'tristeza': round(float(proba[0 ,2])*100, 2)
                        }}
        print(response_data)
        return jsonify(response_data)
    return make_response(jsonify('sucesso', 201))
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import nltk
import re

#Definindo o pré-processador para o vetorizador
class CustomTransformer(BaseEstimator, TransformerMixin):
  def __init__(self, language):
    #Baixa as stopwords
    #nltk.download('stopwords')
    self.language = language

  def fit(self, X, y=None):
    return self

  def transform(self, X, y=None):
    if isinstance(X, pd.core.series.Series) or isinstance(X, pd.core.frame.DataFrame):
      return X.apply(lambda x: self.preprocessador(x))
    if isinstance(X, list):
      return map(lambda x: self.preprocessador(x), X)

  def preprocessador(self, instancia):
    #Removendo stopwords
    stopwords = set(nltk.corpus.stopwords.words(self.language))

    #Retirando o 'não' ou 'no' das stopwords
    if self.language == 'portuguese':
        stopwords.remove('não')
    if self.language == 'english':
        stopwords.remove('no')

    #Removendo caracteres indesejados
    instancia = [p.lower() for p in instancia.split() if p.lower() not in stopwords]
    instancia = " ".join(instancia)

    instancia = re.sub("[,.;/\[\]?!\'\"]", '', instancia)
    return instancia
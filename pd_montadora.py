import pandas as pd
from pymongo import MongoClient

#informações
data = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']
}

df = pd.DataFrame(data)

#conexão
client = MongoClient('mongodb://localhost:27017/')
db = client['teste_leonardo'] 
collection = db['Montadoras'] 


data_to_insert = df.to_dict(orient='records')

collection.insert_many(data_to_insert)

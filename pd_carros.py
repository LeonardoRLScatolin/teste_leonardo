import pandas as pd
from pymongo import MongoClient

#informações
carros_data = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}

df_carros = pd.DataFrame(carros_data)

#conexão
client = MongoClient('mongodb://localhost:27017/') 
db = client['teste_leonardo']
collection_carros = db['Carros']  


data_to_insert = df_carros.to_dict(orient='records')


collection_carros.insert_many(data_to_insert)

print("Dados dos carros salvos no MongoDB com sucesso!")

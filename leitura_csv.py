import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/IOT-temp.csv')  # Ajuste se necessário
print("Arquivo CSV carregado com sucesso!")  # Verificação de leitura do CSV
engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
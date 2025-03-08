# Pipeline-de-Dados-IoT
Dashboard de Temperaturas IoT

Introdução

Este projeto consiste em um Pipeline de Dados IoT que coleta, processa e analisa dados de temperatura provenientes de dispositivos IoT. Os dados são armazenados em um banco de dados, onde são transformados e disponibilizados para visualização em um dashboard interativo.

Configuração do Ambiente

Requisitos

Python 3.x

Docker e Docker Compose (opcional para banco de dados)

Bibliotecas Python necessárias (listadas no requirements.txt)

Banco de dados (PostgreSQL recomendado)(Usado Dbeaver)

Instalação

Clone o repositório:

git clone https://github.com/TheGuilhermeDias/Pipeline-de-Dados-IoT.git
cd Pipeline-de-Dados-IoT

Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
pip install -r requirements.txt

Configure as variáveis de ambiente (.env ou exporte manualmente):

DATABASE_URL=dbeaver://usuario:senha@localhost:5432/iot_db

Execute as migrações do banco de dados (se necessário):

python manage.py migrate

Inicie o servidor do dashboard:

streamlit run app.py

Dashboard

O dashboard apresenta diversas visualizações dos dados coletados:

Média de Temperatura por Dispositivo
### Média de Temperatura por Dispositivo
![Média de Temperatura por Dispositivo](img/dashboard.png)


Este gráfico exibe a média de temperatura registrada por cada dispositivo IoT.
### Temperatura Máxima e Mínima por Dia
![Temperatura Máxima e Mínima por Dia](img/temperatura.png)
### Leituras por Hora
![Leituras por Hora](img/leitura.png)

Leituras por Hora


Mostra a quantidade total de leituras feitas ao longo do dia, agrupadas por hora.

Temperatura Máxima e Mínima por Dia


Apresenta as temperaturas máxima e mínima registradas diariamente ao longo do tempo.

Views SQL

O projeto utiliza algumas views SQL para facilitar a análise dos dados. Aqui estão algumas delas:

View: avg_temp_per_device

CREATE VIEW avg_temp_per_device AS
SELECT device_id, AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;

Objetivo: Calcula a média de temperatura para cada dispositivo.

View: readings_per_hour

CREATE VIEW readings_per_hour AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS total_leituras
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

Objetivo: Obtém a quantidade de leituras por hora.

View: daily_temp_extremes

CREATE VIEW daily_temp_extremes AS
SELECT DATE(timestamp) AS data,
       MAX(temperature) AS temp_maxima,
       MIN(temperature) AS temp_minima
FROM temperature_readings
GROUP BY data
ORDER BY data;

Objetivo: Calcula as temperaturas máxima e mínima registradas a cada dia.

Insights

Com base nos dados coletados, podemos observar os seguintes insights:

Picos de leitura: O maior volume de leituras ocorre por volta das 15h, indicando um possível aumento de uso dos dispositivos nesse horário.

Variação de temperatura: Durante alguns períodos, há uma oscilação significativa entre temperaturas máximas e mínimas, o que pode indicar variações climáticas ou falhas em sensores.

Dispositivo com maior temperatura média: O dispositivo "Room Admin" apresenta a maior média de temperatura, o que pode indicar uma localização específica com alta temperatura ambiente.

Conclusão

Este projeto demonstra a importância do pipeline de dados para a análise de sensores IoT. O dashboard permite uma visão clara das tendências e variações de temperatura ao longo do tempo, facilitando a tomada de decisões baseada em dados. 
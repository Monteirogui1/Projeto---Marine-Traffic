import requests
from datetime import datetime
import pandas as pd
from classes import Infos, GerenciaPlanilha

shipid = input('Digita ai: ')

result = Infos(shipid).infos
data_i = Infos(shipid).get_info()
data_l = Infos(shipid).get_loc()

name = data_i['name']
imo = data_i['imo']
lat = data_l['lat']
lon = data_l['lon']
ts = datetime.utcfromtimestamp(data_l["lastPos"])
data_d = ts.strftime('%d-%m-%Y')
hora = ts.strftime('%H:%M:%S')

print(f'Nome: {name} \n IMO: {imo} \n Latitude: {lat} \n Longitude: {lon} \n Data e Hora: {data_d} {hora} ')
            



# def resul():
#     dic = []

#     data = get_loc('408916')
#     data_i = get_info('408916')
#     name = data_i['name']
#     imo = data_i['imo']
#     lat = data['lat']
#     lon = data['lon']
#     ts = datetime.utcfromtimestamp(data["lastPos"])
#     data_d = ts.strftime('%d-%m-%Y')
#     hora = ts.strftime('%H:%M:%S')
#     print(f'Nome: {name} \n IMO: {imo} \n Latitude: {lat} \n Longitude: {lon} \n Data e Hora: {data_d} {hora}')

#     dic.append({
#         'imo': imo,
#         'name': name,
#         'Latitude': lat,
#         'Longitude': lon,
#         'Data': data_d,
#         'Hora': hora,
#     })

#     dic = pd.DataFrame(dic)



#     dic.to_excel(f'{name} - {imo}.xlsx')

# resul()


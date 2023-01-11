import pandas as pd
import requests
from datetime import datetime

class Infos:
    def __init__(self, shipid: str = ""):
        self.shipid = shipid

    def get_loc(self):
        url = f"https://www.marinetraffic.com/vesselDetails/latestPosition/shipid:{self.shipid}"

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def get_info(self):
        url = f"https://www.marinetraffic.com/vesselDetails/vesselInfo/shipid:{self.shipid}"

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    # def infos(self):
    #     data_i = self.get_info()
    #     data_l = self.get_loc()

    #     self.name = data_i['name']
    #     self.imo = data_i['imo']
    #     self.lat = data_l['lat']
    #     self.lon = data_l['lon']
    #     ts = datetime.utcfromtimestamp(data_l["lastPos"])
    #     self.data_d = ts.strftime('%d-%m-%Y')
    #     self.hora = ts.strftime('%H:%M:%S')

    #     #print(f'Nome: {name} \n IMO: {imo} \n Latitude: {lat} \n Longitude: {lon} \n Data e Hora: {data_d} {hora} ')
            


class GerenciaPlanilha:
    def __init__(self):
        self.df = pd.read_excel('Sondas.xlsx')
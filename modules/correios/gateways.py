import string
import json
import requests
from sys import exit
from infrastructure.config import Environments

class CorreiosGateway():
    """Whapper para API de acesso gratuíto de consulta de ceps e endereços"""

    def __init__(self,):
        pass


    def endereco(self, cep:string = None) -> string:
        url_api = (f'{Environments.VIACEP_URL}/ws/%s/json' % cep)
        req = requests.get(url_api)
        if req.status_code == 200:
            dados_json = json.loads(req.text)
            return dados_json
        else:
            return None


if __name__ == '__main__':
    end = CorreiosGateway().endereco('14027250')            
    print(end)
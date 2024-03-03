import requests
import json

api_key = "cae0ccf67bf64a578070e1b787bcf1e3"
input_claim = "The sky is blue."

# Ruta del Endpoint del webservice
api_endpoint = f"https://idir.uta.edu/claimbuster/api/v2/score/text/{input_claim}"
request_headers = {"x-api-key": api_key}

# Lanzamos el get con la libreria de request
api_response = requests.get(url=api_endpoint, headers=request_headers)

# Imprimos la respuesta del json
print(api_response.json())

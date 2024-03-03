import requests

# API Key
api_key = "AIzaSyAdMZyEh6qs06AebTuwMrtjAiui7yrapFM"

# Remplazar por el hecho a verificar
claim = "chemtrails"


url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?key={api_key}&query={claim}"
print(url)

# Mandar request
response = requests.get(url)

# Chequear codigo de respuesta 
if response.status_code == 200:
    # Respuesta JSON
    fact_check_results = response.json()

    # Imprimir Resultado
    print(fact_check_results)
else:
    print(f"Error fetching fact check results: {response.status_code}")
    print(response.json())

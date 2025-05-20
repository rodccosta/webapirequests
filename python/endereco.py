import requests 

cep = str(input("Digite o CEP"))
if (len(cep) !=8):
    print("CEP inválido")

url = "https://brasilapi.com.br/api/cep/v1/"+cep
print(url)
response = requests.get(url)
#print(response.status_code)
if response.status_code == 200:
    
    json = response.json() 
    '''
    # consultando os campos do json
    for entry in json: 
        print(json[entry]) '''
    print("Endereço: ",json["street"])
    print("Bairro:   ",json["neighborhood"])
    print("Cidade:   ",json["city"])
    print("Estado:   ",json["state"])

else: 
    print("Erro ao consultar a API") 

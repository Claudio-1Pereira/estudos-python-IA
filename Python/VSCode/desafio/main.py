import json
from contato_com_llm import recebe_linha_e_retorna_json

lista_resenha = []

with open('Resenhas_App_ChatGPT.txt', 'r', encoding='utf-8') as arquivo:
  for linha in arquivo:
    lista_resenha.append(linha.strip())

lista_de_resenhas_json = []

for resenha in lista_resenha:
  resenha_json = recebe_linha_e_retorna_json(resenha)
  resenha_dict = json.loads(resenha_json)
  lista_de_resenhas_json.append(resenha_dict)


def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_de_dicionarios_str = []

    for dicionario in lista_de_dicionarios:
        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1
        
        lista_de_dicionarios_str.append(str(dicionario))

    
    texto_unidos = "#####".join(lista_de_dicionarios_str)

    return contador_positivas, contador_positivas, contador_neutras, texto_unidos

pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)
print(f"Positivas: {pos}\n")
print(f"Negativas: {neg}\n")
print(f"Neutras: {neut}\n")
print(textos)
    
    
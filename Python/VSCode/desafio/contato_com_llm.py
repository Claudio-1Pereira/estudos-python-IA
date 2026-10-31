from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role": "system", "content": """
            Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português, deve esta sempre na língua portuguesa
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0
    )
    resposta = resposta_do_llm.choices[0].message.content.replace("```json", "").replace("```", "")
    return resposta
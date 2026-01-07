#!/usr/bin/python3
import urllib.request
import urllib.parse
import json
import sys

print("🤖 Chatbot Wikipedia Light")
print("Pergunte: 'O que é [coisa]?' ou 'Quem foi [pessoa]?'")
print("Digite 'sair' para sair\n")

while True:
    try:
        pergunta = input("Você: ").strip().lower()
        
        if pergunta == 'sair':
            print("Bot: Até mais!")
            break
            
        termo = ""
        if 'o que é' in pergunta:
            termo = pergunta.replace('o que é', '').strip()
        elif 'quem foi' in pergunta:
            termo = pergunta.replace('quem foi', '').strip()
        elif 'quem é' in pergunta:
            termo = pergunta.replace('quem é', '').strip()
        else:
            print("Bot: Formato: 'O que é PYTHON?' ou 'Quem foi EINSTEIN?'")
            continue
        
        if termo:
            print("Bot: Pesquisando...")
            
            # Usa API mais leve da Wikipedia
            url = f"https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={urllib.parse.quote(termo)}&redirects=1"
            
            with urllib.request.urlopen(url) as r:
                dados = json.loads(r.read().decode('utf-8'))
                paginas = dados.get('query', {}).get('pages', {})
                
                for pagina in paginas.values():
                    if 'extract' in pagina:
                        texto = pagina['extract']
                        print(f"Bot: {texto[:400]}...")
                        break
                else:
                    print("Bot: Não encontrei. Tente outro termo.")
                    
    except KeyboardInterrupt:
        print("\n\nBot: Encerrando...")
        break
    except Exception as e:
        print(f"Bot: Erro: {str(e)[:50]}")

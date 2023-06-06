import requests
from googlesearch import search

TOKEN = '6218021420:AAFqzhDAr26JxUKmA0B23kA6TpM6D-slb0o'
API_URL = f"https://api.telegram.org/bot{TOKEN}"

active = True  # Variável para controlar o estado do bot

def start(update):
    chat_id = update['message']['chat']['id']
    text = "Olá! Digite algo para pesquisar."
    send_message(chat_id, text)


def perform_search(update):
    chat_id = update['message']['chat']['id']
    termo_pesquisa = update['message']['text']
    search_results = google_search(termo_pesquisa)
    if search_results:
        response = "\n\n".join(search_results)
    else:
        response = "Nenhum resultado encontrado."
    send_message(chat_id, response)


def stop(update):
    global active
    chat_id = update['message']['chat']['id']
    text = "Bot desativado. Para reativá-lo, utilize o comando /start."
    send_message(chat_id, text)
    active = False


def google_search(query):
    results = []
    for result in search(query, num_results=5):
        results.append(result)
    return results

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=params)
    if response.status_code != 200:
        print("Erro ao enviar a mensagem.")

def get_updates(update_id):
    url = f"{API_URL}/getUpdates"
    params = {
        'offset': update_id + 1 if update_id else None,
        'timeout': 10
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter atualizações.")

def process_message(update):
    if "message" in update:
        message = update["message"]
        if "text" in message:
            text = message["text"]
            if text == "/start":
                start(update)
            elif text == "/stop":
                stop(update)
            else:
                perform_search(update)

def main():
    global active
    # Criação do loop de eventos do Telegram
    update_id = None
    while active:
        updates = get_updates(update_id)
        if updates is not None and "result" in updates and len(updates["result"]) > 0:
            last_update = updates["result"][-1]
            update_id = last_update["update_id"]
            process_message(last_update)

if __name__ == '__main__':
    main()

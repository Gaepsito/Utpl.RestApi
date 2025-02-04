import requests

# Configuración de la API de Mailtrap
MAILTRAP_API_KEY = 'tu_api_key'
MAILTRAP_ENDPOINT = 'https://api.mailtrap.io/v1/email/send'

# Configuración de la API de Slack
SLACK_API_KEY = 'tu_api_key'
SLACK_ENDPOINT = 'https://slack.com/api/chat.postMessage'

# Configuración de la API de Telegram
TELEGRAM_API_KEY = 'tu_api_key'
TELEGRAM_ENDPOINT = 'https://api.telegram.org/bot<tu_telegram_bot_token>/sendMessage'

def enviar_correo(email, contenido):
    headers = {
        'Authorization': f'Bearer {MAILTRAP_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'to': email,
        'subject': 'Notificación',
        'body': contenido
    }
    response = requests.post(MAILTRAP_ENDPOINT, headers=headers, json=payload)
    return response.status_code

def enviar_mensaje_slack(channel_id, mensaje):
    headers = {
        'Authorization': f'Bearer {SLACK_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'channel': channel_id,
        'text': mensaje
    }
    response = requests.post(SLACK_ENDPOINT, headers=headers, json=payload)
    return response.status_code

def enviar_mensaje_telegram(chat_id, mensaje):
    headers = {
        'Authorization': f'Bearer {TELEGRAM_API_KEY}'
    }
    payload = {
        'chat_id': chat_id,
        'text': mensaje
    }
    response = requests.post(TELEGRAM_ENDPOINT, headers=headers, json=payload)
    return response.status_code

# Ejemplo de uso
email = 'destinatario@example.com'
contenido = 'Este es un mensaje de prueba.'
enviar_correo(email, contenido)

channel_id = 'C1234567890'
mensaje = 'Este es un mensaje de prueba en Slack.'
enviar_mensaje_slack(channel_id, mensaje)

chat_id = '123456789'
mensaje = 'Este es un mensaje de prueba en Telegram.'
enviar_mensaje_telegram(chat_id, mensaje)

from telebot import TeleBot
import requests


TELEGRAM_BOT_TOKEN = '6852293508:AAE6u-P8pbcK63i2QnpenNXCGLUykWp5AiE'
API_URL = 'http://localhost:8000'

bot = TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_page(request):
    message = "Hello!"
    bot.send_message(request.from_user.id, message)


@bot.message_handler(content_types=["text"])
def messages_from_user(request):
    user_message = request.text.strip()
    body = {"model": "gpt2", "message": user_message}

    message = "Typing..."
    bot.send_message(request.from_user.id, message)

    response = requests.post(f'{API_URL}/generate', json=body)

    message = response.json().get('answer')
    print(message)
    bot.send_message(request.from_user.id, message)


if __name__ == "__main__":
    print('Bot starts')
    bot.polling(none_stop=True, interval=0)

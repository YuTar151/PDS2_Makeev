
import openai
import telebot

openai.api_key = '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'

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Серьезно?",
    temperature=0,
    max_tokens=1000
)

print(response['choices'][0]['text'])





# bot = telebot.TeleBot ("5813990276: AAG2PBsZG2wNMn7Qu_Uy9gjE2iGh2XEsaBM")
#
# message.text = "hello"
# @bot.message_handler(func=lambda _: True)
#
# def handle_message(message):
#     response = openai. Completion.create(
#         model="text-davinci-003",
#         prompt=message.text,
#         temperature=0.5,
#         max_tokens=1000,
#         top_p=1.0,
#         frequency_penalty=0.5,
#         presence_penalty=0.0,
#     )
#     bot.send_message(chat_id=message.from_user.id.text=response[' choices'][0]['text'])
#
#
# bot.polling()

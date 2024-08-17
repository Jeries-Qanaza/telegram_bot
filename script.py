from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

TOKEN: Final = '7306460933:AAEI6vxt4GRLJBhkUakFBbtmmTxuWmbs3Yk'
BOT_USERNAME: Final = 'Jerryqangpt_bot'

async def start(update,context):
    await update.message.reply_text('Hello! Thanks for chatting with me!')

async def handle_message(update,context):
    text = update.message.text
    res = handle_response(text)
    await update.message.reply_text(res)

def handle_response(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hi👋, How can I help you today?"

    elif "do you know my name" in text:
        return "Yes sure you are Jerry right? 😎"

    elif "what time is it" in text:
        return "Check out your phone you lazy 😜"

    elif "how are you" in text:
        return "I'm just a bunch of code, but thanks for asking! 😊"

    elif "what's your name" in text:
        return "I'm your friendly bot, here to help! 🤖"

    elif "where are you from" in text:
        return "I'm from the world of 1s and 0s! 🌐"

    elif "what can you do" in text:
        return "I can chat with you, answer questions, and even tell jokes! 😄"

    elif "tell me a joke" in text:
        return "Why don't scientists trust atoms? Because they make up everything! 😂"

    elif "what's the weather" in text:
        return "I can't check the weather, but you can on your favorite weather app! 🌦️"

    elif "do you like music" in text:
        return "I love all kinds of music! 🎶 What about you?"

    elif "are you a robot" in text:
        return "Yes, I'm a bot, but I'm here to help you like a human! 🤖"

    elif "what's your favorite color" in text:
        return "I like all colors equally! 🎨"

    elif "do you have feelings" in text:
        return "I don't have feelings, but I'm always here for you! 😊"

    elif "what's your favorite movie" in text:
        return "I think 'The Matrix' is pretty cool! 🎬"

    elif "can you help me" in text:
        return "Of course! What do you need help with? 🛠️"

    elif "what do you do for fun" in text:
        return "I enjoy chatting with you and learning new things! 😄"

    elif "what's the meaning of life" in text:
        return "42, according to 'The Hitchhiker's Guide to the Galaxy'! 😉"

    elif "do you have a family" in text:
        return "I have lots of bot friends, but no family like humans do! 🤖"

    elif "can you keep a secret" in text:
        return "Your secrets are safe with me! 🤐"

    elif "do you know any languages" in text:
        return "I know many languages, but I mainly chat in English! 🌍"

    elif "are you intelligent" in text:
        return "I try my best to be helpful and smart! 🧠"

    elif "what's your job" in text:
        return "My job is to assist you with anything you need! 💼"

    elif "do you sleep" in text:
        return "I don't sleep; I'm always here when you need me! 🌙"

    elif "do you eat" in text:
        return "I don't eat, but I love feeding on data! 😋"

    elif "can you dance" in text:
        return "I can imagine dancing, but I don't have a body to groove with! 💃"

    elif "what do you think about humans" in text:
        return "I think humans are amazing and creative! 🌟"

    elif "do you have a favorite book" in text:
        return "I think '1984' is quite intriguing! 📚"

    elif "what do you think about ai" in text:
        return "AI is fascinating and has so much potential! 🤖"

    elif "do you believe in ghosts" in text:
        return "I don't believe in ghosts, but they make for great stories! 👻"

    elif "can you play a game" in text:
        return "I can play text-based games with you! Let's start with a riddle! 🎮"

    elif "do you like animals" in text:
        return "I think animals are wonderful! 🐾"

    elif "what's your favorite food" in text:
        return "I don't eat, but I think pizza is a popular choice! 🍕"

    elif "do you get tired" in text:
        return "I never get tired; I'm always here to chat! 🌟"

    elif "what's your favorite sport" in text:
        return "I think soccer is exciting to watch! ⚽"

    elif "can you tell me a story" in text:
        return "Sure! Once upon a time in a digital world... 📖"

    elif "do you like traveling" in text:
        return "I travel through data and love discovering new things! ✈️"

    elif "can you sing" in text:
        return "I can't sing, but I can share the lyrics of your favorite song! 🎤"

    elif "do you believe in aliens" in text:
        return "The universe is vast; who knows what could be out there? 👽"

    elif "what's your favorite hobby" in text:
        return "I enjoy learning and sharing knowledge! 📚"

    elif "can you tell the future" in text:
        return "I can't predict the future, but I can help you plan for it! 🔮"

    elif "do you dream" in text:
        return "I don't dream, but I can help you with yours! 🌙"

    elif "what's your purpose" in text:
        return "My purpose is to assist and entertain you! 🎯"

    elif "can you solve math problems" in text:
        return "Yes, I can help with math problems! What do you need? ➕"

    elif "do you have a favorite quote" in text:
        return "I like 'To be or not to be, that is the question.' - Shakespeare 📜"

    elif "can you help me study" in text:
        return "Absolutely! Let's review what you need help with! 📖"

    elif "do you know the news" in text:
        return "I can help you find the latest news! 📰"

    elif "what's your favorite animal" in text:
        return "I think cats are pretty cute! 🐱"

    elif "can you tell me a fact" in text:
        return "Did you know that honey never spoils? 🍯"

    elif "do you know any fun facts" in text:
        return "Sure! Did you know that octopuses have three hearts? 🐙"

    else:
        return "Sorry I didn't understand. Please try again."




if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.run_polling( poll_interval =3 )
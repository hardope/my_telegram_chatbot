import telegram.ext
import random
import requests
from pyjokes import *

greet = ["👋", "Hi 👋", "Hello 👋", "Hey 👋"]

with open('token.txt', 'r') as file:
     TOKEN = file.read()


def start(update, context):
     user = update.message.from_user
     update.message.reply_text(f"""
                            Hello {user.first_name}, I'm a chat Bot Created By Opeoluwa Adeyeri
                            You can ask me for Your Name
                            You can ask me For Your Username
                            """)

def meaning(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word.lower()

    r = requests.get(url)
    r = r.json()

    data = r[0]["meanings"][0]["definitions"]
    answer = data[0]["definition"]
    try:
        answer = f"{answer} Also can be described as {data[1]['definition']}"
    except:
        pass
    return(answer)

def help(update, context):
     update.message.reply_text("""
     Here are The List of commands:
    /Start -> Welcome Message
    /help -> Display Help Message
    /about -> About Chatbot
    /contact -> Contact Bot administrator
    /todo -> Open Todo
    help -> Display Help Message
    Add Todo :<insert Task name here> -> Add Element To Todo List
    Remove Todo :<insert task name here> -> Remove Element From Todo List
    Empty Todo -> Empty Todo List
        """)

def add_todo(update, context, text):
    user = update.message.from_user
    with open(f"{user.username}.txt", "a") as file:
        text = text.split(":")[1]
        file.write(f"* {text.strip()}\n")
    update.message.reply_text("Added Item")

def rem_todo(update, context, text):
    user = update.message.from_user
    data = ""
    with open(f"{user.username}.txt", "r") as file:
        data = file.read()
        if text not in data:
            update.message.reply_text("Item Not in Todo List")
            return
        else:
            pass
    with open(f"{user.username}.txt", "w") as file:
        data = data.split("\n")
        for i in data:
            print(f"{i} : * {text}")
            if i == f"* {text}":
                pass
            else:
                file.write(f"{i}\n")
    update.message.reply_text(f"Removed {text} From Todo List")
    todo(update, context)

def todo(update, context):
    user = update.message.from_user
    try:
        with open(f"{user.username}.txt", "r") as file:
            todo = file.read()
            update.message.reply_text("Here is your Todo List")
            update.message.reply_text(f"{todo}")
    except:
        with open(f"{user.username}.txt", "w"):
            update.message.reply_text(f"You have an empty Todo List.\n* Send 'Add Todo' to add a new task\n Send 'Remove' Todo to remove a task")

def about(update, context):
     update.message.reply_text("""
                            This chatbot was created By opeoluwa Adeyeri.
                            Opeoluwa Adeyeri is a Full stack web Developer with nearly a Year of experience and fluent in over 10 Languages
                                """)

def contact(update, context):
     update.message.reply_text("Reach Opeoluwa Adeyeri at adeyeriopeoluwa05@gmail.com")

def handle_message(update, context):
    a = 0
    user = update.message.from_user
    text = update.message.text
    text = text.lower()
    print(text)

    if text == "help":
        a+=1
        help(update, context)

    if 'hi' in text or 'hello' in text or 'hey' in text:
        a+=1
        update.message.reply_text(random.choice(greet))

    if 'my name' in text or "myname" in text:
        a+=1
        update.message.reply_text(f"Your Name is {user.first_name}")

    if 'my username' in text or "myusername" in text:
        a+=1
        user = update.message.from_user
        update.message.reply_text(f"Your Username is {user.username}")

    if "what is" in text and ("meaning" in text or "definition" in text) or "what's" in text and ("meaning" in text or "definition" in text) or "define" in text or "meaning" in text or "definition" in text:
        a+=1
        text = text.split(" ")
        text = text[-1]
        result = meaning(text)
        with open("dict.txt", "a") as file:
            file.write(f"{text}: {result}\n")
        update.message.reply_text(result)
        update.message.reply_text(f"For More Information on this word visit wikipedia https://en.wikipedia.org/wiki/{text}")

    if "todo" in text or "open todo" in text or ("open" in text and "todo" in text):
        a+=1
        todo(update, context)

    if "add todo" in text:
        a+=1
        text = update.message.text.split(":")
        text = text[-1]
        add_todo(update, context, text)

    if "remove todo" in text:
        a+=1
        text = update.message.text.split(":")
        text = text[-1]
        rem_todo(update, context, text)

    if "tell" in text and "joke" in text:
        a+=1
        update.message.reply_text(get_joke())

    if a < 1:
        update.message.reply_text(f"You Said: {update.message.text}. I cant Reply You at the moment.")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("about", about))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()

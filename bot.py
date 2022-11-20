import telegram.ext

with open('token.txt', 'r') as file:
     TOKEN = file.read()

def start(update, context):
     user = update.message.from_user
     update.message.reply_text(f"""
Hello {user.first_name}, I'm a chat Bot Created By Opeoluwa Adeyeri
You can ask me for Your Name
You can ask me For Your Username
""")

def help(update, context):
     update.message.reply_text("""
     Here are The List of commands:
/Start -> Welcome Message
/help -> Display Help Message
/about -> About Chatbot
/contact -> Contact Bot administrator
     """)

def about(update, context):
     update.message.reply_text("""
This chatbot was created By opeoluwa Adeyeri.
Opeoluwa Adeyeri is a Full stack web Developer with nearly a Year of experience and fluent in over 10 Languages
     """)

def contact(update, context):
     update.message.reply_text("Reach Opeoluwa Adeyeri at adeyeriopeoluwa05@gmail.com")

def handle_message(update, context):
     text = update.message.text
     if 'hi' in text or 'hello' in text 'hey' in text:
          update.message.reply_text(f"Hello :wave:")
     if 'my name' in text or "MY Name" in text or "My name" in text or "myname" in text:
          user = update.message.from_user
          update.message.reply_text(f"Your Name is {user.first_name}")
     else:
          update.message.reply_text(f"You Said: {text}. I cant Reply You at the moment.")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("about", about))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
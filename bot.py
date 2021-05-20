from telegram import *
from telegram.ext import *
from questions import Questions
import database as db

bot = Bot("1535184201:AAFfNVL7vU59h_QxX46VSFI75xg4-X8gMD4")
updater = Updater("1535184201:AAFfNVL7vU59h_QxX46VSFI75xg4-X8gMD4", use_context=True)
progress = {
    1: "░░░░░░░░░░░░░ 0%",
    2: "██░░░░░░░░░░░ 16%",
    3: "████░░░░░░░░░ 33%",
    4: "██████░░░░░░ 50%",
    5: "████████▒░░░░ 66%",
    6: "██████████▓░░ 83%",
    0: "██████████ 100%",
}
dispatcher = updater.dispatcher


def displayStartMessage(update: Update, context: CallbackContext):
    db.addUser(str(update.effective_chat.id))
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""Welcome brave adventurer! 

It is time for thee to set forth on thy epic journey!

Here is your unique chat id: {update.effective_chat.id}

Head on over to /rules to figure out what you need to do..
        """,
    )
    print(update.effective_chat.id)


def displayQuestion(update: Update, context: CallbackContext):
    questionNumber = db.getUserQuestion(str(update.effective_chat.id))
    if questionNumber == 0:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text="Uuhm... why are you still here? You finished your quest, remember?",
        )
    else:
        question = Questions(questionNumber - 1).question
        bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
        if question["image"]:
            bot.send_photo(chat_id=update.effective_chat.id, photo=question["image"])


def displayRules(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Alright, so here's how this works...
You will be presented with the current question you are on using the /question command.
To submit an answer, type in /answer and then your submission.
For example,

/question
->Where would you find Chuck Norris?
/answer False. Chuck Norris finds you.
->Correct!

/question
-> How many minutes of brooding silence do you get when you combine all the Twilight movies?
/answer 26
-> Correct!

You'll receive a confirmation specifying whether your answer is correct or wrong.

If it is the right answer, the next time you enter /question you will be presented with another question.

Particpants will have 24 hours to go through all the questions and submit their solutions.

You may check your progress at any time by using the /progress command.

Good luck!
        """,
    )


def getAnswer(update: Update, context: CallbackContext):
    questionNumber = db.getUserQuestion(str(update.effective_chat.id))
    if questionNumber == 0:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text="Yes, the answer to life is 42. Anything else?",
        )
    else:
        if len(context.args) == 0:
            bot.send_message(
                chat_id=update.effective_chat.id, text="Add your answer after /answer"
            )
        else:
            question = Questions(questionNumber - 1).question
            ### Possiblity to break with varying argument counts
            submission = str(" ".join(context.args)).lower()
            ###
            if question["answer"] == submission:
                db.updateAnswer(str(update.effective_chat.id), questionNumber)
                if questionNumber < 6:
                    bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="""Huzzaaa... a splendid victory!
Forge ahead to your next quest -> /question
                 """,
                    )
                else:
                    bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="""Congratulations awesome person!
You have successfully completed the IEEE Aura Hunt!
Stay frosty, you'll be hearing from us...

In the mean time, follow our pages for more updates!
LinkedIn: https://www.linkedin.com/company/ieee-sb-cet
Instagram: https://www.instagram.com/ieeesbcet/
Facebook: https://m.facebook.com/IEEE.SB.CET/
                 """,
                    )
            else:
                bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Hmmm...that doesn't look right, try again!",
                )


def getProgress(update: Update, context: CallbackContext):
    questionNumber = db.getUserQuestion(str(update.effective_chat.id))
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""
        You are here:
{progress[questionNumber]}
        """,
    )


dispatcher.add_handler(CommandHandler("start", displayStartMessage))
dispatcher.add_handler(CommandHandler("rules", displayRules))
dispatcher.add_handler(CommandHandler("question", displayQuestion))
dispatcher.add_handler(CommandHandler("answer", getAnswer))
dispatcher.add_handler(CommandHandler("progress", getProgress))

updater.start_polling()

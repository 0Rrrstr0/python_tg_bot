import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    message_id = bot.send_message(chat_id, "Запускаю таймер!")
    bot.create_countdown(parse(text), notify_progress,
                         chat_id=chat_id, message_id=message_id, total=parse(text))
    bot.create_timer(parse(text), notify, chat_id=chat_id)


def notify_progress(secs_lef, message_id, chat_id, total):
    bot.update_message(chat_id, message_id, "Осталось {} сек \n".format(
        secs_lef) + render_progressbar(total, secs_lef))


def notify(chat_id):
    bot.send_message(chat_id, "Время вышло!")


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply)
    bot.run_bot()

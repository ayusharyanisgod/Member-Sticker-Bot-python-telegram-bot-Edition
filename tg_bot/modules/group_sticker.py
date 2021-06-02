
import html
from typing import Optional, List
import random
from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler, run_async
from telegram.utils.helpers import mention_markdown, mention_html, escape_markdown
import tg_bot.modules.sql.welcome_sql as sql
from tg_bot import dispatcher, OWNER_ID, LOGGER
from tg_bot.modules.helper_funcs.chat_status import user_admin, can_delete
from tg_bot.modules.helper_funcs.misc import build_keyboard, revert_buttons
from tg_bot.modules.helper_funcs.msg_types import get_welcome_type
from tg_bot.modules.helper_funcs.string_handling import markdown_parser, \
    escape_invalid_curly_brackets


def send(update, message, keyboard, backup_message):
    try:
        msg = update.effective_message.reply_text(message, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)
    except IndexError:
        msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                  "\nNote: the current message was "
                                                                  "invalid due to markdown issues. Could be "
                                                                  "due to the user's name."),
                                                  parse_mode=ParseMode.MARKDOWN)
    except KeyError:
        msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                  "\nNote: the current message is "
                                                                  "invalid due to an issue with some misplaced "
                                                                  "curly brackets. Please update"),
                                                  parse_mode=ParseMode.MARKDOWN)
    except BadRequest as excp:
        if excp.message == "Button_url_invalid":
            msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                      "\nNote: the current message has an invalid url "
                                                                      "in one of its buttons. Please update."),
                                                      parse_mode=ParseMode.MARKDOWN)
        elif excp.message == "Unsupported url protocol":
            msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                      "\nNote: the current message has buttons which "
                                                                      "use url protocols that are unsupported by "
                                                                      "telegram. Please update."),
                                                      parse_mode=ParseMode.MARKDOWN)
        elif excp.message == "Wrong url host":
            msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                      "\nNote: the current message has some bad urls. "
                                                                      "Please update."),
                                                      parse_mode=ParseMode.MARKDOWN)
            LOGGER.warning(message)
            LOGGER.warning(keyboard)
            LOGGER.exception("Could not parse! got invalid url host errors")
        else:
            msg = update.effective_message.reply_text(markdown_parser(backup_message +
                                                                      "\nNote: An error occured when sending the "
                                                                      "custom message. Please update."),
                                                      parse_mode=ParseMode.MARKDOWN)
            LOGGER.exception()

    return msg

@run_async
def new_member(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    join = update.effective_message.new_chat_members
    count = chat.get_members_count()
    if count is 3:
                update.effective_message.reply_text("We are 3 Now,")
    elif count is 5:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtAAFgsFYY1aKAxInpNJMYYn1V50si7AAC2QADMJFBRUJPOESwsw1jHwQ")
    elif count is 10:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtAWCwVhlXekFkrYJx3DfoqLuhnISnAALYAAMrDUlF2pt6MjsOHFkfBA")
    elif count is 25:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp0GCriGh4oGz56qW1wdMHUJULU-wxAAJ1AgACb8FkFDCUuHcEvpgrHwQ")
    elif count is 50:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp02CriHTL6W6VKEDkZ7SpDuBJ-hv\_AAJ2AgACb8FkFMQhQH7icivgHwQ")               
    elif count is 75:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp2WCrjLF-chH9sdbwfZKRweC9wDpdAAJ3AgACb8FkFNnvojLmMWChHwQ")
    elif count is 100:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp2mCrjLK9bjhBHxRKvY6mzC29zdX-AAJ4AgACb8FkFCHyjB1WKhwIHwQ")               
    elif count is 150:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp22CrjLMcLfLnSbQ3MCyJAAF3p5pMfQACeQIAAm\_BZBQtPpJQWxVDnB8E")
    elif count is 200:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp3GCrjLMSlZIUA135iaT2Be9Zhri4AAJ6AgACb8FkFDqPwakq2etKHwQ")               
    elif count is 250:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp6GCrjf9Ynb5ref88s\_gaH8jbUoofAAJ7AgACb8FkFCFLPuqC5veCHwQ")               
    elif count is 300:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp62Crjhl9OLuO0AQXOCD9KjI-jHKNAAJ8AgACb8FkFCmoLzif0k1eHwQ")               
    elif count is 350:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp7mCrjjfNsHWivLln\_yOc\_P8gcYT-AAJ9AgACb8FkFOItmI8tdunbHwQ")               
    elif count is 400:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp8WCrjlPskv0cI2bjkocefjYgtkA6AAJ-AgACb8FkFLEuZPK4e-XOHwQ")               
    elif count is 450:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp9GCrjyZ\_UJduUnF81DakBCh1buf4AAJ\_AgACb8FkFPJ2TY44h3N6HwQ")               
    elif count is 500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp92Crj0AwEaGbayhTtD-fk5YYax5jAAKAAgACb8FkFDdNlq54yRL6HwQ")               
    elif count is 550:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp-mCrj1qG-X0B5fH8p2pkCgAB4jyKwgACgQIAAm\_BZBSPptVG0Fq4JB8E")               
    elif count is 600:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp\_WCrj3PbLep6QljDXk5zvQ2DtzquAAKCAgACb8FkFM9xskyitVWxHwQ")               
    elif count is 650:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqAAFgq4-U-ZYwN9NjQ3\_pmUA2iP3BhAACgwIAAm\_BZBQvwCFfDwjlvB8E")               
    elif count is 700:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqA2CrkCvzVcHt1iWD3mdCzqHyBbtFAAKEAgACb8FkFHeWcxlF2xjEHwQ")               
    elif count is 750:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqBmCrkD9fNnHje\_UKcZ7\_qEg7WtLiAAKFAgACb8FkFND5m5zAauszHwQ")               
    elif count is 800:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqCWCrkFkkx9mTOclBopAR2WXTaqlpAAKGAgACb8FkFAZBHHiJozilHwQ")               
    elif count is 850:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqDGCrkHNLxO\_RXjVgoz4kILONpN7DAAKHAgACb8FkFFmrvvzk7QZRHwQ")               
    elif count is 900:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqEWCrkKOuTeR4zmIRAw7lHnT5MkXKAAKIAgACb8FkFFEX5yMmL9DLHwQ")               
    elif count is 950:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqFGCrkMDDMLWyMWzSIoagwJyYGyk0AAKJAgACb8FkFM3a7eUdwjVxHwQ")               
    elif count is 1000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqGWCrkOOa5UHFZXBSrWYfO7FyvOFSAAKKAgACb8FkFBAnB\_OSoszTHwQ")               
    elif count is 1500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqHGCrkP9q4ZMqL9Pnm23bt-rpn1wHAAKLAgACb8FkFF7f1TftpoS3HwQ")               
    elif count is 2000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqH2CrkS\_LgXE7bPqTyMjUA7NSzVJjAAKMAgACb8FkFBKXkZIBPS-LHwQ")               
    elif count is 2500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqIGCrkTDzdwHEHYkK9Sf1Iz0sGR9hAAKNAgACb8FkFH5oCr7\_PZAlHwQ")               
    elif count is 3000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqbWCsxolKsS4dhUJEQvzLe0aYRjXuAAKOAgACb8FkFDbFTrzyB8eFHwQ")               
    elif count is 3500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqbmCsxouolLXaoKk2C5rQaEUYE\_3JAAKPAgACb8FkFLFEIXI21CkuHwQ")               
    elif count is 4000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqc2Csxsk0N5DMwxE4fCkoas0PUORyAAKQAgACb8FkFEa482BW-SgdHwQ")               
    elif count is 4500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqdGCsxsl9fQcyqAABQh5u\_hPAT8ATbAACkQIAAm\_BZBQp7pS0Yn1KDx8E")               
    elif count is 5000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqeWCsxvF82KBahWUBK195WNX2aXVMAAKmAgACb8FkFAABmvRInkQq1B8E")               
    elif count is 5500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqfGCsxwakyu0e7oum67is2pDCakFMAAKnAgACb8FkFHy9dkRdqy85HwQ")               
    elif count is 6000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqf2CsxxtaTiVWIrqZBAxiwxtZck5VAAKSAgACb8FkFO-7G5rKq-OGHwQ")               
    elif count is 6500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqgGCsxx2qfiZ26XbyF9UWNg9XIQ81AAKTAgACb8FkFIyO8XGfp2-LHwQ")               
    elif count is 7000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqgWCsxx4PPDKEKpJO2IwfzKI-AqfEAAKUAgACb8FkFIxl1Y3Zh7DUHwQ")               
    elif count is 7500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqgmCsxx-q-vvKuy1PR0Ucsh2i\_b5qAAKWAgACb8FkFDJuVxkIH49nHwQ")               
    elif count is 8000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqi2Csx5N5gdJN5UKIpiOLkLP1z1YSAAKVAgACb8FkFFfJp2LBYY2THwQ")               
    elif count is 8500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqjGCsx5Sz4QbPsMzjbzDHw0V1S9ZQAAKXAgACb8FkFEuWh3xGJMEjHwQ")               
    elif count is 9000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqjWCsx5Tq6kroylCm0R5Ba0ZbiINiAAKYAgACb8FkFAOgHXkDWNLUHwQ") 
    elif count is 9500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKquWCsyZmf9gh234AU3Vd\_3ZsNpbpEAAKZAgACb8FkFAlC7No4ds65HwQ")                        
    elif count is 10000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqj2Csx5V4B2qeuDmZuo70Y9eDjoYZAAKaAgACb8FkFOc4tDz93va-HwQ")               
    elif count is 11000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqmGCsyCShxnqxBSHX2nDbRk4XaVu-AAKbAgACb8FkFO97WSB0bRjmHwQ")               
    elif count is 12000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqmWCsyHjlkn-BeuhsRrnmpmsEEquTAAKcAgACb8FkFBQzIWLKUlKpHwQ")               
    elif count is 13000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqmmCsyHnnjIWUG7nsx4k6rVmVjx7MAAKdAgACb8FkFIwB7ZXinCE2HwQ")               
    elif count is 14000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqm2CsyHq1O54DTM-skYGxZATx4lHRAAKeAgACb8FkFDToP3ZAv-\_LHwQ")               
    elif count is 15000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqnGCsyHuMKgckj1BsTg0QeWYtawogAAKfAgACb8FkFHDtQBuvq-0SHwQ")               
    elif count is 16000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqp2CsyOfi6BqA-TuLjEVcpi2ylnIUAAKgAgACb8FkFGS\_0OcY9eH\_HwQ")               
    elif count is 17000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqqGCsyOgz35NuLj2StVxuc1XvOyv3AAKhAgACb8FkFDAjY2BB3IqXHwQ")                  
    elif count is 18000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqqWCsyOiz\_jUHXzSdJLvUUv4UjIZEAAKiAgACb8FkFE8ckXdcKFUuHwQ")               
    elif count is 19000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqqmCsyOncts5liNFhL8E9ZhZZvSu8AAKjAgACb8FkFOGlqzutkPoMHwQ")               
    elif count is 20000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqq2CsyOlKkSUzc5NnWEkmIAwBYiicAAKkAgACb8FkFBwLYOllwLDXHwQ")               
    elif count is 25000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqrGCsyOp0ZcV8MoswUkzghb9ynVYDAAKlAgACb8FkFAqu5NwRTie3HwQ")               
    elif count is 30000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtBmCwVpB3YPGLBnawjP6\_-82RSVUKAAKiAQACatlIRQPM7zY14FASHwQ")
    elif count is 40000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtB2CwVpF--t6hLOziTVK4KiBkaiCaAAIEAQAC6wVARUgHHrCAlVfjHwQ")
    elif count is 50000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtCGCwVpKG3I2EFAITefrIgXRS7xfEAAK2AAOzK0BFZZ67Eai2hP0fBA")
    elif count is 60000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtCWCwVpI0syCabtZ8FG-XRrPvtkvfAAJ8AQACUKdARVgbGFYa4RKrHwQ")
    elif count is 70000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtCmCwVpNd6ujQJ1\_RPREjcOQfDnxfAAJTAQAC1shARadqwBisDaalHwQ")
    elif count is 80000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtC2CwVpTglVtjpbkFxfXXLFpVJ6ivAALoAANZ5UBFCmaz\_d8dsxsfBA")
    elif count is 90000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtDGCwVpQv1DcS4YJuLDhfpMithMdDAALKAAMoWkBFKiSKj9nmRrcfBA")
    elif count is 100000:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtDWCwVpUG8eI45egbzbDsMBUGxHzsAAIrAQACCg9JRQV03n3GU89-HwQ")
   # elif count is 110000:
   #             update.effective_message.reply_sticker("stickerid")
     



# more to cover 
# use
# elif count is {number}:
#                update.effective_message.reply_sticker("stickerid")               
   
# use json bot to return Sticker ID


NEW_MEM_HANDLER = MessageHandler(Filters.status_update.new_chat_members, new_member)
dispatcher.add_handler(NEW_MEM_HANDLER)

# © Notice
# Bughunter0 2021
# All Rights Reserved
# t.me/bughunter0
# github.com/bughunter0

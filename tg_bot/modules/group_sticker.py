
import html
from typing import Optional, List
import random
from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup
from telegram.error import BadRequest

# © Notice
# Bughunter0 2021
# All Rights Reserved
# t.me/bughunter0
# github.com/bughunter0

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
       
# © Notice
# Bughunter0 2021
# All Rights Reserved
# t.me/bughunter0
# github.com/bughunter0
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
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3VWDG5Gl0VyjbjSOK2pXo4e9WCjR6AAL1AgACufE4VgHHxPJeyWOKHwQ")
    elif count is 5:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3WGDG5IjDeVkt0p7vmHBndjzhsCMlAAKQAgACCoU4Vh4T1CeHhp9dHwQ")
    elif count is 7:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3W2DG5NyWz8Z5\_XEIvsIb8dgRX1gKAALdAgAC7f84ViojLrLihZXFHwQ")     
    elif count is 10:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKtAWCwVhlXekFkrYJx3DfoqLuhnISnAALYAAMrDUlF2pt6MjsOHFkfBA")
    elif count is 20:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3XmDG5bOvRccI6xgzCnTTDis51gp8AAIyAwACtjQ5Vl\_xGgHnFbS4HwQ")     
    elif count is 25:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp0GCriGh4oGz56qW1wdMHUJULU-wxAAJ1AgACb8FkFDCUuHcEvpgrHwQ")    
    elif count is 30:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3YWDG5clmpGlbeSNCkVa\_x9coebFYAALXAQACawABMVZAD68bdhsdLB8E")     
    elif count is 35:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3ZGDG5dkxr6MmiZ4nmFMBct0\_JQw0AALDAgACdhE4VlXq3LxwIYXVHwQ")      
    elif count is 40:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3Z2DG5hGpJLPU5cB56ZBmtp0-mP6SAAKkAgACQTU5VjaRqNv2TFeTHwQ")       
    elif count is 45:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3amDG5ioRybt4VyS8\_zdEb36lHTLTAAK8AwACCKoxVqTbpnMk\_MQTHwQ")      
    elif count is 50:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp02CriHTL6W6VKEDkZ7SpDuBJ-hv\_AAJ2AgACb8FkFMQhQH7icivgHwQ")   
    elif count is 55:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3bWDG55f0E6YcRklex5RCIIl6jaPEAAJSAwACI9U5VugjgalV5M1EHwQ")
    elif count is 60:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3cGDG57JHL-t1D7Z5fROsIp7bWffPAAJNAgACKrU4VuCu1cQtX77xHwQ")
    elif count is 65:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3c2DG585Y0-cOiHlMilsPe1rw4A02AAKjBAAC2DoxVo0AAfZxo3XDXh8E")
    elif count is 70:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3dmDG5-8UGVBE-1U8K2Fd1PiSE4VcAAJIAgACE1g5VsL7ptwX608LHwQ")                   
    elif count is 75:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp2WCrjLF-chH9sdbwfZKRweC9wDpdAAJ3AgACb8FkFNnvojLmMWChHwQ")
    elif count is 80:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3eWDG6AjR3gPHDTY527W5lO-drzbWAALzAgACe444Vurr0F\_5S6NsHwQ")
    elif count is 85:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3emDG6Ak8EItAJOtfaBhjCczHGEweAALYAgACzj0xVoeTUX9wbijPHwQ")
    elif count is 90:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3e2DG6AmEyC7V5s5YHP0YTk90QWW8AAJDBAACVQk5VkLLUBVbCmAFHwQ")
    elif count is 95:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3fGDG6ArVoqeEHwhZcFfCLa1h9uTxAAIqAwACij05VhffSZgbF5LwHwQ")
    elif count is 99:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3fWDG6AsQ9jxtHOvqxgUIh\_NABxRUAAK8AwACeFQ4VoQ3RqKdVqA-HwQ")        
    elif count is 100:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp2mCrjLK9bjhBHxRKvY6mzC29zdX-AAJ4AgACb8FkFCHyjB1WKhwIHwQ")    
    elif count is 110:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3omDHXm6lPGCX6qPMo7-oy7550OEGAAIQAwAC9Cg5VmTUQm6kaO9mHwQ")
    elif count is 120:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3o2DHXm8\_Q3m\_29qcuwofGwV9GrcaAAKRAwACnOo4VjyzYcbK44llHwQ")
    elif count is 130:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3pGDHXm-7qWIuq7FZ5WrH3MLx869XAAIYAwACSPtBVql7BPcv3fkmHwQ")
    elif count is 140:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3pWDHXnAVk84Cz0KDxFD6tZHQtpsaAAJ8AgACEjpBVti8pBOmQ-GhHwQ")                      
    elif count is 150:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp22CrjLMcLfLnSbQ3MCyJAAF3p5pMfQACeQIAAm\_BZBQtPpJQWxVDnB8E")
    elif count is 160:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3r2DHXukowkmRAs-rkmQMFnoe9-mSAAIDAwACf7k5VsRb3FPkL5P2HwQ")
    elif count is 170:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3sGDHXunX0VPsA4uk-aQN5wvKB9v3AAIqAwACVPs4VslBUME7PI2uHwQ")
    elif count is 180:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3sWDHXuo5o8e-wJWfqz9HJfoNcNVvAAIuBAACS0k5Vi96vtzMVBELHwQ")    
    elif count is 190:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3smDHXusrf8iu3yuUJztWs52\_abTQAAJTAgACkWRBVvyi4w2ai5amHwQ")
    elif count is 199:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3vmDHX1ChSrO71jdOImgdOo\_OFCgEAAL0AgACkHNAVstYQcfw-zCGHwQ")    
    elif count is 200:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp3GCrjLMSlZIUA135iaT2Be9Zhri4AAJ6AgACb8FkFDqPwakq2etKHwQ")                  
    elif count is 210:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3s2DHXu3B\_xflixxpi\_BQJxTTr7pcAAJjAwACIj1BVpnqAmoWfU\_jHwQ")
    elif count is 220:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3tGDHXu5kd3fglOxjOKsycITfkTenAAINBAACsHw5Vr0x9q43Ss91HwQ")
    elif count is 230:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3tWDHXu\_mOE5Krxn1EGU84hhzarLcAAKbAwACR2s4VsqqxggMWameHwQ")
    elif count is 240:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3x2DHX7kAAWj56Fsus9qc\_pt\_UfsoTwACnwMAAsIZOFaOSVTHBcqIwB8E")     
    elif count is 250:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp6GCrjf9Ynb5ref88s\_gaH8jbUoofAAJ7AgACb8FkFCFLPuqC5veCHwQ")               
    elif count is 260:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3yGDHX7pfD47z6DCfmV0Kzdk8PtI-AAKcAwAC7dE4VuygX7HUOu6bHwQ")
    elif count is 270:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3yWDHX7sUA-i7s0qdPza34ypYpj-KAAKDAwACUNJBVlTPzSt7cM5sHwQ")
    elif count is 280:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3ymDHX7wsbyMObZjNRXEqvbc0G9OoAAIRBgACuuw5VmobUicLKuznHwQ")
    elif count is 290:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK3y2DHX7wrnXyRQR-Fj8aRVTrhf\_n9AAKsAwAChXs4Vjo-0FoAAcO0Lx8E")
    elif count is 299:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK31mDHYEAHGPiM43vY\_fVWFQYnJ9K5AAIKBAACDEM5VghDQNfoEbcaHwQ")
    elif count is 300:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp62Crjhl9OLuO0AQXOCD9KjI-jHKNAAJ8AgACb8FkFCmoLzif0k1eHwQ")               
    elif count is 350:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp7mCrjjfNsHWivLln\_yOc\_P8gcYT-AAJ9AgACb8FkFOItmI8tdunbHwQ")               
    elif count is 399:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK32WDHYVPJzGsLKqk2hCVc4Fsp4akSAAIhAwACzNs4VgXakUcyAwE8HwQ")     
    elif count is 400:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp8WCrjlPskv0cI2bjkocefjYgtkA6AAJ-AgACb8FkFLEuZPK4e-XOHwQ")               
    elif count is 450:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp9GCrjyZ\_UJduUnF81DakBCh1buf4AAJ\_AgACb8FkFPJ2TY44h3N6HwQ")  
    elif count is 499:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK32mDHYVNEC\_iVwO8f7cbWVCGOFIQOAAKNAwAC7Ho4Vj1CImxC\_F9WHwQ")                 
    elif count is 500:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp92Crj0AwEaGbayhTtD-fk5YYax5jAAKAAgACb8FkFDdNlq54yRL6HwQ")               
    elif count is 550:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp-mCrj1qG-X0B5fH8p2pkCgAB4jyKwgACgQIAAm\_BZBSPptVG0Fq4JB8E")    
    elif count is 599:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK322DHYVSIMrpt\_WLtsYIuqHU9\_AkpAALjAgACdvZBVraEOkjVPA4eHwQ")                   
    elif count is 600:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKp\_WCrj3PbLep6QljDXk5zvQ2DtzquAAKCAgACb8FkFM9xskyitVWxHwQ")               
    elif count is 650:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqAAFgq4-U-ZYwN9NjQ3\_pmUA2iP3BhAACgwIAAm\_BZBQvwCFfDwjlvB8E") 
    elif count is 699:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK33GDHYVXd7bVpRw7jU5YbC1Zj7c59AAIaAwACeQABQFbXLEEhtE18XR8E")                      
    elif count is 700:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqA2CrkCvzVcHt1iWD3mdCzqHyBbtFAAKEAgACb8FkFHeWcxlF2xjEHwQ")               
    elif count is 750:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqBmCrkD9fNnHje\_UKcZ7\_qEg7WtLiAAKFAgACb8FkFND5m5zAauszHwQ")   
    elif count is 799:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK33WDHYVVT12Wwo5t3krimIUZXf7Z6AAItAwAC8tY5ViC3gwFBf5xuHwQ")                    
    elif count is 800:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqCWCrkFkkx9mTOclBopAR2WXTaqlpAAKGAgACb8FkFAZBHHiJozilHwQ")               
    elif count is 850:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqDGCrkHNLxO\_RXjVgoz4kILONpN7DAAKHAgACb8FkFFmrvvzk7QZRHwQ")  
    elif count is 899:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK33mDHYVaamo6peetHlafBtWlrTnswAAL7AgACEedAVrSwVT9Mrl6RHwQ")                      
    elif count is 900:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqEWCrkKOuTeR4zmIRAw7lHnT5MkXKAAKIAgACb8FkFFEX5yMmL9DLHwQ")               
    elif count is 950:
                update.effective_message.reply_sticker("CAACAgEAAxkBAAKqFGCrkMDDMLWyMWzSIoagwJyYGyk0AAKJAgACb8FkFM3a7eUdwjVxHwQ")   
    elif count is 999:
                update.effective_message.reply_sticker("CAACAgUAAxkBAAK332DHYVcYYvhZGSMUPqXkiUqSeE15AAKtAgAClAABOVaRUSMWFV2eTR8E")                     
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
     

# © Notice
# Bughunter0 2021
# All Rights Reserved
# t.me/bughunter0
# github.com/bughunter0



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

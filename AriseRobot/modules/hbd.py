import html
import random, re
import requests as r

from telegram import Update, ParseMode, TelegramError, MAX_MESSAGE_LENGTH
from telegram.ext import Filters, CallbackContext, CommandHandler, run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown

from AriseRobot.modules.helper_funcs.extraction import extract_user
from AriseRobot.modules.helper_funcs.filters import CustomFilters
from AriseRobot.modules.helper_funcs.alternate import typing_action
from AriseRobot import dispatcher, DRAGONS, DEMONS, LOGGER
from AriseRobot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler

import AriseRobot.modules.helper_funcs.fun_strings as fun

'''
@run_async
@typing_action
def goodnight(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"Good Night! {escape_markdown(first_name)}" 
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)

@run_async
def hbd(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = random.choice(fun.HBD)
    update.effective_message.reply_text(chosen_option.format(firstname))
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)'''
    
@run_async
@typing_action
def hbd(update, context):
    args = context.args
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(
            msg.from_user.first_name, msg.from_user.id
        )

    user_id = extract_user(update.effective_message, args)
    if user_id:
        bday_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if bday_user.username:
            user2 = "@" + escape_markdown(bday_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(
                bday_user.first_name, bday_user.id
            )

    # if no target found, bot targets the sender
    else:
        user1 = "Awwh! [{}](tg://user?id={})".format(
            context.bot.first_name, context.bot.id
        )
        user2 = curr_user

    temp = random.choice(fun.HBD_TEMPLATES)
    hbd = random.choice(fun.HBD)

    repl = temp.format(user1=user1, user2=user2, hbd=hbd)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)
    
    
    
    
    HBD_HANDLER = DisableAbleCommandHandler("birthday", hbd)
    
    
    dispatcher.add_handler(HBD_HANDLER)

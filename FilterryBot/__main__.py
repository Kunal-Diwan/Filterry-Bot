import os
import datetime
import importlib
import re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop, Dispatcher
from telegram.utils.helpers import escape_markdown

from FilterryBot import dispatcher, updater, TOKEN, WEBHOOK, SUDO_USERS, OWNER_ID, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL
# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from FilterryBot.modules import ALL_MODULES
from FilterryBot.modules.helper_funcs.chat_status import is_user_admin
from FilterryBot.modules.helper_funcs.misc import paginate_modules
from FilterryBot.modules.translations.strings import tld, tld_help, tld_start
from FilterryBot.modules.connection import connected

SOURCE_STRING = """Oh you want my source !

Check Below 👇

⚙️ Source ⚙️ - [Click Here](https://github.com/Kunal-Diwan/Filterry-Bot) ."""

FILTERRY_HOME_TEXT = """
*All Setup done ✔️* \n\nUse /help to Know all modules and features \n
`All commands can be used with / ? or !`
"""

FILTERRY_HOWSETUP_TEXT = """
*Excellent!* \n\nAs you have added me to your group now you can easily set filters . If you don't know how to set filter click on *Setup* button .
"""
FILTERRY_SETUP_TEXT = """
*How to set Filters ?* \n
❍ Adding Single Reply Filter ⬇️
 
`/filter <keyword> <reply message>` \n
❍ Adding Multi Reply Filter ⬇️

`/filter "filtername"
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3` \n\n If you don't understand you can watch video tutorial by clicking *💾 Example Video 💾* .
"""
Filterrytut_VID = "https://telegra.ph/file/b8260e300bdc998e9c3db.mp4"

videobuttons = [[InlineKeyboardButton(text="✅ Done ✅",
                                  callback_data="tutmanu_home")]]


IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []

CHAT_SETTINGS = {}
USER_SETTINGS = {}

GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("FilterryBot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    #Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


#Do NOT async this!
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(chat_id, 0, HELPABLE, "help"))
    dispatcher.bot.send_message(chat_id=chat_id,
                                text=text,
                                parse_mode=ParseMode.MARKDOWN,
                                reply_markup=keyboard)


@run_async
def test(bot: Bot, update: Update):
    #pprint(eval(str(update)))
    #update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


@run_async
def start(bot: Bot, update: Update, args: List[str]):
    LOGGER.info("Start")
    chat = update.effective_chat  # type: Optional[Chat]
    #query = update.callback_query #Unused variable
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, tld(chat.id, "send-help").format(
                     dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(
                         chat.id, "\nAll commands can either be used with `/` or `!`.\n"
                             )))

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, update, user=False)
                else:
                    send_settings(match.group(1), update.effective_user.id, update, user=True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

            elif args[0].lower() == "controlpanel":
                control_panel(bot, update)
        else:
            send_start(bot, update)
    else:
        update.effective_message.reply_text("I'm alive")

def send_start(bot, update):
    chat = update.effective_chat
    # Try to remove old message
    try:
        query = update.callback_query
        query.message.delete()
    except Exception:
        pass

    # chat = update.effective_chat and unused variable
    text = tld(chat.id, 'main_start_pm')

    buttons = [
    [
        InlineKeyboardButton(
            text="➕️ Add Filterry to chat!  ➕️", url="t.me/FilterryBot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ℹ️ About ℹ️", callback_data="filterry_"),
        InlineKeyboardButton(text="⚙️ help ⚙️", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="🎙️ Support 🎙️", url="https://t.me/DevelopedBotz"),
        InlineKeyboardButton(text="🏳️‍🌈 Language 🏳️‍🌈", callback_data="set_lang_"),
    ],
    [
        InlineKeyboardButton(
            text="🎥 Configuration Tutorial 🎥", callback_data="tutmanu_"
        ),
    ],
]

    update.effective_message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

def se_start(bot, update):
    # Try to remove old message
    try:
        query = update.callback_query
        query.message.delete()
    except BaseException:
        pass

    chat = update.effective_chat  # type: Optional[Chat]
    first_name = update.effective_user.first_name
    text = tld(chat.id, 'main_start_pm')
    keyboard = [[InlineKeyboardButton(text="➕ Add me ➕",url="t.me/FilterryBot?startgroup=true"),InlineKeyboardButton(text="⚙️ Help ⚙️",callback_data="help_back")]]
    keyboard += [[InlineKeyboardButton(text="🔔 Channel 🔔", url="t.me/DevelopedBots"),InlineKeyboardButton(text="💬 Group 💬",url="t.me/DevelopedBotz")]]
    keyboard += [[InlineKeyboardButton(text="🏳️‍🌈 Language 🏳️‍🌈", callback_data="set_lang_"),InlineKeyboardButton(text="📱Tutorial📱",callback_data="tutmanu_")]]

    update.effective_message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN,
        timeout=60,
        disable_web_page_preview=False,
    )


def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "An exception was raised while handling an update\n"
        "<pre>update = {}</pre>\n\n"
        "<pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        LOGGER.warning("NO NONO1")
        LOGGER.warning(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        LOGGER.warning("NO NONO2")
        LOGGER.warning("BadRequest caught")
        LOGGER.warning(error)

        # handle malformed requests - read more below!
    except TimedOut:
        LOGGER.warning("NO NONO3")
        # handle slow connection problems
    except NetworkError:
        LOGGER.warning("NO NONO4")
        # handle other connection problems
    except ChatMigrated as err:
        LOGGER.warning("NO NONO5")
        LOGGER.warning(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        LOGGER.warning(error)
        # handle all other telegram related errors


@run_async
def help_button(bot: Bot, update: Update):
    query = update.callback_query
    chat = update.effective_chat  # type: Optional[Chat]
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    try:
        if mod_match:
            module = mod_match.group(1)
            mod_name = tld(chat.id, HELPABLE[module].__mod_name__)
            help_txt = tld_help(chat.id, HELPABLE[module].__mod_name__)

            if help_txt == False:
                help_txt = HELPABLE[module].__help__

            text = tld(chat.id, "*｢ Help for {} module 」*:\n{}").format(mod_name, help_txt)
            query.message.reply_text(text=text,
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton(text=tld(chat.id, "Back"), callback_data="help_back")]]))

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.reply_text(tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(chat.id, "\nAll commands can either be used with `/` or `!`.\n")),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(chat.id, curr_page - 1, HELPABLE, "help")))

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.reply_text(tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(chat.id, "\nAll commands can either be used with `/` or `!`.\n")),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(chat.id, next_page + 1, HELPABLE, "help")))

        elif back_match:
            query.message.reply_text(text=tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(chat.id, "\nAll commands can either be used with `/` or `!`.\n")),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(chat.id, 0, HELPABLE, "help")))

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.reply_text(tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(chat.id, "\nAll commands can either be used with `/` or `!`.\n")),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(chat.id, next_page + 1, HELPABLE, "help")))

        elif back_match:
            query.message.reply_text(text=tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(chat.id, "\nAll commands can either be used with `/` or `!`.\n")),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(chat.id, 0, HELPABLE, "help")))



        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message == "Message is not modified":
            pass
        elif excp.message == "Query_id_invalid":
            pass
        elif excp.message == "Message can't be deleted":
            pass
        else:
            LOGGER.exception("Exception in help buttons. %s", str(query.data))


@run_async
def filterry_about_callback(bot: Bot, update: Update):
    query = update.callback_query
    if query.data == "filterry_":
        query.message.edit_text(
            text="""ℹ️ My name is *Filterry* , Here is my details below 👇 \n
🤖 My Name : *Filterry* \n
👨‍💻 Developer : @Kunaldiwan \n
💻 Server : [Heroku](https://heroku.com) \n
📢 Channel  : @DevelopedBots \n
🔊 Support : @DevelopedBotz """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back 🔙", callback_data="bot_start")
                 ]
                ]
            ),
        )
    elif query.data == "filterry_aback":
        query.message.edit_text(
                text,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )


@run_async
def Filterry_tut_callback(bot: Bot, update: Update):
    query = update.callback_query
    if query.data == "tutmanu_":
        query.message.edit_text(
            text=f"*Welcome to the Filterry configuration tutorial.* "
            f"\n\n👇 The first thing to do is to *add Filterry to your group*! For doing that, press the under button and select your group, then press *Done* to continue the tutorial. 👇",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="➕️ Add Filterry to chat!  ➕️", url="t.me/FilterryBot?startgroup=true"
                        )
                    ],
                    [InlineKeyboardButton(text="✅ Done ✅", callback_data="tutmanu_howto")],
                ]
            ),
        )
    elif query.data == "tutmanu_howto":
        query.message.edit_text(
            text=f"* Ok, well done! *"
            f"\nNow for let me work correctly, you need to make me *Admin of your Group*! \n"
            f"\nTo do that, follow this easy steps:\n"
            f"▫️ Go to your group \n▫️ Press the Group's name \n▫️ Press Modify \n▫️ Press on Administrator \n▫️ Press Add Administrator \n▫️ Press the Magnifying Glass \n▫️ Search @FilterryBot \n▫️ Confirm"
            f"",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="✅ Continue ✅", callback_data="tutmanu_howfilter")]]
            ),
        )
    elif query.data == "tutmanu_howfilter":
        update.effective_message.reply_text(
            FILTERRY_HOWSETUP_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="⚒️ Setup 🛠️", callback_data="tutmanu_setup")]]
            ),
        )
    elif query.data == "tutmanu_setup":
        update.effective_message.reply_text(
            FILTERRY_SETUP_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="💾 Example Video 💾", callback_data="tutmanu_video"
                        ),
                    ],
                    [InlineKeyboardButton(text="✅ Done ✅", callback_data="tutmanu_home")],
                ]
            ),
        )
    elif query.data == "tutmanu_home":
        update.effective_message.reply_text(
            FILTERRY_HOME_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🏡 Home 🏡", callback_data="bot_start")]]
            ),
        )
    elif query.data == "tutmanu_video":
        update.effective_message.reply_animation(
            Filterrytut_VID,
            reply_markup=InlineKeyboardMarkup(videobuttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
        )


@run_async
def get_help(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:

        update.effective_message.reply_text("Contact me in PM to get the list of possible commands.",
                                            reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="Help",
                                                                       url="t.me/{}?start=help".format(
                                                                           bot.username))]]))
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        mod_name = tld(chat.id, HELPABLE[module].__mod_name__)
        help_txt = tld_help(chat.id, HELPABLE[module].__mod_name__)

        if help_txt == False:
            help_txt = HELPABLE[module].__help__

        text = tld(chat.id, "Here is the help for the *{}* module:\n{}").format(mod_name, help_txt)
        send_help(chat.id, text, InlineKeyboardMarkup([[InlineKeyboardButton(text=tld(chat.id, "Back"), callback_data="help_back")]]))

    else:
        send_help(chat.id, tld(chat.id, "send-help").format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else tld(
            chat.id, "\nAll commands can either be used with `/` or `!`.\n"
                )))

def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id)) for mod in USER_SETTINGS.values())
            dispatcher.bot.send_message(user_id, "These are your current settings:" + "\n\n" + settings,
                                        parse_mode=ParseMode.MARKDOWN)

        else:
            dispatcher.bot.send_message(user_id, "Seems like there aren't any user specific settings available :'(",
                                        parse_mode=ParseMode.MARKDOWN)

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(user_id,
                                        text="Which module would you like to check {}'s settings for?".format(
                                            chat_name),
                                        reply_markup=InlineKeyboardMarkup(
                                            paginate_modules(user_id, 0, CHAT_SETTINGS, "stngs", chat=chat_id)))
        else:
            dispatcher.bot.send_message(user_id, "Seems like there aren't any chat settings available :'(\nSend this "
                                                 "in a group chat you're admin in to find its current settings!",
                                        parse_mode=ParseMode.MARKDOWN)


@run_async
def settings_button(bot: Bot, update: Update):
    query = update.callback_query
    user = update.effective_user
    chatP = update.effective_chat  # type: Optional[Chat]
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(escape_markdown(chat.title),
                                                                                     CHAT_SETTINGS[
                                                                                         module].__mod_name__) + \
                   CHAT_SETTINGS[module].__chat_settings__(bot, update, chat, chatP, user)
            query.message.reply_text(text=text,
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton(text="Back",
                                                                callback_data="stngs_back({})".format(chat_id))]]))

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(tld(user.id, "send-group-settings").format(chat.title),
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(curr_page - 1, CHAT_SETTINGS, "stngs",
                                                          chat=chat_id)))

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(tld(user.id, "send-group-settings").format(chat.title),
                                     reply_markup=InlineKeyboardMarkup(
                                         paginate_modules(next_page + 1, CHAT_SETTINGS, "stngs",
                                                          chat=chat_id)))

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text(text=tld(user.id, "send-group-settings").format(escape_markdown(chat.title)),
                                     parse_mode=ParseMode.MARKDOWN,
                                     reply_markup=InlineKeyboardMarkup(paginate_modules(user.id, 0, CHAT_SETTINGS, "stngs",
                                                                                        chat=chat_id)))

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message == "Message is not modified":
            pass
        elif excp.message == "Query_id_invalid":
            pass
        elif excp.message == "Message can't be deleted":
            pass
        else:
            LOGGER.exception("Exception in settings buttons. %s", str(query.data))


@run_async
def get_settings(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]
    args = msg.text.split(None, 1)

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "Click here to get this chat's settings, as well as yours."
            msg.reply_text(text,
                           reply_markup=InlineKeyboardMarkup(
                               [[InlineKeyboardButton(text="Settings",
                                                      url="t.me/{}?start=stngs_{}".format(
                                                          bot.username, chat.id))]]))
        else:
            text = "Click here to check your settings."

    else:
        send_settings(chat.id, user.id, True)



@run_async
def source(bot: Bot, update: Update):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]

    if chat.type == "private":
        update.effective_message.reply_text(
            SOURCE_STRING, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )

    else:
        try:
            bot.send_message(
                user.id,
                SOURCE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )

            update.effective_message.reply_text(
                "I have PM you about my source!"
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get source information."
            )


def migrate_chats(bot: Bot, update: Update):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():
    test_handler = CommandHandler("test", test)
    start_handler = CommandHandler("start", start, pass_args=True)

    help_handler = CommandHandler("help", get_help)
    help_callback_handler = CallbackQueryHandler(help_button, pattern=r"help_.*")
    start_callback_handler = CallbackQueryHandler(
        se_start, pattern=r"bot_start")
    dispatcher.add_handler(start_callback_handler)

    settings_handler = CommandHandler("settings", get_settings)
    settings_callback_handler = CallbackQueryHandler(settings_button, pattern=r"stngs_")

    about_callback_handler = CallbackQueryHandler(filterry_about_callback, pattern=r"filterry_")
    tut_callback_handler = CallbackQueryHandler(
        Filterry_tut_callback, pattern=r"tutmanu_"
    )

    source_handler = CommandHandler("source", source)
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

    # dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(tut_callback_handler)
    dispatcher.add_handler(about_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(source_handler)

    dispatcher.add_error_handler(error_callback)

    # add antiflood processor
    Dispatcher.process_update = process_update

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN,
                                    certificate=open(CERT_PATH, 'rb'))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4)

    updater.idle()

CHATS_CNT = {}
CHATS_TIME = {}


def process_update(self, update):
    # An error happened while polling
    if isinstance(update, TelegramError):
        try:
            self.dispatch_error(None, update)
        except Exception:
            self.logger.exception('An uncaught error was raised while handling the error')
        return

    now = datetime.datetime.utcnow()
    cnt = CHATS_CNT.get(update.effective_chat, 0)

    t = CHATS_TIME.get(update.effective_chat.id, datetime.datetime(1970, 1, 1))
    if t and now > t + datetime.timedelta(0, 1):
        CHATS_TIME[update.effective_chat.id] = now
        cnt = 0
    else:
        cnt += 1

    if cnt > 10:
        return

    CHATS_CNT[update.effective_chat.id] = cnt
    for group in self.groups:
        try:
            for handler in (x for x in self.handlers[group] if x.check_update(update)):
                handler.handle_update(update, self)
                break

        # Stop processing with any other handler.
        except DispatcherHandlerStop:
            self.logger.debug('Stopping further handlers due to DispatcherHandlerStop')
            break

        # Dispatch any error.
        except TelegramError as te:
            self.logger.warning('A TelegramError was raised while processing the Update')

            try:
                self.dispatch_error(update, te)
            except DispatcherHandlerStop:
                self.logger.debug('Error handler stopped further handlers')
                break
            except Exception:
                self.logger.exception('An uncaught error was raised while handling the error')

        # Errors should not stop the thread.
        except Exception:
            self.logger.exception('An uncaught error was raised while processing the update')


if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    LOGGER.info("Successfully loaded")
    main()

#(©)Codexbotz
#Recoded By @Its_Tartaglia_Childe

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ɢᴏᴅ : <a href='https://t.me/Jas_Mehra'>Jas Mehra</a>\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ 1 : <a href='https://t.me/Fantastic_Animes'>ᴀɴɪᴍᴀᴛɪᴏɴ ʜᴜʙ</a>\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ 2 : <a href='https://t.me/Ongoing_Phoenix_Anime'>ᴀɴɪᴍᴀᴛɪᴏɴ ʜᴜʙ</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"Hᴀɪ {user.mention}♡゙,\n\n◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ.\n◈ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇs, Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟs, Cᴏɴᴠᴇʀᴛ Bᴇᴛᴡᴇᴇɴ Vɪᴅᴇᴏ Aɴᴅ Fɪʟᴇ, Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟs Aɴᴅ Cᴀᴘᴛɪᴏɴs.\n\n• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @Tonystark_botz"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('⚡ Updates', url='https://t.me/Tonystark_botz'),
        InlineKeyboardButton('⚡ Support', url='https://t.me/MovieTimesXDisc')
        ],[
        InlineKeyboardButton('✨ About', callback_data='about'),
        InlineKeyboardButton('⚙️ Help', callback_data='help')
        ],[
        InlineKeyboardButton(" Join Our Movie Channel !", url='https://t.me/MovieTimes_TV')
        ],[
        InlineKeyboardButton("❤️ Aᴠᴇɴɢᴇʀs Aʟʟɪᴀɴᴄᴇ™ ❤️", url='https://t.me/Avengers_Alliance')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""Hᴀɪ {user.mention}♡゙,\n\n◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ.\n◈ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇs, Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟs, Cᴏɴᴠᴇʀᴛ Bᴇᴛᴡᴇᴇɴ Vɪᴅᴇᴏ Aɴᴅ Fɪʟᴇ, Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟs Aɴᴅ Cᴀᴘᴛɪᴏɴs.\n\n• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @Tonystark_botz""",
            reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton('⚡ Updates', url='https://t.me/Tonystark_botz'),
        InlineKeyboardButton('⚡ Support', url='https://t.me/MovieTimesXDisc')
        ],[
        InlineKeyboardButton('✨ About', callback_data='about'),
        InlineKeyboardButton('⚙️ Help', callback_data='help')
        ],[
        InlineKeyboardButton(" Join Our Movie Channel !", url='https://t.me/MovieTimes_TV')
        ],[
        InlineKeyboardButton("❤️ Aᴠᴇɴɢᴇʀs Aʟʟɪᴀɴᴄᴇ™ ❤️", url='https://t.me/Avengers_Alliance')
        ]
        ]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/MovieTimes_TV")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/MovieTimes_TV")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/MovieTimes_TV")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()






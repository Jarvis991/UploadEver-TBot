#Copyright 2022-present, Author: 5MysterySD

from time import time
from config import BOT_UPTIME
from bot.core.display import convertTime
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    ''' Start Message of the Bot !!'''

    await m.reply_photo(photo='https://te.legra.ph/file/fff361f8f1019fa5162f9.jpg',
        caption='''<b>🔰 Hello, I am UploadEver.in Uploader and Multi-Tasking Bot! 🔰</b>

I can Do Many things, Check Out My Help Section !!

<b>💯 Bot Created By ♥️ @MysterySD ♥️
💥 Powered By ⚡️ UploadEver ⚡️</b>
<i>If you face any kind of Problem/Error or Feature Request, Message to @MysterySD</i>''',
        quote=True,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📃 About", callback_data="upabout"),
            InlineKeyboardButton("📮 Help", callback_data="uphelp"),
            InlineKeyboardButton("📊 Stats", callback_data="upstats")],
            [InlineKeyboardButton("👥 Group", url="https://t.me/uploadever"),
            InlineKeyboardButton("📇 Website", url="https://uploadever.in")]
        ])
    )

@Client.on_callback_query(filters.regex('^up'))
async def cb_handlers(c: Client, cb: CallbackQuery):
    ''' CallbackQuery Handlers '''

    
    if cb.data == "upabout":
        await cb.message.edit(text="Hii",
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "uphelp":
        await cb.message.edit(text='''Main  Features :
        
☃️  <i>Here you can Upload Files via Forwarding Telegram Files/ Sending Telegram File/Send UploadEver Links to this Bot!</i>

<b>Bot Commands :</b>

<i>/start For Start Bot
/login To Login
/logout To Logout from here
/stats to get account stats/earning/space/etc information
/bulklinks to check supported links that can be converted to uploadever

Send Any File or media to directly Upload !!</i>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "upstats":
        await cb.message.edit(text=f'''Bot Stats:
        
Bot Uptime : {convertTime((time() - BOT_UPTIME)*1000)}
Today Stats:
Files Uploaded:

Active Tasks :
Total Files Uploaded :
...
''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "uphome":
        await cb.message.edit(text='''<b>🔰 Hello, I am UploadEver.in Uploader and Multi-Tasking Bot! 🔰</b>

I can Do Many things, Check Out My Help Section !!

<b>💯 Bot Created By ♥️ @MysterySD ♥️
💥 Powered By ⚡️ UploadEver ⚡️</b>
<i>If you face any kind of Problem/Error or Feature Request, Message to @MysterySD</i>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📃 About", callback_data="upabout"),
                InlineKeyboardButton("📮 Help", callback_data="uphelp"),
                InlineKeyboardButton("📊 Stats", callback_data="upstats")],
                [InlineKeyboardButton("👥 Group", url="https://t.me/uploadever"),
                InlineKeyboardButton("📇 Website", url="https://uploadever.in")]
            ])
        )
    


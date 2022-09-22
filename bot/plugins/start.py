#Copyright 2022-present, Author: 5MysterySD

from time import time
from platform import python_version
from config import BOT_UPTIME
from bot.core.display import convertTime
from bot.core.db.db_func import _addNewUserToDB
from bot.client import Client
from pyrogram import filters, enums, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    ''' Start Message of the Bot !!'''
    await _addNewUserToDB(c, m)
    await m.reply_photo(photo='https://te.legra.ph/file/fff361f8f1019fa5162f9.jpg',
        caption='''🔰 <i>Hello, I am UploadEver.in Uploader and Multi-Tasking Bot 🔰</i>

🏷<b><i> I have Many Amazing Features, Check Out My Help Section to Know them All !!</i></b>

<i>💯 Bot Created By ♥️ @MysterySD ♥️
💥 Powered By ⚡️ UploadEver ⚡️</i>''',
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
        await cb.message.edit(text=f'''🔭 <b>About Me :</b>

<i>• My Name : <a href="https://t.me/{(await c.get_me()).username}">{(await c.get_me()).first_name}</a>
• Version : V1.0.0
• Framework : <a href="https://pyrogram.org/">Pyrogram V{__version__}</a>
• Language : <a href="https://www.python.org/">{python_version()}</a>
• Database : <a href="http://mongodb.com/">MongoDB 5.0</a>
• Developer : @MysterySD</i>

📝 <b>Note :</b> <u>If you face Any Kind of Issue/Error or Feature Request, Message to @MysterySD</u>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "uphelp":
        await cb.message.edit(text='''🚦<b>Main Features</b>🚦
        
⛵️ <i>Upload Files via Forwarding or Sending Telegram File, Media, Audio and Get UploadEver Links
⛵️Send UploadEver Links to this Bot
⛵️Send Any Message Containing UploadEver.in Links, Auto Clone to your Account 
⛵️ Check your Account Stats</i>

🚧 <code>More Features Soon  ...</code>

🏖 <b><i>Available Bot Commands :<i></b>

<i>/start To Check Bot Existence 
/login To Login to your Account
/logout To Logout from this Bot
/stats to get Account stats/earning/space/etc Information
/bulklinks To Convert UploadEver Links to your Accounts UploadEver Links, Without Any Change in Formatted Text of the Message</i>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "upstats":
        await cb.message.edit(text=f'''🤖 <b><u>Bot Stats:</u></b>

<b>🎛 Active Downloads : 
⏱ Bot Uptime : {convertTime((time() - BOT_UPTIME)*1000)}</b>

📃 <b>Today Stats:</b>

<i>• Active Users :
• Files Uploaded :
• Links Cloned :
• Bulk Link Cloned :</i>

📊 <b>Overall Stats:</b>

<i>• Total Users :
• Total Files Uploaded :
• Total Links Cloned :
• Total Bulk Link Cloned :</i>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back", callback_data="uphome")]
                ])
        )
    elif cb.data == "uphome":
        await cb.message.edit(text='''🔰 <i>Hello, I am UploadEver.in Uploader and Multi-Tasking Bot 🔰</i>

🏷<b><i> I have Many Amazing Features, Check Out My Help Section to Know them All !!</i></b>

<i>💯 Bot Created By ♥️ @MysterySD ♥️
💥 Powered By ⚡️ UploadEver ⚡️</i>''',
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📃 About", callback_data="upabout"),
                InlineKeyboardButton("📮 Help", callback_data="uphelp"),
                InlineKeyboardButton("📊 Stats", callback_data="upstats")],
                [InlineKeyboardButton("👥 Group", url="https://t.me/uploadever"),
                InlineKeyboardButton("📇 Website", url="https://uploadever.in")]
            ])
        )
    


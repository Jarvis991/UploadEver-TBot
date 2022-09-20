#Copyright 2022-present, Author: 5MysterySD

from pathlib import Path
from time import time
from subprocess import check_output
from asyncio import sleep as asleep
from requests import get as rget
from config import LOGGER, USERS_API, Config
from bot.client import Client
from bot.core.display import convertBytes
from bot.core.progress import progress_for_pyrogram
from pyrogram import filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("upload") & filters.private)
async def upload_file_handler(c: Client, m: Message):
    ''' Upload Telegram Files Directly to the UploadEver Server upto 4GB (TG Limit) 

    :param media: Telegram File you want to Upload to UploadEver Server.
    :param token: Your Own API token of UploadEver.in
    :param sess_id: Session ID for Remote Upload 
    :param server_url: The Server which will take the Request to Upload the Media

    OUTPUT: (Step 1)
    {
      "status": 200,
      "sess_id": "3rexxxxxxxxxx9",
      "result": "http://s1.fileserverdomain.com/cgi-bin/upload.cgi",
      "msg": "OK",
      "server_time": "2021-10-22 05:13:21"
    }
    OUTPUT: (Step 2)
    [
      {
        "file_code": "bxxxxxxxka",
        "file_status": "OK"
      }
    ]
    '''

    Token = USERS_API.get(m.chat.id, None)
    if Token is None: 
        await m.reply_text("<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>",  quote=True, parse_mode=enums.ParseMode.HTML)
        return
    rpy_media = m.reply_to_message
    if not rpy_media:
        await m.reply_text("📤 <i>Reply to a Telegram File to Start Uploading to UploadEver Server !!</i>", quote=True, parse_mode=enums.ParseMode.HTML)
        return

    downMSG = await m.reply_text("🔍 <b>Finding a UploadEver Server to Start Uploading ...</b>", quote=True, parse_mode=enums.ParseMode.HTML)
    resp = rget(f"https://uploadever.in/api/upload/server?key={Token}")
    jdata = resp.json()
    if jdata['status'] == 200:
        SESS_ID = jdata['sess_id']
        UP_SER_URL = jdata['result']
    else:
        await m.reply_text(jdata['msg'])
        return
    await asleep(1.5)

    await downMSG.edit(f"🔍 <b>Found a UploadEver Server for Taking Requests !!</b>\n\n 📤 <b>Starting Media Download...</b>", parse_mode=enums.ParseMode.HTML)
    media = [rpy_media.document, rpy_media.video, rpy_media.audio]
    file = [md for md in media if md is not None][0]
    file_name = file.file_name
    mime_type = file.mime_type
    file_size = file.file_size
    __fileName = f"{Path('./').resolve()}/{Config.DIRECTORY}"
    try:
        __time = time()
        __downLocation = await c.download_media(message=rpy_media, 
            file_name=__fileName,
            progress=progress_for_pyrogram,
            progress_args=(f"🚄 Fɪʟᴇɴᴀᴍᴇ: {file_name}",
                downMSG,
                __time
            )
        )
    except Exception as err:
        await downMSG.edit(f"⛔️ Download Error : {err}")
        LOGGER.error(err)
        return
    LOGGER.info(f"[TG Upload] User: {m.chat.id} File Location: {__downLocation}")
    await downMSG.edit(f"🔍 <b>Found a UploadEver Server for Taking Requests !!</b>\n\n 📤 <b>Media Downloaded, Uploading...</b>", parse_mode=enums.ParseMode.HTML)
    
    UpData = check_output(f"curl -F 'sess_id={SESS_ID}' -F 'file_0=@{__downLocation}' {UP_SER_URL}", shell=True).decode('utf-8')
    await downMSG.delete()
    filecode = UpData.strip(']}{[').replace(":", ",").replace('"', '').split(',')
    URL = f"https://uploadever.in/{filecode[1]}"
    await m.reply_text(text=f'''📈 <b>Upload Completed</b> 📉

• 📨 <b>FileName :</b> <code>{file_name}</code>

• 📋 <b>Mime-Type :</b> <code>{mime_type}</code>
• 📦 <b>Size :</b> <code>{convertBytes(file_size)}</code>

• 🔗 <b>URL :</b> <code>{URL}</code>
''',
        quote=True,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📎 UploadEver URL", url=URL)]
        ])
     )

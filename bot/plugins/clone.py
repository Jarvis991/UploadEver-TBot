#Copyright 2022-present, Author: 5MysterySD

from os import remove as orem
from re import findall
from pathlib import Path
from requests import get as rget
from config import LOGGER, USERS_API, Config
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message

@Client.on_message(filters.regex(r'^https?://uploadever\.in\S+') & filters.private)
async def _cloneUploadEverLinks(c: Client, m: Message):
    ''' Clone URL from UploadEver.in Server API:

    :param url: The UploadEver.in URL you want to Clone
    :param token: Your Own API token of UploadEver.in

    OUTPUT:
    {
      "status": 200,
      "result": {
        "url": "https://uploadever.in/r9o25tsq86ru",
        "filecode": "r9o25tsq86ru"
      },
      "msg": "OK",
      "server_time": "2022-03-09 10:49:48"
    }
    '''

    Link = (m.text).strip()
    filecode = (Link.split("/"))[-1]
    Token = USERS_API.get(m.chat.id, None)
    if Token is None: text_ = "<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>"
    else:
        resp = rget(f"https://uploadever.in/api/file/clone?file_code={filecode}&key={Token}")
        jdata = resp.json()
        if jdata['status'] == 200:
            text_ = f"<b>🔗 Generated Cloned URL:</b> <code>{jdata['result']['url']}</code>"
        else: text_ = jdata['msg']

    await m.reply_text(text=text_, parse_mode=enums.ParseMode.HTML, quote=True)


@Client.on_message(filters.command("bulklinks") & filters.private)
async def _bulkCloneLinks(c: Client, m: Message):
    ''' Bulk Clone URL from UploadEver.in Server API:

    :param url: The UploadEver.in URL you want to Clone
    :param token: Your Own API token of UploadEver.in
    '''

    rpyMSG = m.reply_to_message
    if not rpyMSG:
        await m.reply_text(text="🖇 <b><i>Give a UploadEver.in Link to Clone or Reply to Any Message Containing UploadEver.in Links !!</i></b>", parse_mode=enums.ParseMode.HTML, quote=True)
        return
    if rpyMSG.photo:
        _rpyPhoto = rpyMSG.download(file_name=f"{Path('./').resolve()}/{Config.DIRECTORY}photos/")
        _txtLinks = rpyMSG.caption
    else: _txtLinks = rpyMSG.text
    _retxt = findall(r'https?://uploadever\.in\S+', _txtLinks)
    
    LOGGER.info(f"[BULK] Clone Links : {len(_retxt)}")
    Token = USERS_API.get(m.chat.id, None)
    if Token is None:
        await m.reply_text(text="<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>", parse_mode=enums.ParseMode.HTML, quote=True)
        return
    for no, link in enumerate(_retxt, 1):
        filecode = (link.split("/"))[-1]
        resp = rget(f"https://uploadever.in/api/file/clone?file_code={filecode}&key={Token}")
        jdata = resp.json()
        if jdata['status'] == 200:
            _txtLinks = _txtLinks.replace(link, jdata['result']['url'])
        else:
            await m.reply_text(f"⛔️ <b>ERROR: (Link No.: {no})</b> <code>{jdata['msg']}</code>", quote=True)
            _txtLinks = _txtLinks.replace(link, "")
    if rpyMSG.photo: await m.reply_photo(photo=_rpyPhoto, caption=_txtLinks, quote=True)
    else: await m.reply_text(_txtLinks, quote=True, disable_web_page_preview=True)
    orem(_rpyPhoto)





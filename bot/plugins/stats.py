#Copyright 2022-present, Author: 5MysterySD

from requests import get as rget
from pyrogram import filters, enums
from pyrogram.types import Message

from bot.client import Client
from bot.core.db.db_func import db
from config import LOGGER
from bot.core.display import convertBytes

@Client.on_message(filters.command("stats") & filters.private)
async def stats_handler(c: Client, m: Message):
    ''' UploadEver Account Stats Fetched from API
    :param token: Your Own API token of UploadEver.in

    OUTPUT: (info)
    
    OUTPUT: (stats)
    {
        "msg":"OK",
        "server_time":"2022-09-20 01:02:02",
        "status":200,
        "result":[
            {
             "profit_rebills":"0.0000",
             "downloads":1,
             "profit_dl":"0.0000",
             "sales":0,
             "profit_refs":"0.00000",
             "profit_sales":"0.0000",
             "profit_site":"0.00000",
             "day":"2022-09-19",
             "profit_total":"0.00000"
            }
        ]
    }
    '''

    Token = await db._getUserToken(m.chat.id)
    if Token is None:
        text_ = "<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>"
    else:
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        text_ = f'''<b>🗄 Your Account Info:</b>

• 📮 <b>Email :</b> <i>{jdata['result']['email']}</i>
• 💸 <b>Balance :</b> <code>{jdata['result']['balance']}</code>
• 📭 <b>Storage Left :</b> <code>{'Unlimited' if jdata['result']['storage_left'] == 'inf' else jdata['result']['storage_left']}</code>
• 📬 <b>Storage Used :</b> <code>{0 if jdata['result']['storage_used'] == None else convertBytes(jdata['result']['storage_used'])}</code>
• ⚠️ <b>Premium Expiry :</b> <code>{jdata['result']['premium_expire']}</code>

♻️ <b>Server Time :</b> <code>{jdata['server_time']}</code>

<b>🗃 Your Account Stats :</b>

'''
        resp2 = rget(f"https://uploadever.in/api/account/stats?key={Token}")
        jdata2 = resp2.json()
        if jdata2['msg'] != "OK" :
            text_ += f"• ⛔️ <b>{jdata2['msg']}</b> ⛔️"
        elif jdata2['status'] == 200:
            sData = jdata2['result'][0]
            text_ += f'''• 💳 <b>Profit Rebills :</b> <code>{sData['profit_rebills']}</code>
• 📥 <b>Downloads :</b> <code>{sData['downloads']}</code>
• 📩 <b>Profit Download :</b> <code>{sData['profit_dl']}</code>
• 🗳 <b>Sales :</b> <code>{sData['sales']}</code>
• 🖋 <b>Profit Refs :</b> <code>{sData['profit_refs']}</code>
• 🗂 <b>Profit Site :</b> <code>{sData['profit_site']}</code>
• 📆 <b>Current Day :</b> <code>{sData['day']}</code>
• 📈 <b>Total Profits :</b> <code>{sData['profit_total']}</code>
'''

    await m.reply_text(text=text_, parse_mode=enums.ParseMode.HTML, quote=True)

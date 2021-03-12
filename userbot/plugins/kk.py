"""command: .kk By @Grandpaa_please """


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "kk":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        else:
            await event.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")


import asynico
from telethon import events

@bot.on(pattern="تحديث", outgoing=True)
async def icss(event) 
 await event.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰")
 await async.sleep(1)
 await event.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰")

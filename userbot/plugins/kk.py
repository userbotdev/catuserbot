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


import asyncio


@bot.on(admin_cmd(pattern="تحديث", outgoing=True))
async def icss(ics):
    await ics.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰**")
    await asyncio.sleep(1)
    await ics.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰**")

@bot.on(admin_cmd(pattern="تيست", outgoing=True))
async def icss(ics):
    await ics.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰**")
    await asyncio.sleep(1)
    await ics.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰**")


import os
import random

from telethon.tl.users import GetFullUserRequst
from telethon.tl.types import MassageEntityMentoinName

hbk = [
  "100%"
  "90%"
  "80%"
  "70%"
  "60%"
  "50%"
  "40%"
  "30%"
  "20%"
  "10%"
  "0%"
]

@bot.on(admin_cmd(pattren="تيست", outgoing=True))
async def icss(mentoin):
    uu = random.choice(hbk)
    user, custom = await get_user_from_events(mention)
    if not user:
        return
    if custom:
       await edit_or_reply(
           mention, f" تسيت [{custom}](tg://user?id={user?id}) {uu}"
       )
   else:
       tag = (
           user.first_name.replace("\u2060", "") if user.first_name else user.username
       )
       await edit_or_reply(
           mention, f"تيست [{tag}](tg://user?id={user?id}) {uu}"
       )

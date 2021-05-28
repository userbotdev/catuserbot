import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from . import get_user_from_event
import asyncio
import base64
import random
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import BOTLOG, BOTLOG_CHATID, get_user_from_event
from . import catmemes

@bot.on(admin_cmd(pattern="join (.*)"))
@bot.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    await event.delete()
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="raid (.*)"))
@bot.on(sudo_cmd(pattern="raid (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.from_id is None and not event.is_private:
            await edit_delete(event, "`Well that's an anonymous admin !`")
            return None
        user = await event.client.get_entity(r_msg.sender_id)
        username = (f"@{user.username}")
        await edit_or_reply(event, f"{username}")
        RAIDHU = ["MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩", "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫", "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣", "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT", "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙", "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍", "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍", "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE" , "TERI VAHEEN DHANDHE VAALI 😋😛", "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI", "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚", "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱", "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩", "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈", "TERA PEHLA BAAP HU MADARCHOD ", "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹", "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ", "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ", "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭", "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬", "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 "] 
        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
        sleeptimet = sleeptimem = float(input_str[0])
        cat = input_str[1:]
        await event.delete()
        counter = int(cat[0])
        for _ in range(counter):
            reply = random.choice(RAIDHU)
            caption = f"{username} {reply}"
            sandy = await event.client.send_message(
                event.chat_id, caption
            )
            await asyncio.sleep(sleeptimem)
    else:
        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 3)
        sleeptimet = sleeptimem = float(input_str[0])
        cat = input_str[1:]
        user = input_str[2:]
        await event.delete()
        RAIDHU = ["MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩", "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫", "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣", "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT", "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙", "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍", "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍", "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE" , "TERI VAHEEN DHANDHE VAALI 😋😛", "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI", "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚", "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱", "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩", "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈", "TERA PEHLA BAAP HU MADARCHOD ", "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹", "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ", "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ", "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭", "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬", "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 "] 
        counter = int(cat[0])
        for _ in range(counter):
            reply = random.choice(RAIDHU)
            username = random.choice(user)
            caption = f"{username} {reply}"
            sandy = await event.client.send_message(
                event.chat_id, caption
            )
            await asyncio.sleep(sleeptimem)


@bot.on(admin_cmd(pattern="bio (.*)"))
@bot.on(sudo_cmd(pattern="bio (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    await event.delete()
    event = await edit_or_reply(event, "Trying")
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:
        await event.edit(str(e))
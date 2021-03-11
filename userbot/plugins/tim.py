import time

from . import StartTime, get_readable_time, mention, reply_id

DEFAULTUSER = "ICSS"
CAT_IMG = "https://telegra.ph/file/ca2467e77ffcd605cc54d.jpg"
CUSTOM_ALIVE_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪"
EMOJI = "  - ༻ : "


@bot.on(admin_cmd(outgoing=True, pattern="المده$"))
@bot.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{EMOJI} المستخدم ↫** {mention}\n"
        cat_caption += f"**{EMOJI} مدة التشغيل ↫** `{uptime}\n`"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**{EMOJI} المستخدم ↫** {mention}\n"
            f"**{EMOJI} مدة التشغيل ↫** `{uptime}\n`"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻",
        )

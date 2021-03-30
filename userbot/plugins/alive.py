import time
from platform import python_version

from telethon import version

from . import (
    ALIVE_NAME,
    TOSH,
    K,
    StartTime,
    catversion,
    get_readable_time,
    mention,
    reply_id,
)

DEFAULTUSER = ALIVE_NAME or "ICSS"
CAT_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑨𝑹𝑨𝑩𝑰𝑪 𝑪𝑨𝑻 𓆪"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  - ❝ ⌊ "


@bot.on(admin_cmd(outgoing=True, pattern="السورس$"))
@bot.on(sudo_cmd(pattern="السورس$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{EMOJI} قاعدة البيانات ↫** `{check_sgnirts}`\n"
        cat_caption += f"**{EMOJI} اصدار التليثون  ↫** `{version.__version__}\n`"
        cat_caption += f"**{EMOJI} اصدار كات ↫** `{catversion}`\n"
        cat_caption += f"**{EMOJI} اصدار البايثون ↫** `{python_version()}\n`"
        #        cat_caption += f"**{EMOJI} مدة التشغيل ↫** `{uptime}\n`"
        cat_caption += f"**{EMOJI} المستخدم ↫** {mention}\n"
        cat_caption += f"**{EMOJI} مطور السورس ↫** [اضغط هنا](t.me/rruuurr) 𓆰.\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} قاعدة البيانات ↫**  `{check_sgnirts}`\n"
            f"**{EMOJI} اصدار التليثون  ↫** `{version.__version__}\n`"
            f"**{EMOJI} اصدار كات ↫** `{catversion}`\n"
            f"**{EMOJI} اصدار البايثون  ↫** `{python_version()}\n`"
            f"**{EMOJI} مدة التشغيل ↫** `{uptime}\n`"
            f"**{EMOJI} المستخدم ↫** {mention}\n",
        )


if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("البوت") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("الرابط 🔗", K),
                ]
            ]
            if CAT_IMG and CAT_IMG.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    CAT_IMG, text=TOSH, buttons=buttons, link_preview=False
                )
            elif CAT_IMG:
                result = builder.document(
                    CAT_IMG,
                    title="Arabic - Cat",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Arabic - Cat",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="البوت"))
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(KIM, "البوت")
    await response[0].click(event.chat_id)
    await event.delete()


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n  •  **Syntax : **`.alive` \
      \n  •  **Function : **__status of bot will be showed__\
      \n\n  •  **Syntax : **`.ialive` \
      \n  •  **Function : **__inline status of bot will be shown.__\
      \nSet `ALIVE_PIC` var for media in alive message"
    }
)

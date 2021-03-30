from telethon import Button
from . import (
    ALIVE_NAME,
    TOSH, 
    catversion,
    mention,
    K,
    R,
)
@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def icsrepo(icsp):
    await eor(icsp, R)

CAT_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
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

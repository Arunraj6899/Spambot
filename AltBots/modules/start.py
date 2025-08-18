from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ll_GOD_ABOUT_ll"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/ll_GOD_ABOUT_ll")
    ],
    [
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/ll_GOD_ABOUT_ll")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [GOD ꭙ FATHER](https://t.me/ll_GOD_ABOUT_ll)**\n\n"
        TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━\n\n🥀 ᴛʜɪs ɪs sᴘᴀᴍ ʙᴏᴛ ᴅᴏɴ'ᴛ ᴛʜɪɴᴋ I ᴀᴍ ᴏᴡɴᴇʀ [ɪ ᴀᴍ Jᴜsᴛ ᴄᴏᴅᴇ ᴅᴇᴘʟᴏᴇʀ](https://t.me/ll_GOD_ABOUT_ll) , ᴜsᴇ sᴘᴀᴍʙᴏᴛ ᴀɴᴅ ᴇɴJᴏʏ"
        await event.client.send_file(
                    event.chat_id,
                    "https://envs.sh/urx.jpg/IMG20250818129.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )

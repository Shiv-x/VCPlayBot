from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am 𝗩𝗖𝗣𝗹𝗮𝘆𝗕𝗼𝘁 VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @HEROGAMERS1 ❤
For source code Join our support group @LaylaSupport.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/ĦŘØ-GΔΜŘ-04-02",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/LaylaSupport"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/QueenArzoo/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join ChatGroup", url="https://t.me/GIRLS_AND_BOYS_CHATTING"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

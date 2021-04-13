from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chat
Maintained by @HEROGAMERS1 ❤
\nTo add in your group contact us at @LaylaSupport.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Music World", url="https://t.me/GIRLS_AND_BOYS_CHATTING",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/LaylaSupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/LaylaList"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/QueenArzoo/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/VCPlayBot?startgroup=true"
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

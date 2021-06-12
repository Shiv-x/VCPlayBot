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
\nI Grubunuzun sesli sohbetinde müzik çalabilirim
Benim Tarafından korunur @yoksunhala 🥵🇹🇷
\nTo add in your group contact us at @CanmuzikSupport.
\nHit /help kullanılabilir komutların listesi..
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Müzik Dünyası", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/CanmuzikSupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    ),
                    InlineKeyboardButton(
                        "💾 Kaynak kodu", url="https://github.com/QueenArzoo/can131w"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Lgmuzik_bot?startgroup=true"
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
                        "🔊 Kanal", url="https://t.me/CanmuzikSupport"
                    ),
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    )
                ],    
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

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/CanmuzikSupport"
                    ),
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    )
                ]
            ]
        )
    )    

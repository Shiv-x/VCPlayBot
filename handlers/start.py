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
\nBot ini Bisa Digunakan Di Grup Anda ✅
Jika ada ditanyakan hubungi @RI024 ❤
\nJoin Channel Team support @sadnesstalk.
\nHai /help daftar perintah pengguna Music .
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "owner", url="https://t.me/RI024",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "grup", url="https://t.me/antigabutbrothers"
                    ),
                    InlineKeyboardButton(
                        "grup", url="https://t.me/SanssAbisssss"
                    ),
                    InlineKeyboardButton(
                        "support", url="https://t.me/Ngapangentott"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/santuabissss_bot?startgroup=true"
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
        "apakah kamu ingin memutar via YouTube coba gunakan url 🥰 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/sadnesstalk"
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
\n/play <song name> - play lagu dipilih via link youtube
/dplay <song name> - play lagu dipilih via deezer 
/splay <song name> - play lagu  dipilih via jio saavn 
/playlist - Melihat daftar lagu yang tersedia
/current - Tidak ada daftar putar 
/song <song name> - download music via song nama artis judul nama artis
/search <query> - search video via YouTube dengan nama judul artis
/deezer <song name> - download lagu ketik judul nama artis via deezer
/saavn <song name> - download lagu via saavn
/video <song name> - download video dengan nama judul via YouTube
\n*Admins only*
/player - open music panel bot music 
/pause - pause berhenti sementara play
/resume - resume berhenti sementara play
/skip - play melompat ke lagu lain
/end - stop berhenti memainkan
/userbotjoin - manggil music Assistant
itulah daftar perintah yang tersedia terimakasih 🙏
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/sadnesstalk"
                    )
                ]
            ]
        )
    )    

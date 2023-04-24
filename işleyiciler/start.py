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
        f"""<b>Merhaba {message.from_user.first_name}!
\nGrubunun sesli sohbetinde müzik çalabilirim @naberbebeq tarafından korunur ❤
\nSohbet ve Destek için @hzelpatrons.
\nKomutları görmek için /help yazman yeterli.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Müzik Dünyası", url="https://t.me/harleymusiic",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/hzelpatrons"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/harleymusiic"
                    ),
                    InlineKeyboardButton(
                        "💾 Kaynak Kodu", url="https://github.com/QueenArzoo/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Beni Gruba Ekle ➕", url="https://t.me/VCPlayBot?startgroup=true"
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
                        "🔊 Kanal", url="https://t.me/harleymusiic"
                    ),
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/hzelpatrons"
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
        f"""<b>Merhaba {message.from_user.first_name}!
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
                        "🔊 Kanal", url="https://t.me/harleymusiic"
                    ),
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/hzelpatrons"
                    )
                ]
            ]
        )
    )    

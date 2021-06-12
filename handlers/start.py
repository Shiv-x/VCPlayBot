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
Benim Tarafımdan korunur @yoksunhala ❤️🥵
\nTo adresinden bize ulaşın. @CanmuzikSupport.
\nHit Kullanılabilir komutların /help listesine basın...
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Müzik Dünyası" , url    =    "https://t.me/joinchat/31ibrhlU0SQ1ZjI0" ,
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    ),
                    InlineKeyboardButton(
                        "💾 kaynak kodu", url="https://github.com/Can131w"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekleyin ➕" , url    = "https://t.me/Lgmuzik_bot?startgroup=true"
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
async def start(client: from pyrogram import Client, filters
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
Benim Tarafımdan korunur @yoksunhala ❤️🥵
\nTo adresinden bize ulaşın. @CanmuzikSupport.
\nHit Kullanılabilir komutların /help listesine basın...
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Müzik Dünyası" , url    =    "https://t.me/joinchat/31ibrhlU0SQ1ZjI0" ,
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
                    ),
                    InlineKeyboardButton(
                        "💾 kaynak kodu", url="https://github.com/Can131w"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekleyin ➕" , url    = "https://t.me/Lgmuzik_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.editedClient, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ bir Youtube videosu aramak istermisiniz
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Kanal" , url = "https://t.me/CanmuzikSupport"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/joinchat/31ibrhlU0SQ1ZjI0"
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
/n/play <şarkı adı> - istediğiniz şarkıyı çal

 /dplay <şarkı adı> - deezer aracılığıyla istediğiniz şarkıyı çal

 /splay <şarkı adı> - jio saavn aracılığıyla istediğiniz şarkıyı çal

 /playlist - Şimdi oynatma listesini göster

 /current - Şimdi oynatılıyor göster

 /song <şarkı adı> - istediğiniz şarkıları hızlıca indirin

 /search <query> - youtube'da ayrıntılarla video arayın

 /deezer <şarkı adı> - deezer aracılığıyla istediğiniz şarkıları hızlı bir şekilde indirin

 /saavn <şarkı adı> - saavn aracılığıyla istediğiniz şarkıları hızlı bir şekilde indirin

 /video <şarkı adı> - istediğiniz videoları hızlıca indirin

 \n*Yalnızca yöneticiler*

 /player - müzik çalar ayarları panelini aç

 /pause - şarkı çalmayı duraklat

 /resume - şarkı çalmaya devam et

 /atla - sonraki şarkıyı çal

 /end - müzik çalmayı durdur

 /userbotjoin - asistanı sohbetinize davet edin

 /admincache - Yönetici listesini yenile
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

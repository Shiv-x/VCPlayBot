from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo ya, masukan assistant music @musicwan.\n\n ❗️ Rules:\n   - Tidak untuk chatting\n   - Tidak untuk spam\n\n 👉 **Masukan Music Assistant jika kendala hubungi admin.**\n\n 📖 jika ada kendala tentang music hubungi admin\n    - masukan ke grup music asisstant secara manual.\n   - informasi pengguna ada di petunjuk manual\n\n **jika ada kendala kontak ke @Musicwan**")
  return                        

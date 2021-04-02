from __future__ import unicode_literals
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from pyrogram.types import CallbackQuery
from youtube_search import YoutubeSearch
import aiohttp
import wget
import youtube_dl
import json
from Python_ARQ import ARQ
import asyncio
import aiofiles
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from tgcalls import pytgcalls
import tgcalls
from converter import convert
from youtube import download
import sira
from config import DURATION_LIMIT
from helpers.wrappers import errors, admins_only
from helpers.errors import DurationLimitError


chat_id = None
@Client.on_message(
    filters.command("play")
    & filters.group
    & ~ filters.edited
)
@errors
async def play(client: Client, message_: Message):
    audio = (message_.reply_to_message.audio or message_.reply_to_message.voice) if message_.reply_to_message else None
    chat_id=message_.chat.id
    res = await message_.reply_text("✯𝗩𝗖𝗣𝗹𝗮𝘆✯=🔄 Processing...")

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {audio.duration / 60} minute(s)"
            )

        file_name = audio.file_id + audio.file_name.split(".")[-1]
        file_path = await convert(await message_.reply_to_message.download(file_name))
    else:
        messages = [message_]
        text = ""
        offset = None
        length = None

        if message_.reply_to_message:
            messages.append(message_.reply_to_message)

        for message in messages:
            if offset:
                break

            if message.entities:
                for entity in message.entities:
                    if entity.type == "url":
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset == None:
            await res.edit_text("❕ You did not give me anything to play.")
            return

        url = text[offset:offset+length]

        file_path =await convert(download(url))

    if message_.chat.id in tgcalls.pytgcalls.active_calls:
        position = sira.add(message_.chat.id, file_path)
        await res.edit_text(f"✯𝗩𝗖𝗣𝗹𝗮𝘆✯=#️⃣ Queued at position {position}.")
    else:
        await res.edit_text("✯𝗩𝗖𝗣𝗹𝗮𝘆✯=▶️ Playing...")
        res.delete
        m = await client.send_photo(
        chat_id=message_.chat.id,
        photo="https://telegra.ph/file/7ffa8d18b9b7f1b51a81e.jpg",
        caption=f"Playing Your song Via  [✯𝗩𝗖𝗣𝗹𝗮𝘆✯](https://t.me/LaylaSupport).",
         ) 
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path)


#---------------------------------DEEZER------------------------------------------------------------------
@Client.on_message(
    filters.command("deezer")
    & filters.group
    & ~ filters.edited
)
async def deezer(client: Client, message_: Message):
    requested_by = message_.from_user.first_name
    text = message_.text.split(" ", 1)
    queryy = text[1]
    res = await message_.reply_text(f"Searching 👀👀👀 for `{queryy}` on deezer")
    try:
        arq = ARQ("https://thearq.tech")
        r = await arq.deezer(query=queryy, limit=1)
        title = r[0]["title"]
        duration = int(r[0]["duration"])
        thumbnail = r[0]["thumbnail"]
        artist = r[0]["artist"]
        url = r[0]["url"]
    except:
        await res.edit(
            "Found Literally Nothing, You Should Work On Your English!"
        )
        is_playing = False
        return
    file_path= await convert(wget.download(url))
    await res.edit("Generating Thumbnail")
    await generate_cover_square(requested_by, title, artist, duration, thumbnail)
    if message_.chat.id in tgcalls.pytgcalls.active_calls:
        await res.edit("adding in queue")
        position = sira.add(message_.chat.id, file_path)
        await res.edit_text(f"✯𝗩𝗖𝗣𝗹𝗮𝘆✯=#️⃣ Queued at position {position}.")
    else:
        await res.edit_text("✯𝗩𝗖𝗣𝗹𝗮𝘆✯=▶️ Playing.....")
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path)
    await res.delete()
    m = await client.send_photo(
        chat_id=message_.chat.id,
        photo="final.png",
        caption=f"Playing [{title}]({url}) Via [Deezer](https://t.me/AuraXSupport)."
    ) 
    os.remove("final.png")
# -----------------------------------------------------Jiosaavn-----------------------------------------------------------------
@Client.on_message(
    filters.command("saavn")
    & filters.group
    & ~ filters.edited
)
async def jiosaavn(client: Client, message_: Message):
    requested_by = message_.from_user.first_name
    chat_id=message_.chat.id
    text = message_.text.split(" ", 1)
    query = text[1]
    res = await message_.reply_text(f"Searching 👀👀👀 for `{query}` on jio saavn")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://jiosaavnapi.bhadoo.uk/result/?query={query}"
            ) as resp:
                r = json.loads(await resp.text())
        sname = r[0]["song"]
        slink = r[0]["media_url"]
        ssingers = r[0]["singers"]
        sthumb = r[0]["image"]
        sduration = int(r[0]["duration"])
    except Exception as e:
        await res.edit(
            "Found Literally Nothing!, You Should Work On Your English."
        )
        print(str(e))
        is_playing = False
        return
    file_path= await convert(wget.download(slink))
    if message_.chat.id in tgcalls.pytgcalls.active_calls:
        position = sira.add(message_.chat.id, file_path)
        await res.edit_text(f"✯𝗩𝗖𝗣𝗹𝗮𝘆✯=#️⃣ Queued at position {position}.")
    else:
        await res.edit_text("✯𝗩𝗖𝗣𝗹𝗮𝘆✯=▶️ Playing.....")
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path)
    await res.edit("Generating Thumbnail.")
    await generate_cover_square(requested_by, sname, ssingers, sduration, sthumb)
    await res.delete()
    m = await client.send_photo(
        chat_id=message_.chat.id,
        caption=f"Playing {sname} Via [Jiosaavn](https://t.me/AuraXSupport)",
        photo="final.png",
    )
    os.remove("final.png")


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage
 
 #-----------------------------------YOUTUBE--------------------------------------------------------------
@Client.on_message(
    filters.command("ut")
    & filters.group
    & ~ filters.edited
)
async def ytp(client: Client, message_: Message):
    requested_by = message_.from_user.first_name
    chat_id=message_.chat.id
    text = message_.text.split(" ", 1)
    query = text[1]
    res = await message_.reply_text(f"Searching 👀👀👀for `{query}` on You Tube")
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        thumbnail = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        views = results[0]["views"]
    except Exception as e:
        await res.edit(
            "Found Literally Nothing!, You Should Work On Your English."
        )
        is_playing = False
        print(str(e))
        return
    file_path = await convert(download(link))
    if message_.chat.id in tgcalls.pytgcalls.active_calls:
        position = sira.add(message_.chat.id, file_path)
        await res.edit_text(f"✯𝗩𝗖𝗣𝗹𝗮𝘆✯=#️⃣ Queued at position {position}.")
    else:
        await res.edit_text("✯𝗩𝗖𝗣𝗹𝗮𝘆✯=▶️ Playing....")
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path)
    await res.edit("Generating Thumbnail.")
    await generate_cover(requested_by, title, views, duration, thumbnail)
    res.delete
    m = await client.send_photo(
        chat_id=message_.chat.id,
        caption=f"Playing `{query}` Via [YouTube](https://t.me/AuraXSupport)",
        photo="final.png",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Watch on youtube", url=link)]]
        ),
        parse_mode="markdown",
    )
    os.remove("final.png")

async def generate_cover_square(requested_by, title, artist, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open("./background.png")
    image2 = Image.open("Others/AURAX.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Others/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text((190, 550), f"Artist: {artist}", (255, 255, 255), font=font)
    draw.text(
        (190, 590),
        f"Duration: {duration} Seconds",
        (255, 255, 255),
        font=font,
    )

    draw.text(
        (190, 670),
        f"Played By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


# Generate cover for youtube

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("Others/AURAX.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Others/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"Played By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")

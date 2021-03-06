#    This file is part of the ChannelAutoForwarder distribution (https://github.com/Benchamxd/Telegraph-Uploader).
#    Copyright (c) 2021 Rishisuperyo
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/RISHISUPERYO-GAMERZ/PROBOT-TELEGRAPH-MAKER/blob/main/License> 

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

Tgraph = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Tgraph.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Wait plz Lemme download the photo😎⚡`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`I HAVE DOWNLOADED THE PHOTO🥳🥳, sending u ⚡`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`WAIT AND EK MANTRA DE RAHA WOH BOL MUJHE:- 𝓢𝓐𝓚𝓐 𝓛𝓐𝓚𝓐 𝓑𝓞𝓞𝓜 𝓑𝓞𝓞𝓜`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Sending😎 Plz wait 😂⚡`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("『s』『o』『r』『r』『y』 『k』『u』『c』『h』 『g』『a』『r』『b』『a』『r』 『u』『i』 『h』『a』『e』 😔") 
  else:
    await message.reply_text("Bhai yaar aap plz 5 mb ka niche size ma koi pic de sakte😭 plz")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`r͛u͛k͛o͛ z͛a͛r͛a͛ s͛a͛b͛a͛r͛ k͛a͛r͛o͛😂😂😂`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Lo abh finnally bhej raha😂`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Kuch garbar hui hae really😶") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb😶😑")

@Tgraph.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/Rishisuperyogamerzin'),
        InlineKeyboardButton('⚡D̸E̸V͎E͎L͢O͢P̶E̶R̶⚡ ', url='https://t.me/Rishisuperyo')
    ]]v
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Halo me yaha hu dekh😶😉,
        
im a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegra.ph
        
Made With ⚡😎 By @Rishisuperyo_ping</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Tgraph.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/ultramaxupdates')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""There Is Nothing To Know More,
        
Just Send Me A Video/gif/photo Upto 5 mb.

i'll upload it to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Tgraph.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

Tgraph.run()


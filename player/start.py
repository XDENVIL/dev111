from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey I am Innexia Radio Bot 📻\n\n** `Add this Bot to your Group and Make it Admin \n2) Add` @InnexiaRadioBot `to your Group` \n3) **Commands** : \n`/radio`ytlink Live \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/SiderzChat")
                                    ]]
                            ))
   else:
      await m.reply("**Innexia Radio is Alive! ✨**")

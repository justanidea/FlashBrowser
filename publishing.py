# This example requires the 'message_content' intent.
import asyncio
import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from discord.ext import commands, tasks
from config.definitions import ROOT_DIR
from datetime import datetime

load_dotenv()
token: str = os.getenv("BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot: commands.Bot = commands.Bot(command_prefix=".", intents=intents, application_id=os.getenv("APP_ID"), allowed_mentions = discord.AllowedMentions(everyone = True), help_command=None)
bot.remove_command("help")
client = discord.Client(intents=intents)
print("The bot is INIT", flush=True)

@bot.event
async def on_ready():
    print("The bot is online", flush=True)
    bot.machine_id = os.getenv("MACHINE_ID")
    bot.easter: int = 0
    bot.program_path = os.path.join(ROOT_DIR)
    print("test", flush=True)
    bot.pre_raw_channel_id = int(os.getenv("PRE_RAW_CHANNEL"))
    bot.pre_raw_channel= bot.get_channel(bot.pre_raw_channel_id)
    bot.path = os.path.join(ROOT_DIR, 'Processed')
    bot.it_sending = 0
    if not  api_process_messages.is_running():
            api_process_messages.start(bot)
    
@tasks.loop(seconds = 1)
async def api_process_messages(self):
    try:
        await check_folder()
    except Exception as e:
        print(e, flush=True)
        
api_process_messages.before_loop
async def before_api_process_messages(self):
    await self.bot.wait_until_ready()

async def check_folder():
    path = "saved\\screenshots"
    dir = os.listdir(path) 
    if len(dir) != 0:     
        dir.reverse()
        for file in dir:
            file_sec = int(file[-6:-4])
            file_min = int(file[-9:-7])
            file_hour = int(file[-12:-10])
            now_min = int(str(datetime.now().strftime("%M")))
            now_hour = int(str(datetime.now().strftime("%H")))
            now_sec= int(str(datetime.now().strftime("%S")))
            now_total_sec = now_hour * 3600 + now_min * 60 + now_sec
            file_total_sec = file_hour * 3600 + file_min * 60 + file_sec
            if now_total_sec > file_total_sec + 10:
                print(str(now_total_sec - file_total_sec) + " seconds diff", flush=True)
                file_list= []
                try:
                    file_list.append(discord.File(f"{os.path.join(path, file)}", filename=file))
                except Exception as e:
                    print ("publishing.py failed with:", e.strerror, flush=True )     
                await bot.pre_raw_channel.send("", files=file_list)
                try:
                    os.remove(f"{os.path.join(path, file)}")
                    bot.it_sending += 1
                    if bot.it_sending >= 1:
                        # print("updating the screenCount", flush=True)
                        bot.it_sending = 1
                        break
                except OSError as e:
                    print ("publishing.py failed with:", e.strerror, flush=True )
                    
async def main():
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
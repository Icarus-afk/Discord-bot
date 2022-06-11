import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
<help - eida likhle tore help korbo
<p <keywords> - tore youtube er the gaan bair koira hunaibo
<q - pura gaan er list dekhaibo
<skip - gaan skip korbo
<clear - shob clear koira falaibo. 
<leave - disconnect koira falaibo
<pause - tor life er moto gaan o pause koira dibo
<resume - thamainna gaan abar bajaibo
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
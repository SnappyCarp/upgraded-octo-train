import json
import discord



with open('Authorization.json', 'r') as f:
    data=json.load(f)
    Token=data['Token']

class ScreenshareSelfbot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author==self.user: return
        if message.content == 'ping' and message.author.id==904144997559975937:
            await message.channel.send('pong')


ScreenshareSelfbot().run(Token)
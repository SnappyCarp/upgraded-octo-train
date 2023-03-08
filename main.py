import json
import discord



with open('Authorization.json', 'r') as f:
    data=json.load(f)
    Token=data['Token']

class ScreenshareSelfbot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        #Put Your Userid Here ↓
        self.AuthorId = 1

    async def on_message(self, message):
        if message.author==self.user: return
        if message.content == 'ping' and message.author.id==self.AuthorId:
            await message.channel.send('pong')


ScreenshareSelfbot().run(Token)

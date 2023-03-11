from threading import Thread
from discord.errors import HTTPException
from selenium import webdriver
import discord
import json

with open('Authorization.json', 'r') as f: data=json.load(f); Prefix:str = data['Prefix']


class ScreenshareSelfbot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user, 'Bot is Ready For Use')

    async def on_message(self, message):
        #don't respond to self
        if message.author==self.user: return

        #commands
        #ping command
        if message.content == Prefix+'ping':
            await message.channel.send(f'Client Ping Is {self.latency*1000}ms')
            print(message.author.name, 'Used The Command Ping')
        #start streaming
        elif message.content.startswith(Prefix+'Video'):
            YtUrl = message.content.replace(Prefix, '').replace('Video', '')
            try:
                await message.channel.send('Loading Video')
            except HTTPException:
                await message.channel.send('Please Send A Youtube Url')
            



Thread(target=ScreenshareSelfbot().run(data['Token'])).start()

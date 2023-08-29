import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
         await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1- Não Desrespeitar os membros do Servidor{os.linesep} regra importante 2')
        elif message.content == '?nível':
            await message.author.send('Nível 1')
        elif message.content == '?github':
            await message.author.send(f'{message.author.name} os comandos são: 1 - git add 2 - git commit -m first commit 3 - git branch -M main 4- git push -u origin main')
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE0NTg1Mjk4MzUyMzk1NDc1OQ.GeiRpt.OjXfrXQP3WU1X6DTyW_CiKzGJP4gTMVHnbySjM')

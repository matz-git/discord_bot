import discord
import random
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('BOT.py'))
        print('Bot is online.')
    
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f'{member} has joined a server.')

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f'{member} has left a server.')

    @commands.command(aliases=['color', 'colors'])
    async def _3colors(self, ctx, question):
        responses = [
            "yellow",
            "blue",
            "red"
        ]
        await ctx.send(f'{question}?\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(General(client))

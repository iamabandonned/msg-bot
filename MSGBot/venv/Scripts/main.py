import discord
from discord.ext import commands
from discord.ext.commands import UserConverter
intents = intents=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)
client.remove_command('help')
class MSGBot(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print('Um herer')
    @commands.command()
    async def msg(self, ctx, user, author, *m):
        conv = UserConverter()
        msg1 = " ".join(m)
        user1: discord.User = await conv.convert(ctx, str(user))
        try:
            await user1.send(f'{author} whispered you: {msg1}')
        except:
            await ctx.send(f'Cannot send {user1} any message :(')
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.set_author(name='Help')
        embed.add_field(name='.msg id author message', value='Send private messages to a user by his id on behalf of author', inline=False)
        await ctx.send(embed=embed)

    async def setup(client):
        await client.add_cog(MSGBot(client))

token = "ODQ5OTI3ODQ1MTE4ODY5NTI0.GRBvQH.peNu_KbHJiOHc-YdZH6ykCCAuAxd1IajPqHrBM"
client.run(token)
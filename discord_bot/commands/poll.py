```python
import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll')
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to start a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot have more than 10 options.')
            return

        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))

        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

def setup(bot):
    bot.add_cog(Poll(bot))
```
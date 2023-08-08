```python
import discord
from discord.ext import commands
import random
from utils import error_handling

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='giveaway')
    @commands.has_role('Admin')
    async def giveaway(self, ctx):
        """Selects a random user with a specific role as the winner of a giveaway."""
        try:
            role = discord.utils.get(ctx.guild.roles, name="Giveaway Participant")
            members = [member for member in ctx.guild.members if role in member.roles]
            if not members:
                await ctx.send("No users with the 'Giveaway Participant' role found.")
                return
            winner = random.choice(members)
            await ctx.send(f"Congratulations {winner.mention}! You have won the giveaway!")
        except Exception as e:
            await error_handling.handle_error(ctx, str(e))

def setup(bot):
    bot.add_cog(Giveaway(bot))
```
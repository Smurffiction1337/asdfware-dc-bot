```python
import discord
from discord.ext import commands
from discord_bot.utils import error_handling

class Feedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='feedback')
    async def feedback(self, ctx, *, message: str):
        """Allows users to provide feedback for the server."""
        try:
            feedback_channel = discord.utils.get(ctx.guild.channels, name="feedback")
            if feedback_channel is None:
                await ctx.send("Feedback channel does not exist.")
                return

            embed = discord.Embed(title="New Feedback", description=message, color=0x00ff00)
            embed.set_footer(text=f"Feedback by: {ctx.author.name}")
            await feedback_channel.send(embed=embed)
            await ctx.send("Your feedback has been submitted successfully.")
        except Exception as e:
            await error_handling.handle_error(ctx, str(e))

def setup(bot):
    bot.add_cog(Feedback(bot))
```
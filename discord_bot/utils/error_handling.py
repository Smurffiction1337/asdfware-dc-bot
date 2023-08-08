```python
import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command. Please use a valid command.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You are missing a required argument for this command.')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send('This command is on cooldown. Please try again later.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the required permissions to use this command.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I do not have the required permissions to execute this command.')
        else:
            await ctx.send('An unexpected error occurred. Please try again later.')

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
```
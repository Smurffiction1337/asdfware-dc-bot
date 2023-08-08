```python
import discord
from discord.ext import commands
from discord_bot.config import BOT_TOKEN
from discord_bot.commands import giveaway, poll, profile, csgoitems, permissions, feedback
from discord_bot.utils import error_handling

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.add_cog(giveaway.Giveaway(bot))
bot.add_cog(poll.Poll(bot))
bot.add_cog(profile.Profile(bot))
bot.add_cog(csgoitems.CSGOItems(bot))
bot.add_cog(permissions.Permissions(bot))
bot.add_cog(feedback.Feedback(bot))

bot.add_error_handler(error_handling.handle_error)

bot.run(BOT_TOKEN)
```
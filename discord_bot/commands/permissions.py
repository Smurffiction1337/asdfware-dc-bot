```python
import discord
from discord.ext import commands
from discord_bot.utils.error_handling import handle_error

class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='permissions')
    @commands.has_permissions(administrator=True)
    async def permissions(self, ctx, command: str, role: discord.Role, permission: str):
        try:
            if permission.lower() not in ['allow', 'deny']:
                await ctx.send("Invalid permission type. Use 'allow' or 'deny'.")
                return

            if command not in self.bot.command_names:
                await ctx.send(f"Invalid command '{command}'.")
                return

            if permission.lower() == 'allow':
                self.bot.command_permissions[command].add(role.id)
                await ctx.send(f"Role '{role.name}' has been allowed to use the command '{command}'.")
            else:
                self.bot.command_permissions[command].discard(role.id)
                await ctx.send(f"Role '{role.name}' has been denied from using the command '{command}'.")
        except Exception as e:
            await handle_error(ctx, e)

def setup(bot):
    bot.add_cog(Permissions(bot))
```
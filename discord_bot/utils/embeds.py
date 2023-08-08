```python
import discord

def create_profile_embed(profile_data):
    embed = discord.Embed(
        title=f"{profile_data['personaname']}'s Steam Profile",
        url=profile_data['profileurl'],
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=profile_data['avatar'])
    embed.add_field(name="Status", value=profile_data['personastate'], inline=True)
    return embed

def create_csgoitems_embed(items_data, profile_url):
    embed = discord.Embed(
        title="Top 5 Expensive CS:GO Items",
        url=profile_url,
        color=discord.Color.green()
    )
    for item in items_data:
        embed.add_field(name=item['name'], value=f"Price: {item['price']}", inline=False)
    return embed

def create_poll_embed(question, options):
    embed = discord.Embed(
        title=question,
        color=discord.Color.orange()
    )
    for i, option in enumerate(options, start=1):
        embed.add_field(name=f"Option {i}", value=option, inline=False)
    return embed

def create_feedback_embed(message, user):
    embed = discord.Embed(
        title="New Feedback Submitted",
        description=message,
        color=discord.Color.purple()
    )
    embed.set_footer(text=f"Submitted by: {user}")
    return embed

def create_error_embed(error_message):
    embed = discord.Embed(
        title="Error",
        description=error_message,
        color=discord.Color.red()
    )
    return embed
```
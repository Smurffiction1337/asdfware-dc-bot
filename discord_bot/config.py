```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord Bot Token
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Steam Web API Key
STEAM_WEB_API_KEY = os.getenv('STEAM_WEB_API_KEY')

# Command Prefix
COMMAND_PREFIX = '!'

# Role for Giveaway
GIVEAWAY_ROLE = os.getenv('GIVEAWAY_ROLE')

# Feedback Channel
FEEDBACK_CHANNEL = os.getenv('FEEDBACK_CHANNEL')
```
```python
import requests
from .rate_limiting import rate_limited
from ..config import STEAM_API_KEY

STEAM_API_BASE_URL = "http://api.steampowered.com"

@rate_limited()
def get_player_summaries(steamid64):
    url = f"{STEAM_API_BASE_URL}/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={steamid64}"
    response = requests.get(url)
    data = response.json()
    return data['response']['players'][0] if data['response']['players'] else None

@rate_limited()
def get_inventory(steamid64, appid=730):
    url = f"{STEAM_API_BASE_URL}/IEconItems_{appid}/GetPlayerItems/v0001/?key={STEAM_API_KEY}&steamid={steamid64}"
    response = requests.get(url)
    data = response.json()
    return data['result']['items'] if data['result']['items'] else None

@rate_limited()
def get_item_price(itemid, currency='USD'):
    url = f"{STEAM_API_BASE_URL}/ISteamEconomy/GetAssetPrices/v0001/?key={STEAM_API_KEY}&appid=730&currency={currency}"
    response = requests.get(url)
    data = response.json()
    prices = data['result']['assets']
    for price in prices:
        if price['classid'] == itemid:
            return price['price']
    return None
```
from requests import get

from data.config import ETHSCAN_API_KEY

ETH_VALUE = 10 ** 18

async def async_check_eth_balance(address: str, api_key: str) -> str:
    URL = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    return str(int(get(URL).json()['result']) / ETH_VALUE)


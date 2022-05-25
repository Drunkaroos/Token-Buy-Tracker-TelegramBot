from json import JSONDecodeError, loads
from requests import get as getRequest
from pydantic import BaseModel, ValidationError


url = "https://api.unmarshal.com/v2/ethereum/address/0x6e48dbea2d3b37e4d605fda71e85c52ebc40aa40/transactions"

class Transaction(BaseModel):
    """
    group_helper configuration class
    """
    id: str
    date: int
    native_token_decimals: int
    received: list
    sent: list
        
query = {
  "page": "1",
  "pageSize": "5",
  "contract": "0xc4c75f2a0cb1a9acc33929512dc9733ea1fd6fde",
  "auth_key": "9TwbFPmBpx8Sz9JjhWm229Ff5elVbxq21s4UIjzG"
}

class UnmarshalApi():
    def __init__(self, eth_address, contract, chain, auth_key) -> None:
        self.eth_address = "0x6e48dbea2d3b37e4d605fda71e85c52ebc40aa40"
        self.chain = "ethereum"

    def getTransactions(self):
        resp = getRequest(url, params=query)

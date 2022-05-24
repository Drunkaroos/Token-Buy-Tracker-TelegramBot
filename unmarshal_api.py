from json import JSONDecodeError, loads
from requests import get as getRequest
from pydantic import BaseModel, ValidationError




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
  "pageSize": "1",
  "contract": "0x19ce9b1b9db57fce6e5057230ba105e499ad6a00",
  "auth_key": "9TwbFPmBpx8Sz9JjhWm229Ff5elVbxq21s4UIjzG"
}

class UnmarshalApi():
    def __init__(self, eth_address, contract, chain, auth_key) -> None:
        self.eth_address = eth_address
        self.contract = contract
        self.chain = chain
        self.api_key = UNMARSHAL_API_KEY
        url = "https://api.unmarshal.com/v2/{self.chain}/address/{self.eth_address}/transactions"

    def getTransactions(self):
        resp = getRequest(url, params=query)

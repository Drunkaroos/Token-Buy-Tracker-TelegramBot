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


class UnmarshalApi():
    def __init__(self, eth_address, contract, chain, UNMARSHAL_API_KEY) -> None:
        self.eth_address = eth_address
        self.contract = contract
        self.chain = chain
        self.api_key = UNMARSHAL_API_KEY
        self.url = f"https://api.unmarshal.com/v2/{self.chain}/address/{self.eth_address}/transactions?page=0&pageSize=1&contract={self.contract}&auth_key={self.api_key}"

    def getTransactions(self):
        resp = getRequest(self.url)
        try:
            resp = resp.json()
            last_transaction = resp['transactions'] 
            if last_transaction:
                return Transaction(**dict(last_transaction[0]))
            else:
                return None
        except JSONDecodeError:
            return None 

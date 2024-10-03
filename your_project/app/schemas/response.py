from pydantic import BaseModel
from typing import List, Optional

class Token(BaseModel):
    symbol: Optional[str] = None
    decimals: Optional[int] = None  # Add the decimals field

class Transaction(BaseModel):
    from_: Optional[str] = None
    to: Optional[str] = None
    transaction_hash: Optional[str] = None
    amount: Optional[str] = None
    token: Optional[Token] = None  # Use the Token class instead of str

class TransactionResponse(BaseModel):
    transactions: List[Transaction]
    total: int
    error: Optional[str] = None

import requests
from schemas.response import TransactionResponse

def get_transactions(page: int, page_size: int) -> TransactionResponse:
    url = "https://block-explorer-api.mainnet.zksync.io/address/0x75490D0E8EF212c993c06DA92deF1cbBA684F77E/transfers"
    params = {
        "toDate": "2024-10-03T03:08:30.908Z",
        "limit": page_size,  # Changed 'pageSize' to 'limit'
        "page": page
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data:  # Check for 'items' instead of 'list'
            transactions = []
            for tx in data['items']:  # Loop through 'items'
                transaction = {
                    "from": tx.get("from"),
                    "to": tx.get("to"),
                    "transaction_hash": tx.get("transactionHash"),
                    "amount": tx.get("amount"),
                    "token":{ "symbol":tx.get("token", {}).get("symbol"),
                             "decimals": tx.get("token", {}).get("decimals")
                            }
                }
                transactions.append(transaction)
            return TransactionResponse(transactions=transactions, total=data['meta']['totalItems'])  # Use 'meta.totalItems'
        else:
            # Log the full response for debugging purposes
            print("Unexpected response format:", data)
            return TransactionResponse(transactions=[], total=0, error="Unexpected response format")
    else:
        return TransactionResponse(transactions=[], total=0, error=f"Failed to retrieve transactions: {response.status_code}")

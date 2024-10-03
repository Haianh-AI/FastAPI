from fastapi import FastAPI
from routers import transactions

app = FastAPI()

# Include the transactions router
app.include_router(transactions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the zkSync API Service!"}

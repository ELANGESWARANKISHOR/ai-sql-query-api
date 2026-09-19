from fastapi import FastAPI
from pydantic import BaseModel
from app.database import get_connection


app = FastAPI(title="AI SQL Query API")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI SQL Query API is running"
    }


@app.get("/customers")
def get_customers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    connection.close()

    return {
        "customers": customers
    }


@app.post("/query")
def query_database(request: QueryRequest):
    return {
        "question": request.question,
        "message": "Question received successfully"
    }
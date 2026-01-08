import psycopg2
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis

app = FastAPI()
origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Connexion
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD"),
    database=os.getenv("POSTGRES_DB", "ynov_ci")
)

rdb = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)

@app.get('/')
async def get_version():
    cur = conn.cursor()
    cur.execute("SELECT nom, promo FROM students ORDER BY id;")
    rows = cur.fetchall()
    views = rdb.incr("students:views")
    return [{"nom": r[0], "promo": r[1], "views": views} for r in rows]


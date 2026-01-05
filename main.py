import psycopg2
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get('/')
async def get_version():
    cur = conn.cursor()
    cur.execute("UPDATE students SET views = views + 1;")
    cur.execute("SELECT nom, promo, views FROM students ORDER BY id;")
    rows = cur.fetchall()
    conn.commit()
    return [{"nom": r[0], "promo": r[1], "views": r[2]} for r in rows]



import sqlite3
from pathlib import Path
import json

# schema path
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"
# DB path
DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent.parent / "greenhouse.db"
# Data path (seeding DB from data)
_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def connect(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db(db_path: Path | str = DEFAULT_DB_PATH) -> None:
    conn = connect(db_path)
    try:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()

#  SEED DB EXAMPLE
#
# def seed_from_json(db_path: Path | str = DEFAULT_DB_PATH) -> tuple[int, int]:
#     customers = json.loads((_DATA_DIR / "customers.json").read_text(encoding="utf-8"))
#     tickets = json.loads((_DATA_DIR / "tickets.json").read_text(encoding="utf-8"))
#     conn = connect(db_path)
#     try:
#         conn.executemany(
#             """
#                 INSERT OR REPLACE INTO customers
#                     (id, name,tenant, plan, primary_contact_email, created_at)
#                     VALUES (:id, :name, :tenant, :plan, :primary_contact_email, :created_at)
#             """, customers
#         )
#         conn.commit()
#     finally: 
#         conn.close()

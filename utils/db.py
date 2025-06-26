import json
from pathlib import Path

DB_PATH = Path("database.json")

def load_db():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_user(user_id, ref_id=None):
    db = load_db()
    if user_id not in db["users"]:
        db["users"][user_id] = {"balance": 0}
        if ref_id and ref_id in db["users"]:
            db["referrals"].setdefault(ref_id, []).append(user_id)
            db["users"][ref_id]["balance"] += 10
    save_db(db)

def get_user_balance(user_id):
    db = load_db()
    return db["users"].get(user_id, {}).get("balance", 0)

def update_user_balance(user_id, amount):
    db = load_db()
    if user_id in db["users"]:
        db["users"][user_id]["balance"] += amount
    else:
        db["users"][user_id] = {"balance": amount}
    save_db(db)
    return db["users"][user_id]["balance"]

def request_withdraw(user_id, amount):
    db = load_db()
    db["withdraw_requests"].append({"user_id": user_id, "amount": amount})
    save_db(db)
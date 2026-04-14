import json
import os
import random
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

random.seed(42)

CATEGORIES = ["Food", "Transport", "Personal", "Entertainment", "Health", "Utilities"]

DESCRIPTIONS = {
    "Food": ["McDonald's", "KFC", "Canteen lunch", "Bubble tea", "7-Eleven", "Sushi", "Hotpot", "Dim sum", "Noodles", "Cake shop"],
    "Transport": ["MTR fare", "Bus fare", "Taxi", "Cross-harbour tunnel", "Airport Express", "Minibus", "Ferry"],
    "Personal": ["Uniqlo shirt", "Skincare", "Haircut", "Stationery", "Phone case", "Earphones", "Shoes", "Bag"],
    "Entertainment": ["Netflix", "Cinema ticket", "KTV", "Board game cafe", "Steam game", "Concert ticket", "Spotify"],
    "Health": ["Pharmacy", "Face mask", "Vitamins", "Gym pass", "Doctor visit", "Dental check"],
    "Utilities": ["Phone bill", "Water bill", "Electricity", "Internet fee", "Cloud storage"],
}

AMOUNT_RANGES = {
    "Food": (15, 120),
    "Transport": (5, 55),
    "Personal": (50, 400),
    "Entertainment": (30, 600),
    "Health": (20, 250),
    "Utilities": (100, 600),
}


def rand_amount(cat):
    lo, hi = AMOUNT_RANGES.get(cat, (10, 100))
    return round(random.uniform(lo, hi), 1)


def generate_transactions(n=120):
    transactions = []
    now = datetime.now()

    for i in range(n):
        days_ago = random.randint(0, 30)
        date = (now - timedelta(days=days_ago)).strftime("%Y-%m-%d")

        if i < 5:
            cat = "Uncategorized"
            desc = "Miscellaneous item"
        elif i >= 105:
            cat = "Entertainment"
            desc = random.choice(["Netflix", "Spotify", "YouTube Premium", "iCloud+", "Disney+", "Apple Music"])
            date = (now - timedelta(days=random.randint(0, 5))).strftime("%Y-%m-%d")
        else:
            cat = random.choice(CATEGORIES)
            desc = random.choice(DESCRIPTIONS[cat])

        transactions.append({
            "id": i + 1,
            "date": date,
            "amount": rand_amount(cat) if cat != "Uncategorized" else round(random.uniform(10, 50), 1),
            "currency": "HKD",
            "category": cat,
            "description": desc,
        })

    return sorted(transactions, key=lambda x: x["date"])


def generate_budget_rules():
    return [
        {"category": "Food",          "daily_cap": 80,  "monthly_cap": 2400, "pct_threshold": 35},
        {"category": "Transport",     "daily_cap": 30,  "monthly_cap": 900,  "pct_threshold": 20},
        {"category": "Entertainment", "daily_cap": 100, "monthly_cap": 1500, "pct_threshold": 25},
        {"category": "Personal",      "daily_cap": 200, "monthly_cap": 2000, "pct_threshold": 30},
        {"category": "Health",        "daily_cap": 150, "monthly_cap": 1000, "pct_threshold": 15},
    ]


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base, "data")
    os.makedirs(data_dir, exist_ok=True)

    txns = generate_transactions(120)
    rules = generate_budget_rules()

    with open(os.path.join(data_dir, "transactions.json"), "w") as f:
        json.dump(txns, f, indent=2)

    with open(os.path.join(data_dir, "budget_rules.json"), "w") as f:
        json.dump(rules, f, indent=2)

    print(f"Generated {len(txns)} transactions → data/transactions.json")
    print(f"Generated {len(rules)} budget rules  → data/budget_rules.json")
    print("\nEdge cases included:")
    print("  • 5 Uncategorized transactions (IDs 1–5)")
    print("  • Subscription creep spike: Entertainment transactions last 5 days (IDs 106–120)")


if __name__ == "__main__":
    main()

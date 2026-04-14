import calendar
from collections import defaultdict
from datetime import datetime, timedelta


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


def filter_by_date(transactions, start=None, end=None):
    result = []
    for t in transactions:
        d = parse_date(t["date"])
        if start and d < start:
            continue
        if end and d > end:
            continue
        result.append(t)
    return result


def get_totals_by_category(transactions, start=None, end=None):
    filtered = filter_by_date(transactions, start, end)
    totals = defaultdict(float)
    for t in filtered:
        totals[t["category"]] += t["amount"]
    return dict(totals)


def get_top_n_categories(transactions, n=3, start=None, end=None):
    totals = get_totals_by_category(transactions, start, end)
    total = sum(totals.values())
    sorted_cats = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return [
        (cat, amt, (amt / total * 100) if total > 0 else 0)
        for cat, amt in sorted_cats[:n]
    ]


def get_spending_trends(transactions):
    now = datetime.now()
    last_7 = filter_by_date(transactions, now - timedelta(days=7), now)
    last_30 = filter_by_date(transactions, now - timedelta(days=30), now)
    avg_7 = sum(t["amount"] for t in last_7) / 7 if last_7 else 0
    avg_30 = sum(t["amount"] for t in last_30) / 30 if last_30 else 0
    return avg_7, avg_30


def get_daily_totals_by_category(transactions, category):
    daily = defaultdict(float)
    for t in transactions:
        if t["category"] == category:
            daily[t["date"]] += t["amount"]
    return dict(daily)


def get_consecutive_overspend(transactions, category, daily_cap):
    daily = get_daily_totals_by_category(transactions, category)
    sorted_dates = sorted(daily.keys(), reverse=True)
    streak = 0
    for date_str in sorted_dates:
        if daily[date_str] > daily_cap:
            streak += 1
        else:
            break
    return streak


def get_savings_progress(transactions, savings_goal, income):
    now = datetime.now()
    start = datetime(now.year, now.month, 1)
    monthly = filter_by_date(transactions, start, now)
    spent = sum(t["amount"] for t in monthly)
    remaining = income - spent
    savings = remaining - savings_goal
    return spent, remaining, savings


def linear_forecast(transactions):
    now = datetime.now()
    start = datetime(now.year, now.month, 1)
    monthly = filter_by_date(transactions, start, now)
    if not monthly:
        return 0.0
    days_elapsed = (now - start).days + 1
    spent = sum(t["amount"] for t in monthly)
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    return (spent / days_elapsed) * days_in_month


def spending_heatmap(transactions):
    now = datetime.now()
    start = datetime(now.year, now.month, 1)
    monthly = filter_by_date(transactions, start, now)

    daily = defaultdict(float)
    for t in monthly:
        daily[t["date"]] += t["amount"]

    if not daily:
        return {}

    avg = sum(daily.values()) / len(daily)
    result = {}
    for date_str, amt in daily.items():
        ratio = amt / avg if avg > 0 else 0
        if ratio < 0.5:
            sym = "░"
        elif ratio < 1.0:
            sym = "▒"
        elif ratio < 1.5:
            sym = "▓"
        else:
            sym = "█"
        result[date_str] = (sym, amt)
    return result

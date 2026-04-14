from datetime import datetime
from analytics import (
    get_daily_totals_by_category,
    get_totals_by_category,
    get_consecutive_overspend,
)


def check_daily_caps(transactions, budget_rules):
    today = datetime.now().strftime("%Y-%m-%d")
    alerts = []
    for rule in budget_rules:
        if "daily_cap" not in rule:
            continue
        cat = rule["category"]
        cap = rule["daily_cap"]
        daily = get_daily_totals_by_category(transactions, cat)
        today_total = daily.get(today, 0)
        if today_total > cap:
            alerts.append({
                "type": "daily_exceeded",
                "category": cat,
                "spent": today_total,
                "cap": cap,
                "message": f"{cat}: Daily limit exceeded! (HK${today_total:.2f} / HK${cap:.2f})",
            })
    return alerts


def check_percentage_thresholds(transactions, budget_rules):
    totals = get_totals_by_category(transactions)
    total = sum(totals.values())
    alerts = []
    if total == 0:
        return alerts
    for rule in budget_rules:
        if "pct_threshold" not in rule:
            continue
        cat = rule["category"]
        threshold = rule["pct_threshold"]
        pct = (totals.get(cat, 0) / total * 100)
        if pct > threshold:
            alerts.append({
                "type": "pct_exceeded",
                "category": cat,
                "pct": pct,
                "threshold": threshold,
                "message": f"{cat}: {pct:.1f}% of total (limit: {threshold}%)",
            })
    return alerts


def check_consecutive_overspend(transactions, budget_rules):
    alerts = []
    for rule in budget_rules:
        if "daily_cap" not in rule:
            continue
        cat = rule["category"]
        streak = get_consecutive_overspend(transactions, cat, rule["daily_cap"])
        if streak >= 3:
            alerts.append({
                "type": "consecutive_overspend",
                "category": cat,
                "streak": streak,
                "message": f"{cat}: Budget exceeded for {streak} consecutive days!",
            })
    return alerts


def check_uncategorized(transactions, categories):
    alerts = []
    for t in transactions:
        if t["category"] == "Uncategorized" or t["category"] not in categories:
            alerts.append({
                "type": "uncategorized",
                "id": t["id"],
                "category": t["category"],
                "message": f"Transaction #{t['id']} has invalid/unknown category: '{t['category']}'",
            })
    return alerts


def get_all_alerts(transactions, budget_rules, categories):
    alerts = []
    alerts += check_daily_caps(transactions, budget_rules)
    alerts += check_percentage_thresholds(transactions, budget_rules)
    alerts += check_consecutive_overspend(transactions, budget_rules)
    alerts += check_uncategorized(transactions, categories)
    return alerts

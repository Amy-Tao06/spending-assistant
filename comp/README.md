# COMP1110 B12 — Personal Budget & Spending Assistant

**Project**: Personal Budget & Spending Assistant (Topic A)  
**Members**: Mao Yicheng, Tao Xinran, Wang Ziyi, Yang Andi, Yao Junzhu  
**Repo**: `comp1110-project` (private)

---

## 📋 Quick Links

| Document | Purpose |
|----------|---------|
| [GUIDELINES.md](GUIDELINES.md) | Official assignment spec |
| [PLAN.md](PLAN.md) | Timeline, research, roles |
| [FEATURES.md](FEATURES.md) | Feature list |
| [UI.md](UI.md) | UI/interface design specs |
| [CLAUDE.md](CLAUDE.md) | Code conventions |

## 🗂️ Project Structure

```
comp1110projectlocal/
├── main.py              ← Entry point; questionary menu loop
├── display.py           ← All rich rendering (tables, panels, alerts)
├── analytics.py         ← Statistics, trends, forecasting, heatmap
├── alerts.py            ← Alert logic (caps, thresholds, streaks)
├── data.py              ← JSON load/save; file I/O helpers
├── validator.py         ← Input validation (dates, amounts, categories)
│
├── config/
│   └── config.json      ← Categories, currencies, savings goal, income
├── data/
│   ├── transactions.json
│   └── budget_rules.json
├── outputs/             ← Generated .txt reports
├── tests/
│   └── test_generator.py ← 120+ fake transactions with edge cases
│
├── requirements.txt
└── README.md
```

### Module responsibilities

| File | Key functions |
|------|--------------|
| `main.py` | `main()`, `add_transaction_flow()`, `view_transactions_flow()`, `edit_delete_flow()`, `statistics_flow()`, `alerts_flow()`, `manage_budget_rules_flow()`, `manage_categories_flow()`, `settings_flow()`, `export_flow()` |
| `display.py` | `print_transaction_table()`, `print_statistics()`, `print_top_categories()`, `print_trends()`, `print_alerts()`, `print_budget_bars()`, `print_budget_rules()`, `print_savings_goal()`, `print_heatmap()`, `print_forecast()`, `export_report()` |
| `analytics.py` | `filter_by_date()`, `get_totals_by_category()`, `get_top_n_categories()`, `get_spending_trends()`, `get_daily_totals_by_category()`, `get_consecutive_overspend()`, `get_savings_progress()`, `linear_forecast()`, `spending_heatmap()` |
| `alerts.py` | `check_daily_caps()`, `check_percentage_thresholds()`, `check_consecutive_overspend()`, `check_uncategorized()`, `get_all_alerts()` |
| `data.py` | `load_transactions()`, `save_transactions()`, `load_budget_rules()`, `save_budget_rules()`, `load_config()`, `save_config()`, `get_next_id()`, `ensure_dirs()` |
| `validator.py` | `validate_date()`, `validate_amount()`, `validate_category()`, `validate_description()` |

### Data schemas

**Transaction**
```json
{"id": 1, "date": "2026-04-01", "amount": 50.5, "currency": "HKD", "category": "Food", "description": "Lunch"}
```

**Budget rule**
```json
{"category": "Food", "daily_cap": 80, "monthly_cap": 2400, "pct_threshold": 35}
```

**Config**
```json
{"categories": [...], "currencies": {"HKD": 1.0, "USD": 7.78}, "default_currency": "HKD", "savings_goal": 500, "income": 0}
```

### Run

```bash
pip install -r requirements.txt
python main.py

# Generate test data
python tests/test_generator.py
```

---

## 👥 Team Roles

| Role | Lead | ID |
|------|------|-----|
| **Project Lead & UI Design** | Yang Andi | 3036587092 |
| Algorithm & Logic | Mao Yicheng | 3036483040 |
| Research & Documentation | Tao Xinran | 3036525393 |
| Testing & Evaluation | Wang Ziyi | 3036484020 |
| Data Modeling & File Management | Yao Junzhu | 3036590427 |

---

## ⏱️ Timeline

- **Phase 1** (Mar 15–23): Planning & research ✅
- **Phase 2** (Mar 24–Apr 12): Architecture & implementation 🔄
- **Phase 3** (Apr 13–19): Testing & evaluation
- **Phase 4** (Apr 20–May 2): Final deliverables & reports

---

## 🎯 Tech Stack

- **Language**: Python (text-based)
- **UI**: `rich` (formatted tables, colors, panels) + `questionary` (interactive menu)
- **Data**: JSON files (transactions.json, config.json, budget_rules.json)
- **I/O**: File-based persistence via `json` module

---

## 📌 Key Deliverables

✅ Problem modeling & design justification (5+ trade-offs)  
✅ Research & tool comparison (Goodbudget, YNAB, Spendee, etc.)  
✅ Implementation: Python CLI with transaction management, analytics, alerts  
✅ 3–4 realistic case studies with sample data & evidence  
✅ Final report + individual reports + video demo

---

**Start with**: [GUIDELINES.md](GUIDELINES.md) for the full spec, [UI.md](UI.md) for interface design

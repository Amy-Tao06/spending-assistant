# Feature List

> UI layout and display specs: [UI.md](UI.md)

---

## Must-Have Features

### 1. Transaction Management

**1.1 Add Transaction**  
Prompts for date (YYYY-MM-DD), amount, currency, category, and description. Assigns a unique auto-incrementing ID and saves to `transactions.json` immediately. Currency defaults to HKD; other currencies (CNY, USD, JPY, etc.) show an HKD equivalent inline using current rates.  
Difficulty: Easy

**1.2 Edit and Delete Transactions**  
User selects a transaction by ID from the table, then chooses to edit a specific field or delete the record. Any change re-saves the full list to disk immediately.  
Difficulty: Medium

**1.3 Category Customization**  
Categories live in `config/config.json`, not hardcoded. Users can add or remove categories from a dedicated menu. All features — validation, statistics, alerts — read dynamically from config.  
Difficulty: Medium

---

### 2. Data and File Management

**2.1 Persistent JSON Storage**  
All data (transactions, budget rules, config) is stored in local JSON files. Every add/edit/delete calls `save_transactions()` or `save_budget_rules()` immediately. On startup, `load_transactions()` reads the file into memory as a list of dicts.  
Difficulty: Easy

**2.2 Error Handling for Corrupt or Missing Files**  
`_load_json()` in `data.py` catches `FileNotFoundError` (missing file), `json.JSONDecodeError` (corrupt JSON), and empty file content. In all cases, a safe default is returned and the program continues without crashing. Config merges any missing keys from `DEFAULT_CONFIG` automatically.  
Difficulty: Medium

---

### 3. Interface and Validation

**3.1 Interactive CLI Menu**  
Main menu and all sub-menus use `questionary.select()` with arrow-key navigation — no numbered input. Options are grouped with labelled separators. A custom green style (`#00ff88`) is applied consistently. After each action, `press_any_key_to_continue()` pauses before returning to the menu. `Ctrl+C` exits cleanly at any prompt.

See [UI.md](UI.md) for menu layout and style details.

Difficulty: Easy

**3.2 Input Validation**  
Every text input loops until valid. Dates use `datetime.strptime()`, amounts require `float > 0`, percentages require `0 < x <= 100`, descriptions must be non-empty. Category and currency are always chosen from a `questionary.select()` list, so they can't be invalid. Validation logic is centralized in `validator.py`.

See [UI.md](UI.md) for the full validation table.

Difficulty: Medium

**3.3 View and Filter Transactions**  
Four view modes in a sub-menu: all transactions, filter by date range, filter by category, and keyword search (case-insensitive match on description). Results display as a `rich` table sorted newest-first, with HKD equivalents shown for foreign-currency entries.  
Difficulty: Medium

---

### 4. Statistics and Analytics

**4.1 Spending by Category**  
Groups transactions by category using a `defaultdict`, with optional date filtering. Available for the current month or all time. Displays a `rich` table with inline unicode bar charts and percentage share, color-coded by proportion (green/yellow/red).  
Difficulty: Medium

**4.2 Top-3 Spending Categories**  
Sorts category totals descending and shows the top 3 with medal labels, amounts, and percentage share.  
Difficulty: Easy

**4.3 Spending Trends (7d vs 30d)**  
Computes daily average spend over the last 7 and 30 days. Compares the two and shows the direction and percentage change (e.g., spending 12.6% more this week than the 30-day average).  
Difficulty: Medium

**4.4 Export Summary Report**  
Generates a plain-text `.txt` file in `outputs/` with timestamp in the filename. Covers current month's category totals, 7d/30d trends, top-3 categories, and active alerts. Uses `Console(no_color=True, width=72)` so the file is readable in any editor.  
Difficulty: Medium

---

### 5. Alert System

**5.1 Rule-Based Alerts**  
Reads rules from `budget_rules.json`. Each rule can have a daily cap, monthly cap, and percentage threshold. After every new transaction, the system checks all rules and prints any triggered alerts. Alert types: daily cap exceeded, percentage threshold exceeded, consecutive overspend (3+ days), forecast warning (projected month-end spend exceeds total monthly caps), and uncategorized transactions.

See [UI.md](UI.md) for alert display format.

Difficulty: Medium

**5.2 Consecutive Overspend Detection**  
Checks daily totals for a category going backwards from today. If the daily cap was exceeded for 3 or more consecutive days, a high-priority alert fires.  
Difficulty: Hard

**5.3 Uncategorized Transaction Warnings**  
Scans all transactions for entries with `"Uncategorized"` or a category not in `config.json`. Each match produces a warning with the transaction ID.  
Difficulty: Easy

---

### 6. Testing

**6.1 Test Data Generator**  
`tests/test_generator.py` generates 120 realistic fake transactions with a fixed random seed for reproducibility. Deliberately includes: 5 uncategorized entries (to trigger uncategorized alerts), 1 zero-amount refund (tests edge case handling), and 15 high-value Entertainment entries in the last 5 days (to trigger percentage threshold and consecutive overspend alerts). Also generates matching budget rules and config. Written by Wang Ziyi.  
Difficulty: Medium

---

## Nice-to-Have Features

### Implemented

**P1. Budget Progress Bars** (implemented)  
Daily progress bar per category shown as a unicode bar chart in a `rich` table. Color-coded: green below 80%, yellow 80–99%, red at or above 100%. Shown in the statistics sub-menu and automatically after adding a transaction.

**P2. Keyword Search** (implemented)  
Available as a view mode in "View / Filter Transactions". Case-insensitive search against the description field.

**P3. Multi-Currency Support** (implemented)  
Each transaction stores a currency field. Eight currencies supported: HKD, CNY, USD, JPY, KRW, NTD, GBP, EUR. Exchange rates are stored in `config.json` and displayed as HKD equivalents in all tables.

**P3-ext. Live Exchange Rates** (implemented — extended from P3)  
On startup, `fetch_exchange_rates()` in `data.py` pulls live rates from `open.er-api.com` via `urllib.request` and writes them to `config.json`. Falls back to cached rates silently if offline. Idea by Yang Andi; API suggested by AI; JSON storage approach by Yang Andi.

**P4. Savings Goal Tracker** (implemented)  
Users set monthly income and a savings goal in Settings. The savings view shows income, total spent, remaining, and a progress bar toward the goal with a status message.

**P6. Spending Forecast** (implemented)  
Extrapolates this month's total from the daily average so far using linear scaling (`spent / days_elapsed * days_in_month`). Displayed in the statistics sub-menu and used to generate forecast-based alerts.

**P7. Spending Heatmap** (implemented)  
Calendar grid for the current month (Mon–Sun columns). Each day shows a unicode block symbol (░▒▓█) based on spending relative to the month's daily average. Implemented in `analytics.py` (`spending_heatmap`) and rendered in `display.py` (`print_heatmap`).

**P8. Major Expense Outliers** (implemented — not originally planned)  
Shows the top 5% of transactions by amount. Implemented by Mao Yicheng (`print_outliers` in `display.py`, `get_spending_outliers` in `analytics.py`).

### Not Implemented

**P5. Recurring Transactions**  
Flagging transactions as recurring and auto-logging them on startup. Descoped — adds significant complexity and the subscription creep case study is covered via the alert system and test data instead.

---

## Features to Avoid

- GUI or web dashboard — out of scope; text CLI is required.
- Live bank/API syncing for transactions — explicitly excluded by project guidelines.
- Machine learning or complex statistical models — beyond course level; linear extrapolation is sufficient.

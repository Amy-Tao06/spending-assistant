# Personal Budget & Spending Assistant — Complete Documentation

**Course**: COMP1110 B12, HKU 2026  
**Language**: Python 3.x  
**Dependencies**: `rich==13.7.0`, `questionary==1.10.0`

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation & Setup](#installation--setup)
3. [How to Use All Features](#how-to-use-all-features)
4. [Function Documentation](#function-documentation)
5. [Data Models](#data-models)
6. [Module Dependency Map](#module-dependency-map)

---

## Project Overview

The **Personal Budget & Spending Assistant** is an interactive CLI tool for tracking expenses across multiple currencies, setting budget rules, viewing analytics, and receiving spending alerts.

### Purpose
- Record and organize spending by category
- Track spending patterns and trends (7-day, 30-day averages)
- Set and monitor budget constraints (daily caps, monthly caps, category % limits)
- Export spending reports to plain text
- Support multi-currency transactions with live exchange rates

### Tech Stack
- **UI**: `rich` (formatted terminal tables, panels, progress bars, colors)
- **Interaction**: `questionary` (menu selection, prompts, confirmations)
- **Data Storage**: JSON files (transactions, budget rules, config)
- **API**: `open.er-api.com` (live exchange rates)
- **Language**: Python 3.x (no NumPy, pandas, or async)

### Project Structure

```
comp1110projectlocal/
├── main.py                    Main CLI loop & menu orchestration
├── display.py                 All Rich rendering & report export
├── analytics.py               Statistical calculations, trends, forecasting
├── alerts.py                  Budget rule enforcement & alert logic
├── data.py                    File I/O (transactions, rules, config)
├── validator.py               Input validation (dates, amounts, descriptions)
├── config/
│   └── config.json            Categories, currencies, income, savings goal
├── data/
│   ├── transactions.json      Transaction ledger
│   └── budget_rules.json      Budget rules (daily/monthly caps, thresholds)
├── outputs/                   Generated text reports
├── tests/
│   └── test_generator.py      Test data generator (120 transactions + 5 rules)
└── requirements.txt           Dependencies list
```

---

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python main.py
```

The first run will:
- Create `data/`, `config/`, and `outputs/` directories
- Initialize `config/config.json` with default categories and exchange rates
- Attempt to fetch live exchange rates from `open.er-api.com` (optional; falls back to hardcoded defaults on failure)

### 3. Generate Test Data (Optional)
```bash
python tests/test_generator.py
```

This creates:
- 120 realistic transactions in `data/transactions.json` (0–30 days ago)
- 5 sample budget rules in `data/budget_rules.json`
- Edge cases baked in: uncategorized transactions (IDs 1–5), recent spending spikes (IDs 106–120)

---

## How to Use All Features

### Main Menu
On startup, the app displays a cyan header panel and presents the main menu. Use arrow keys to navigate, Enter to select.

---

### Feature 1: Add a Transaction

**Menu**: Select `"Add Transaction"`

**Steps**:
1. **Date** — Enter in `YYYY-MM-DD` format (auto-validates; defaults to today if you press Enter with no input)
2. **Amount** — Enter a positive number (e.g., `50.5`; decimals allowed; auto-validates as positive)
3. **Currency** — Select from the currency list (HKD, CNY, JPY, KRW, NTD, USD, GBP, EUR)
4. **Category** — Select from the available categories or choose `"Uncategorized"`
5. **Description** — Enter a short note (e.g., "Lunch at Causeway Bay"; cannot be empty or whitespace)

**Output**: Transaction saved with an auto-assigned ID. The app then:
- Displays alerts (if any budget rules are violated)
- Shows today's budget progress bars
- Returns to the main menu

**Currency Note**: Amounts are stored in the transaction's native currency but are automatically converted to HKD using live exchange rates when displayed.

---

### Feature 2: View Transactions

**Menu**: Select `"View Transactions"` → Choose a sub-option

#### 2a. All Transactions
Displays a table sorted by date (newest first) with columns: ID, Date, Amount (in HKD with original currency shown), Category, Description.

#### 2b. Filter by Date Range
Prompts for:
- **Start Date** (YYYY-MM-DD; optional, defaults to 30 days ago)
- **End Date** (YYYY-MM-DD; optional, defaults to today)

Displays only transactions falling in `[start, end]` (inclusive on both bounds).

#### 2c. Filter by Category
Select a category from the list. Displays only transactions in that category.

#### 2d. Search by Keyword
Enter a keyword. The app performs a case-insensitive substring match on transaction descriptions.

---

### Feature 3: Edit or Delete a Transaction

**Menu**: Select `"Edit / Delete Transaction"`

**Steps**:
1. The app displays all transactions in a table
2. Prompts for a transaction **ID** to modify
3. Offers two options:
   - **Edit a Field** — Select which field to change (date, amount, currency, category, or description). Enter the new value; it will be re-validated.
   - **Delete Transaction** — Confirm before deletion

After any change, the transaction file is saved and the app returns to the main menu.

---

### Feature 4: View Statistics

**Menu**: Select `"View Statistics"` → Choose a sub-option

#### 4a. Category Totals
Sub-menu allows:
- **All Time** — Sum all transactions by category
- **Current Month** — Sum only this month's transactions by category

Displays a table with columns: Category, Amount (HKD), ASCII bar graph (20 chars, color-coded), % of total.
- Green bar: category is <30% of total
- Yellow bar: 30–50% of total
- Red bar: >50% of total

#### 4b. Top 3 Categories
Shows the top 3 categories by spending with medal icons (🥇 Gold, 🥈 Silver, 🥉 Bronze), amounts, and percentages.

#### 4c. Spending Trends
Displays a table showing:
- **7-day average** — Daily average over the last 7 days (HKD/day)
- **30-day average** — Daily average over the last 30 days (HKD/day)
- **Trend indicator** — Red ↑ if recent spend is higher than the 30-day baseline; Green ↓ if lower

#### 4d. Budget Progress Bars
For each budget rule with a daily cap, shows today's spending vs. the limit in a colored progress bar:
- Green: <80% of cap
- Yellow: 80–99% of cap
- Red: ≥100% of cap

(Shows nothing if no budget rules exist.)

#### 4e. Spending Forecast
Extrapolates end-of-month total using linear regression on spending so far this month. Shows:
- Days of data in the calculation
- Projected month-end total (HKD)

(Returns 0 if no transactions this month.)

#### 4f. Spending Heatmap
Displays a visual calendar grid (Monday–Sunday) for the current month. Each day cell shows:
- A Unicode block symbol (░ ▒ ▓ █) color-coded by spending intensity
- Relative to that month's daily average:
  - `░` (dim) = <50% of average (low)
  - `▒` (green) = 50–99% of average (medium)
  - `▓` (yellow) = 100–149% of average (high)
  - `█` (red) = ≥150% of average (very high)

A legend appears at the bottom.

---

### Feature 5: View Alerts

**Menu**: Select `"View Alerts"`

The app scans all transactions and rules, then displays four types of alerts (if triggered):

1. **Daily Exceeded** (🔴 Red) — Today's spending in a category exceeded its daily cap
2. **Percentage Exceeded** (🔴 Red) — A category's all-time share of total spending exceeded its % threshold
3. **Consecutive Overspend** (🔴 Red) — A category exceeded its daily cap for 3+ consecutive days
4. **Uncategorized** (🟡 Yellow) — A transaction's category is invalid or literally "Uncategorized"

If no alerts are triggered, a green "All clear" panel appears.

---

### Feature 6: Manage Budget Rules

**Menu**: Select `"Manage Budget Rules"` → Choose a sub-option

Budget rules are constraints on spending by category. Each rule can have:
- **Daily Cap** (HKD) — Maximum allowed per day
- **Monthly Cap** (HKD) — Maximum allowed per calendar month
- **Percentage Threshold** (%) — Maximum allowed as a % of total all-time spending

#### 6a. View Budget Rules
Displays a table with columns: Category, Daily Cap, Monthly Cap, % Threshold (or `"—"` if not set).

#### 6b. Add or Update a Rule
1. Select a category
2. For each constraint (daily cap, monthly cap, % threshold), you're prompted to:
   - Enter a value (or press Enter to skip / not set that constraint)
3. The rule is saved (or updated if it already exists for that category)

#### 6c. Delete a Rule
Select a category, confirm deletion. The rule is removed from the file.

---

### Feature 7: Manage Categories

**Menu**: Select `"Manage Categories"` → Choose a sub-option

#### 7a. View Categories
Lists all currently available categories.

#### 7b. Add a Category
Enter a new category name (non-empty, no duplicates). It's added to the config and available immediately in the "Add Transaction" flow.

#### 7c. Remove a Category
Select a category from the list, confirm deletion. Existing transactions in that category remain (though they may trigger "Uncategorized" alerts).

---

### Feature 8: Settings

**Menu**: Select `"Settings"` → Choose a sub-option

#### 8a. Set Monthly Income
Enter your expected monthly income (HKD, positive). This is used to calculate savings progress (remaining budget = income − spent).

#### 8b. Set Savings Goal
Enter your target monthly savings (HKD, positive). Savings are calculated as: `remaining − savings_goal`.

#### 8c. View Savings Progress
Displays a progress bar showing:
- Spent (HKD) in the current month
- Remaining budget after spending
- Savings (remaining − goal)

**Requires**: Both income and savings goal must be set (>0). If not, a prompt appears to set them first.

#### 8d. Currency Exchange Rates
Displays a table of all exchange rates (currency name → HKD). On startup, the app fetches live rates from `open.er-api.com`. You can manually update a single rate here if needed (e.g., for offline testing).

---

### Feature 9: Export Report

**Menu**: Select `"Export Report"`

Generates a plain-text file to `outputs/report_YYYY-MM-DD_HHMMSS.txt` containing:
1. **Current Month Spending by Category** — A summary table
2. **Spending Trends** — 7-day and 30-day averages with trend arrows
3. **Top 3 Categories** — With amounts and percentages
4. **Active Alerts** — All triggered budget alerts (if any)

The file is saved with no color codes (plain text) and the app displays the file path.

---

## Function Documentation

### Module: `validator.py`

Pure validation functions. Return `True`/`False` or tuples indicating success.

#### `validate_date(date_str: str) -> bool`
- **Input**: A string (possibly empty)
- **Returns**: `True` if the string is non-empty and parses as `YYYY-MM-DD`; `False` otherwise
- **Validation**: Checks for exact ISO 8601 date format using `datetime.strptime()`
- **Used by**: Add Transaction flow (date input)

#### `validate_amount(amount_str: str) -> tuple[bool, float]`
- **Input**: A string (possibly empty)
- **Returns**: `(True, amount)` if the string is non-empty, numeric, and strictly positive; otherwise `(False, 0.0)`
- **Validation**: Converts to float; must be > 0
- **Used by**: Add Transaction flow, Edit Transaction (amount field)

#### `validate_category(category: str, categories: list) -> bool`
- **Input**: A category name and list of valid categories
- **Returns**: `True` if the category is in the list; `False` otherwise
- **Validation**: Simple membership check
- **Used by**: Add Transaction flow (validates user's category selection)

#### `validate_description(desc: str) -> bool`
- **Input**: A string (possibly empty or whitespace)
- **Returns**: `True` if non-empty and non-whitespace; `False` otherwise
- **Validation**: `bool(desc and desc.strip())`
- **Used by**: Add Transaction flow (description input)

---

### Module: `data.py`

File I/O, configuration management, and API integration.

#### Constants

| Name | Value |
|------|-------|
| `DATA_DIR` | `"data"` |
| `CONFIG_DIR` | `"config"` |
| `OUTPUTS_DIR` | `"outputs"` |
| `TRANSACTIONS_FILE` | `"data/transactions.json"` |
| `BUDGET_RULES_FILE` | `"data/budget_rules.json"` |
| `CONFIG_FILE` | `"config/config.json"` |

#### `fetch_exchange_rates() -> dict | None`
- **Purpose**: Fetch live currency exchange rates from `open.er-api.com`
- **Input**: None
- **Returns**: A dict `{currency_name: rate_in_hkd}` on success, or `None` on failure
- **Details**:
  - Calls `https://open.er-api.com/v6/latest/HKD` with a 5-second timeout
  - Converts rates from "HKD per 1 foreign unit" to internal format
  - Maps ISO codes (TWD, KRW, etc.) to app internal names (NTD, KRW, etc.)
  - Returns `None` on network error, timeout, or parse error
- **Used by**: `main.py` on startup (updates config with live rates)

#### `ensure_dirs() -> None`
- **Purpose**: Create required directories if they don't exist
- **Input**: None
- **Returns**: None
- **Details**: Creates `data/`, `config/`, and `outputs/` using `os.makedirs(..., exist_ok=True)`
- **Used by**: `main.py` on startup

#### `_load_json(filepath: str, default: any) -> any` (private)
- **Purpose**: Load and parse a JSON file with graceful fallback
- **Input**: File path and default value
- **Returns**: Parsed JSON content on success, or `default` if file missing / unparseable
- **Details**: Prints a warning if JSON parse fails
- **Used by**: Transaction/rule/config loaders (internal helper)

#### `_save_json(filepath: str, data: any) -> None` (private)
- **Purpose**: Serialize and save data to a JSON file
- **Input**: File path and data (list or dict)
- **Returns**: None
- **Details**: Writes with 2-space indentation for human readability
- **Used by**: Transaction/rule/config savers (internal helper)

#### `load_transactions() -> list`
- **Purpose**: Load all transactions from disk
- **Input**: None
- **Returns**: List of transaction dicts, or empty list if file missing
- **Used by**: All flows that read transactions

#### `save_transactions(transactions: list) -> None`
- **Purpose**: Save transactions to disk
- **Input**: List of transaction dicts
- **Returns**: None
- **Used by**: All flows that modify transactions

#### `load_budget_rules() -> list`
- **Purpose**: Load all budget rules from disk
- **Input**: None
- **Returns**: List of rule dicts, or empty list if file missing
- **Used by**: All flows that read rules

#### `save_budget_rules(rules: list) -> None`
- **Purpose**: Save budget rules to disk
- **Input**: List of rule dicts
- **Returns**: None
- **Used by**: All flows that modify rules

#### `load_config() -> dict`
- **Purpose**: Load app configuration from disk with fallback to defaults
- **Input**: None
- **Returns**: Complete config dict (always includes all required keys)
- **Details**: Loads from file, then merges in any missing keys from `DEFAULT_CONFIG` (ensures robustness)
- **Used by**: All flows that need config (categories, currencies, income, savings goal)

#### `save_config(config: dict) -> None`
- **Purpose**: Save app configuration to disk
- **Input**: Config dict
- **Returns**: None
- **Used by**: Settings flows (income, savings goal, currencies)

#### `get_next_id(transactions: list) -> int`
- **Purpose**: Generate the next unique transaction ID
- **Input**: List of existing transactions
- **Returns**: `max(t["id"] for t in transactions) + 1`, or `1` if list is empty
- **Ensures**: Monotonically increasing IDs
- **Used by**: Add Transaction flow

---

### Module: `analytics.py`

Pure statistical calculation. No file I/O or UI. All dates work with `datetime` objects.

#### `parse_date(date_str: str) -> datetime`
- **Purpose**: Convert an ISO date string to a datetime object
- **Input**: String in `YYYY-MM-DD` format
- **Returns**: `datetime` object
- **Used by**: Filtering and trend functions

#### `filter_by_date(transactions: list, start: datetime = None, end: datetime = None) -> list`
- **Purpose**: Filter transactions by date range
- **Input**: Transaction list, optional start and end datetimes
- **Returns**: Subset of transactions with dates in `[start, end]` (both bounds inclusive)
- **Details**: `None` for start/end means no lower/upper bound
- **Used by**: View Transactions (date range filter)

#### `get_totals_by_category(transactions: list, start: datetime = None, end: datetime = None) -> dict`
- **Purpose**: Sum spending by category
- **Input**: Transaction list, optional date range
- **Returns**: `{category: total_amount_hkd}`
- **Details**: First filters by date, then groups by category
- **Used by**: Statistics (category totals display)

#### `get_top_n_categories(transactions: list, n: int = 3, start: datetime = None, end: datetime = None) -> list[tuple]`
- **Purpose**: Identify top N spending categories
- **Input**: Transaction list, number of categories, optional date range
- **Returns**: List of tuples `[(category, amount, percentage_of_total), ...]` sorted descending by amount
- **Details**: Returns up to `n` categories; returns fewer if fewer categories exist
- **Used by**: Statistics (top 3 display)

#### `get_spending_trends(transactions: list) -> tuple[float, float]`
- **Purpose**: Calculate short-term and medium-term spending averages
- **Input**: Transaction list
- **Returns**: `(avg_7_day, avg_30_day)` — daily averages in HKD per day
- **Details**:
  - Filters transactions to last 7 and 30 days respectively
  - Calculates total ÷ number of days in each window
  - Returns `0.0` if no transactions in a window
- **Used by**: Statistics (trends display)

#### `get_daily_totals_by_category(transactions: list, category: str) -> dict`
- **Purpose**: Sum spending per date for a single category
- **Input**: Transaction list, category name
- **Returns**: `{date_str: total_amount_hkd}` for that category
- **Used by**: Alerts (consecutive overspend check), display (if needed)

#### `get_consecutive_overspend(transactions: list, category: str, daily_cap: float) -> int`
- **Purpose**: Count how many consecutive days a category exceeded its cap
- **Input**: Transaction list, category, daily cap in HKD
- **Returns**: Integer count of consecutive days (most recent backward) exceeding the cap
- **Details**: Works backward from today; stops at first day under the cap
- **Used by**: Alerts (consecutive overspend alert)

#### `get_savings_progress(transactions: list, savings_goal: float, income: float) -> tuple[float, float, float]`
- **Purpose**: Calculate monthly savings metrics
- **Input**: Transaction list, monthly savings goal, monthly income (both HKD)
- **Returns**: `(spent, remaining, savings)`
  - `spent` — total spent in current month
  - `remaining` — income − spent
  - `savings` — remaining − goal
- **Details**: Filters to current calendar month only
- **Used by**: Statistics (savings progress display)

#### `linear_forecast(transactions: list) -> float`
- **Purpose**: Project end-of-month spending
- **Input**: Transaction list
- **Returns**: Extrapolated month-end total in HKD
- **Calculation**: `(spent_so_far / days_elapsed) × days_in_month`
- **Details**: Returns `0.0` if no transactions this month
- **Used by**: Statistics (forecast display)

#### `spending_heatmap(transactions: list) -> dict`
- **Purpose**: Generate a day-by-day intensity heatmap for the current month
- **Input**: Transaction list
- **Returns**: `{date_str: (symbol, amount)}`
  - `symbol` is one of `"░"`, `"▒"`, `"▓"`, `"█"` based on spending level
  - `amount` is the HKD total for that day
- **Details**:
  - Computes daily totals for the current month
  - Calculates the month's average daily spending
  - Maps each day to a symbol:
    - `░` = <50% of average (low)
    - `▒` = 50–99% of average (medium)
    - `▓` = 100–149% of average (high)
    - `█` = ≥150% of average (very high)
  - Days with no spending are omitted
- **Used by**: Statistics (heatmap display)

---

### Module: `alerts.py`

Budget rule enforcement. Generates alert dictionaries consumed by `display.py`.

#### Alert Dictionary Schema

All alerts share a `type` and `message` key. Specific types have additional fields:

| `type` | Extra Fields | Meaning |
|--------|-------------|---------|
| `"daily_exceeded"` | `category`, `spent`, `cap` | Today's spending in this category exceeded the daily cap |
| `"pct_exceeded"` | `category`, `pct`, `threshold` | Category's % of all-time total exceeded threshold |
| `"consecutive_overspend"` | `category`, `streak` | Daily cap exceeded 3+ consecutive days |
| `"uncategorized"` | `id`, `category` | Transaction has an invalid or "Uncategorized" category |

#### `check_daily_caps(transactions: list, budget_rules: list) -> list`
- **Purpose**: Alert if today's spending exceeded any daily cap
- **Input**: Transaction list and budget rules
- **Returns**: List of `"daily_exceeded"` alert dicts (one per rule violated today)
- **Details**: Filters transactions to today, sums by category, compares to cap
- **Used by**: Main menu after adding a transaction

#### `check_percentage_thresholds(transactions: list, budget_rules: list) -> list`
- **Purpose**: Alert if a category's all-time share exceeded a threshold
- **Input**: Transaction list and budget rules
- **Returns**: List of `"pct_exceeded"` alert dicts
- **Details**: Computes each category's % of total all-time spending; skips if total is zero
- **Used by**: Alerts menu, export report

#### `check_consecutive_overspend(transactions: list, budget_rules: list) -> list`
- **Purpose**: Alert if a category exceeded its daily cap 3+ days in a row
- **Input**: Transaction list and budget rules
- **Returns**: List of `"consecutive_overspend"` alert dicts
- **Details**: Calls `get_consecutive_overspend()` for each rule; alerts if streak ≥ 3
- **Used by**: Alerts menu

#### `check_uncategorized(transactions: list, categories: list) -> list`
- **Purpose**: Alert for any transaction with an invalid or "Uncategorized" category
- **Input**: Transaction list and known categories list
- **Returns**: List of `"uncategorized"` alert dicts (one per bad transaction)
- **Details**: Checks if `transaction["category"]` is either literally `"Uncategorized"` or not in the categories list
- **Used by**: Alerts menu, export report

#### `get_all_alerts(transactions: list, budget_rules: list, categories: list) -> list`
- **Purpose**: Aggregate all alert types
- **Input**: Transaction list, budget rules, categories
- **Returns**: Combined list of all alerts from the four check functions (in order: daily caps, pct thresholds, consecutive overspend, uncategorized)
- **Used by**: Alerts menu, add transaction flow

---

### Module: `display.py`

All terminal rendering using `rich`. Receives data from analytics/alerts; no business logic.

#### Module-level

`console = Console()` — Single shared `rich.Console` instance for all rendering.

#### `print_header() -> None`
- **Purpose**: Render the app title/header
- **Output**: A cyan panel with app title ("Personal Budget Assistant") and course info (COMP1110 B12, HKU, 2026)
- **Used by**: Main menu at each loop iteration

#### `print_transaction_table(transactions: list, title: str = "Transaction History") -> None`
- **Purpose**: Render a table of transactions
- **Input**: List of transactions and optional table title
- **Output**: A `ROUNDED` box table sorted by date (newest first) with columns: ID, Date, Amount (HKD + original currency), Category, Description
  - For non-HKD amounts, shows: `"CUR X.XX ≈ HK$Y.YY"`
  - Empty state: dim panel saying "No transactions found"
- **Used by**: View Transactions flow

#### `print_statistics(transactions: list, period_label: str = "All Time") -> None`
- **Purpose**: Render category breakdown
- **Input**: Transaction list and period label (e.g., "Current Month", "All Time")
- **Output**: A table with columns: Category, Amount, ASCII bar (20 chars), %
  - Bar color: green (<30%), yellow (30–50%), red (>50%)
  - Total shown below
- **Used by**: Statistics (category totals)

#### `print_top_categories(transactions: list, n: int = 3) -> None`
- **Purpose**: Render top-N categories with icons
- **Input**: Transaction list and count
- **Output**: A list with medal icons (🥇 🥈 🥉), amounts, and percentages
- **Used by**: Statistics (top 3)

#### `print_trends(transactions: list) -> None`
- **Purpose**: Render spending trend indicators
- **Input**: Transaction list
- **Output**: A two-row table showing 7-day and 30-day daily averages with trend arrows
  - Red ↑ = recent avg > 30-day avg
  - Green ↓ = recent avg < 30-day avg
- **Used by**: Statistics (trends)

#### `print_alerts(alerts: list) -> None`
- **Purpose**: Render all budget alerts
- **Input**: List of alert dicts
- **Output**:
  - If alerts exist: red-bordered panel with each alert listed
    - Red circle (🔴) for daily/pct/consecutive alerts
    - Yellow circle (🟡) for uncategorized
  - If empty: green "All clear" panel
- **Used by**: Alerts menu, add transaction flow

#### `print_budget_bars(transactions: list, budget_rules: list) -> None`
- **Purpose**: Render today's progress vs. daily caps
- **Input**: Transaction list and budget rules
- **Output**: One 20-char progress bar per rule with daily cap
  - Green (<80%), yellow (80–99%), red (≥100%)
  - Shows nothing if no rules
- **Used by**: Add transaction flow, statistics menu

#### `print_budget_rules(budget_rules: list) -> None`
- **Purpose**: Render the list of all budget rules
- **Input**: Budget rules list
- **Output**: A `ROUNDED` table with columns: Category, Daily Cap, Monthly Cap, % Threshold
  - `"—"` for unset constraints
- **Used by**: Manage Budget Rules (view)

#### `print_savings_goal(transactions: list, config: dict) -> None`
- **Purpose**: Render monthly savings progress
- **Input**: Transaction list and config (with income and savings_goal)
- **Output**:
  - If income and savings_goal are both > 0: progress bar + status message (e.g., "On track" / "Behind")
  - Otherwise: dim prompt to set both values first
- **Used by**: Statistics (savings) and Settings (view savings)

#### `print_forecast(transactions: list) -> None`
- **Purpose**: Render month-end spending forecast
- **Input**: Transaction list
- **Output**: A small table showing days of data and projected month-end total
- **Used by**: Statistics (forecast)

#### `print_heatmap(transactions: list) -> None`
- **Purpose**: Render a calendar-style spending intensity heatmap
- **Input**: Transaction list
- **Output**: A Monday–Sunday grid for the current month with heatmap symbols (░ ▒ ▓ █) color-coded by intensity
  - Includes a legend line
- **Used by**: Statistics (heatmap)

#### `export_report(transactions: list, budget_rules: list, categories: list, config: dict, filename: str = None) -> str`
- **Purpose**: Export a plain-text spending report to disk
- **Input**: Transaction list, budget rules, categories, config, optional filename override
- **Output**:
  - Writes to `outputs/report_YYYY-MM-DD_HHMMSS.txt` (or custom filename)
  - Content (plain text, no color codes):
    1. Current month spending by category
    2. Spending trends (7d/30d averages + % change)
    3. Top 3 categories
    4. Active alerts
  - Returns the filename written
- **Used by**: Export Report flow

---

### Module: `main.py`

The entry point. Defines the CLI menu loop and orchestrates all flows.

#### Helper UI Primitives

**`_sep(label: str = "") -> Separator`**
- **Purpose**: Create a visual divider for use in menus
- **Input**: Optional label text
- **Returns**: A `questionary.Separator`
- **Output**: `"── Label "` with label, or 44 dashes without

**`ask(prompt: str, default: str = "") -> str`**
- **Purpose**: Prompt for text input
- **Input**: Prompt text and optional default value
- **Returns**: The user's input string
- **Raises**: `KeyboardInterrupt` if the user cancels
- **Details**: Wraps `questionary.text()` with project styling

**`choose(prompt: str, choices: list) -> str`**
- **Purpose**: Prompt for a single-choice selection
- **Input**: Prompt text and list of choices
- **Returns**: The selected choice string
- **Raises**: `KeyboardInterrupt` if the user cancels
- **Details**: Uses `questionary.select()` with `"❯"` pointer

**`confirm(prompt: str, default: bool = False) -> bool`**
- **Purpose**: Prompt for a yes/no confirmation
- **Input**: Prompt text and default value
- **Returns**: `True` for yes, `False` for no
- **Raises**: `KeyboardInterrupt` if the user cancels
- **Details**: Wraps `questionary.confirm()`

**`pause() -> None`**
- **Purpose**: Hold the screen until the user presses any key
- **Input**: None
- **Returns**: None
- **Details**: Calls `questionary.press_any_key_to_continue()`

#### Flow Functions (Menu Handlers)

Each flow is a function that handles one menu option. They all follow the same pattern: load data, validate user input, modify, save, display results, pause.

**`add_transaction_flow() -> None`**
- Prompts for date (defaults to today), amount (validated positive), currency, category, description
- Builds a transaction dict with a new auto-assigned ID
- Appends to the transactions list and saves
- Displays any triggered alerts and today's budget progress bars

**`view_transactions_flow() -> None`**
- Sub-menu:
  - "All Transactions" — display all
  - "Filter by Date Range" — prompts for start/end dates (validated), filters, displays
  - "Filter by Category" — select category, filters, displays
  - "Search by Keyword" — enter keyword, case-insensitive substring match on description, displays

**`edit_delete_flow() -> None`**
- Displays the transaction table, prompts for an ID
- Offers "Edit a Field" or "Delete"
  - Edit: select field (date, amount, currency, category, description), enter new value (re-validated), save
  - Delete: confirm, remove from list, save

**`statistics_flow() -> None`**
- Sub-menu offering:
  - Category Totals (current month or all time)
  - Top 3 Categories
  - Spending Trends
  - Budget Progress Bars
  - Spending Forecast
  - Spending Heatmap

**`alerts_flow() -> None`**
- Loads transactions, budget rules, config, calls `get_all_alerts()`, displays results

**`manage_budget_rules_flow() -> None`**
- Sub-menu:
  - View: display rules table
  - Add/Update: select category, optionally set daily cap / monthly cap / pct threshold, upsert rule, save
  - Delete: select category, confirm, remove, save

**`manage_categories_flow() -> None`**
- Sub-menu:
  - View: list all categories
  - Add: validate non-empty, check no duplicate, append, save
  - Remove: select from list, confirm, remove from list, save

**`settings_flow() -> None`**
- Sub-menu:
  - Set Monthly Income: validate positive, save to config
  - Set Savings Goal: validate positive, save to config
  - View Savings Progress: display via `print_savings_goal()`
  - Currency Exchange Rates: display table, option to manually update a single rate

**`export_flow() -> None`**
- Calls `export_report()`, prints the output file path

#### Application Entry Point

**`main() -> None`**
- On startup:
  1. Calls `ensure_dirs()` to create data/config/outputs directories
  2. Attempts `fetch_exchange_rates()` (updates config on success; falls back on failure)
  3. Enters the main menu loop:
     - Clears screen
     - Prints header panel
     - Displays main menu via `questionary.select()`
     - Dispatches to the appropriate handler
     - Calls `pause()`
- Handles `KeyboardInterrupt` gracefully with a goodbye message
- The menu loop repeats until the user chooses "Exit"

---

### Module: `tests/test_generator.py`

Generates realistic test data for testing and demo purposes.

#### `rand_amount(cat: str) -> float`
- **Purpose**: Generate a realistic random amount for a category
- **Input**: Category name
- **Returns**: A float (1 decimal place) from the per-category range
- **Details**: E.g., Food might be 10–100, Transport 5–50, based on `AMOUNT_RANGES` dict

#### `generate_transactions(n: int = 120) -> list`
- **Purpose**: Generate `n` synthetic transaction dicts
- **Input**: Number of transactions (default 120)
- **Returns**: A list sorted by date ascending
- **Details**:
  - Each has a random date from 0–30 days ago
  - Realistic category/description pairs (e.g., "Lunch at Causeway Bay" for Food)
  - Random amounts from `rand_amount()`
  - Edge cases:
    - IDs 1–5: category set to `"Uncategorized"` (to test uncategorized alerts)
    - IDs 106–120: category set to `"Entertainment"` with high amounts (to test recent spending spikes)
- **Deterministic**: Uses a fixed seed for reproducibility

#### `generate_budget_rules() -> list`
- **Purpose**: Generate a hardcoded set of sample budget rules
- **Input**: None
- **Returns**: A list of 5 rule dicts (Food, Transport, Entertainment, Personal, Health)
- **Details**: Each has daily cap, monthly cap, and pct threshold suitable for testing

#### `main() -> None`
- **Purpose**: Entry point for the test generator
- **Input**: None
- **Returns**: None
- **Behavior**:
  - Calls `generate_transactions()` and `generate_budget_rules()`
  - Writes to `data/transactions.json` and `data/budget_rules.json`
  - Prints a summary including the edge cases included

**Usage**:
```bash
python tests/test_generator.py
```

---

## Data Models

### `data/transactions.json`

A JSON array of transaction objects.

#### Schema
```json
[
  {
    "id": 1,
    "date": "2026-04-01",
    "amount": 50.5,
    "currency": "HKD",
    "category": "Food",
    "description": "Lunch"
  },
  ...
]
```

#### Field Descriptions

| Field | Type | Constraints | Meaning |
|-------|------|-------------|---------|
| `id` | int | Auto-incremented, unique | Unique transaction ID (always > 0) |
| `date` | string | ISO 8601 YYYY-MM-DD format | Transaction date |
| `amount` | float | Positive (> 0) | Spending amount in the transaction's native currency |
| `currency` | string | Key in `config["currencies"]` | Currency code (HKD, CNY, JPY, etc.) |
| `category` | string | In `config["categories"]` or `"Uncategorized"` | Spending category |
| `description` | string | Non-empty, non-whitespace | Short description of the transaction |

#### Notes
- **Currency**: Amounts are stored in the transaction's native currency. The display layer converts to HKD on-the-fly using exchange rates from `config.json`.
- **ID Generation**: Always auto-assigned by `get_next_id()` when adding. Never edited; only increased.

---

### `data/budget_rules.json`

A JSON array of budget rule objects. Each rule constrains spending for one category.

#### Schema
```json
[
  {
    "category": "Food",
    "daily_cap": 399.0,
    "monthly_cap": 2400.0,
    "pct_threshold": 35
  },
  ...
]
```

#### Field Descriptions

| Field | Type | Constraints | Meaning |
|-------|------|-------------|---------|
| `category` | string | Must match a key in `config["categories"]` | Spending category to constrain |
| `daily_cap` | float | Optional; positive if set | Maximum HKD spend per calendar day |
| `monthly_cap` | float | Optional; positive if set | Maximum HKD spend per calendar month |
| `pct_threshold` | float | Optional; 0–100 if set | Max allowed % of all-time total spend |

#### Notes
- **One per category**: At most one rule per category. Adding a rule to a category that already has a rule updates it.
- **Optional fields**: All three constraint fields are optional. A rule can have any combination (e.g., only a daily cap, or only a pct threshold).
- **Validation**: Alerts are triggered when any constraint is breached:
  - `daily_cap`: Checked daily; alerts if today's total exceeds it
  - `monthly_cap`: Checked monthly; alerts if current month's total exceeds it
  - `pct_threshold`: Checked against all-time spending; alerts if the category's share exceeds the threshold

---

### `config/config.json`

A single JSON object containing app-wide settings.

#### Schema
```json
{
  "categories": ["Food", "Transport", "Personal", "Entertainment", "Health", "Utilities"],
  "currencies": {
    "HKD": 1.0,
    "CNY": 1.144452,
    "JPY": 0.0491,
    "KRW": 0.005275,
    "NTD": 0.247038,
    "USD": 7.830854,
    "GBP": 10.548634,
    "EUR": 9.179281
  },
  "default_currency": "HKD",
  "savings_goal": 500.0,
  "income": 0.0
}
```

#### Field Descriptions

| Field | Type | Constraints | Meaning |
|-------|------|-------------|---------|
| `categories` | array of strings | Non-empty list, no duplicates | Available spending categories |
| `currencies` | object | Keys are currency names; values are floats > 0 | Exchange rates: `1 unit = X HKD` |
| `default_currency` | string | Must be a key in `currencies` | Default currency for new transactions |
| `savings_goal` | float | ≥ 0 | Monthly savings target in HKD |
| `income` | float | ≥ 0 | Monthly income in HKD (0 = not set) |

#### Exchange Rate Convention
- All rates are stored as: **1 unit of that currency = X HKD**
- Example: `"CNY": 1.144452` means 1 CNY = 1.144452 HKD (or 1 HKD = ~0.87 CNY)
- Conversion formula: `amount_in_hkd = amount_in_currency × rate`
- Rates are fetched live from `open.er-api.com` on startup and cached in the config file

#### Notes
- **Default values**: If a key is missing, `load_config()` fills it in from `DEFAULT_CONFIG`
- **Savings goal & income**: Both must be > 0 to enable savings progress calculations
- **Currency list**: Can be extended by adding new entries to the `currencies` object and the `categories` list

---

## Module Dependency Map

### Direct Dependencies

```
main.py (orchestration)
  ├─→ data.py
  │   └─ load_transactions, save_transactions
  │   └─ load_budget_rules, save_budget_rules
  │   └─ load_config, save_config
  │   └─ fetch_exchange_rates, ensure_dirs, get_next_id
  │
  ├─→ validator.py
  │   └─ validate_date, validate_amount, validate_category, validate_description
  │
  ├─→ analytics.py
  │   └─ filter_by_date, get_totals_by_category, get_consecutive_overspend, etc.
  │
  ├─→ alerts.py
  │   └─ get_all_alerts
  │
  └─→ display.py (all print_* and export_report)
      ├─→ analytics.py
      │   └─ (all stats functions)
      └─→ alerts.py
          └─ (get_all_alerts for export)

display.py
  └─→ analytics.py
      └─ All statistical calculations

alerts.py
  └─→ analytics.py
      └─ get_consecutive_overspend, get_daily_totals_by_category, etc.
```

### Function Call Flow Example: Add Transaction

1. `main()` → `add_transaction_flow()`
2. Prompt user for inputs (date, amount, currency, category, description)
3. `validator.py` → `validate_date()`, `validate_amount()`, `validate_category()`, `validate_description()`
4. `data.py` → `load_transactions()`, `get_next_id()`
5. Build transaction dict and append
6. `data.py` → `save_transactions()`
7. `alerts.py` → `get_all_alerts()`
8. `display.py` → `print_alerts()`, `print_budget_bars()`
9. Return to main menu

---

## Summary

This documentation covers:

1. **How to install and run** the app
2. **How to use every feature** through the CLI menu
3. **Complete function documentation** for all 6 modules + test generator
4. **Data model schemas** with constraints and conventions
5. **Cross-module dependencies** for understanding the architecture

For questions or issues, refer to the respective module section or check the code comments.

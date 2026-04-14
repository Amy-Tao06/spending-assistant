# **MUST-HAVE FEATURES**

> **UI Design Details**: See [UI.md](UI.md) for menu layout, display formatting, and validation specs.

## **1\. Transaction Management**

**1.1 Add Transaction**  
Prompts the user to enter a date (YYYY-MM-DD), a positive amount, a category from the predefined list, and a short description. Assigns a unique auto-incrementing ID to each transaction and saves it to transactions.json.  
Difficulty: ⭐ Easy

**1.2 Transaction Editing and Deletion**  
Allows a user to find a transaction by its ID and either update any of its fields or remove it entirely. The program reloads and re-saves the full list after every change to keep the file consistent.  
Difficulty: ⭐⭐ Medium

**1.3 Category Customization**  
Categories are stored in data/config.json instead of being hardcoded. Users can add or remove categories via a dedicated menu option. All features (validation, statistics, alerts) dynamically read from this config file.  
Difficulty: ⭐⭐ Medium

---

## **2\. Data & File Management**

**2.1 Load and Save Data to CSV/JSON Files**  
All transactions and budget rules are persisted to local files. Every time a transaction is added, edited, or deleted, save\_data() is called immediately to prevent data loss. On startup, load\_data() reads the file into memory as a Python list of dictionaries.  
Difficulty: ⭐ Easy

**2.2 Error Handling for Missing, Empty, or Malformed Files**  
Uses try-except blocks to catch FileNotFoundError (file does not exist), json.JSONDecodeError (corrupted JSON), and empty file scenarios. In each case, the program prints a helpful error message and either creates a fresh empty file or prompts the user to fix the issue. The program must never crash.  
Difficulty: ⭐⭐ Medium

---

## **3\. Interface & Validation**

**3.1 Text-Based CLI Menu with Numbered Options**  
A while True loop that prints a clearly formatted numbered menu on every iteration. Each number maps to a function call. Invalid menu choices are caught and re-prompted gracefully.

**See [UI.md](UI.md) for the complete menu layout & design specs.**

**Difficulty: ⭐ Easy**

**3.2 Input Validation (Dates, Amounts, Categories)**  
Every user input goes through validator.py before being accepted. Dates are checked with datetime.strptime(), amounts use try: float() with a check that the value is positive, and categories are validated against the dynamic list in config.json. Each failed validation re-prompts the user with a clear error message instead of crashing.

**See [UI.md](UI.md) for validation rules table & error messages.**

Difficulty: ⭐⭐ Medium

**3.3 View and Filter Transactions**  
Allows users to view their full transaction history or filter it by a specific date range or category. Results are printed as a formatted table with columns for ID, Date, Amount, Category, and Description.

**See [UI.md](UI.md) for table layout & formatting example.**

Difficulty: ⭐⭐ Medium

---

## 

## 

## **4\. Statistics & Analytics**

**4.1 Summary Statistics (Totals by Category, Daily/Weekly/Monthly)**  
Iterates through all loaded transactions, groups them by category using a dictionary accumulator, and filters by date range using datetime comparisons. Outputs a formatted table showing spending per category for the chosen time period.  
Difficulty: ⭐⭐ Medium

**4.2 Top-3 Spending Categories**  
Takes the category totals dictionary, sorts it by value in descending order, and prints the top 3 results with their amounts and percentage of total spending.  
**Difficulty: ⭐ Easy**

**4.3 Spending Trends (Last 7 and 30 Days)**  
Computes the average daily spending for the last 7 days and last 30 days separately. Compares the two averages and prints whether the user is spending more or less recently. For example: "Your spending this week is 23% higher than your 30-day average."  
Difficulty: ⭐⭐ Medium

**4.4 Export Summary Report**  
Generates a neatly formatted .txt file in the outputs/ folder summarising the current month's spending by category, trends, top-3 categories, and any active budget alerts. This file is used directly as the case study output evidence in the final report.

**See [UI.md](UI.md) for export report format & layout.**

Difficulty: ⭐⭐ Medium

---

## **5\. Alert System**

**5.1 Rule-Based Alerts (Daily/Weekly Caps, Percentage Thresholds)**  
Reads all rules from budget\_rules.json. After every new transaction is added, the alert system automatically checks if today's total for a category exceeds its daily cap, or if a category's share of total spending exceeds its percentage threshold (e.g., Transport \> 30% of total budget).

**See [UI.md](UI.md) for alert display format.**

Difficulty: ⭐⭐ Medium

**5.2 Consecutive Overspend Day Detection**  
Checks the last N days of daily totals for a specific category. If the daily cap was exceeded for 3 or more consecutive days, a special escalated warning is triggered. For example: "Warning: You have exceeded your food budget for 3 days in a row\!"  
Difficulty: ⭐⭐⭐ Hard

**5.3 Uncategorized Transaction Warnings**  
After loading transactions, scans for any entries with "category": "Uncategorized" or a category that no longer exists in config.json. Prints a warning listing the affected transaction IDs and prompts the user to recategorize them.  
Difficulty: ⭐ Easy

---

## **6\. Testing**

**6.1 Test Data Generator with Edge Cases**  
A standalone tests/test\_generator.py script that uses random and datetime libraries to generate 100+ realistic fake transactions spread across the last 30 days. Must deliberately include edge cases: an entire day of zero spending, a batch of uncategorized transactions, and a sudden spike in one category to simulate subscription creep.  
Difficulty: ⭐⭐ Medium

---

# **PROPOSED NICE-TO-HAVE FEATURES**

**P1. Budget Progress Bar**  
When viewing summaries, prints a dynamic text-based progress bar next to each category.  
Built using simple string multiplication. Turns red (using ANSI escape codes) if over 100%.

**See [UI.md](UI.md) for implementation details & example.**

Difficulty: ⭐ Easy — highest impact-to-effort ratio of all proposed features.

**P2. Transaction Search by Keyword**  
Adds a search option to the CLI menu where users can type a keyword (e.g., "McDonald's") and the program filters all transactions whose description contains that string (case-insensitive).  
Difficulty: ⭐ Easy

**P3. Multi-Currency Support**  
Adds an optional currency field to each transaction (default: HKD). Stores fixed exchange rates in config.json (e.g., USD: 7.78, CNY: 1.07). When displaying summaries, converts all amounts to HKD automatically. Useful for international students and directly supports a strong design trade-off discussion in the final report.  
Difficulty: ⭐⭐ Medium

**P4. Spending Goal Tracker**  
Users can set a monthly savings goal in config.json (e.g., "Save HK$500 this month"). The program calculates income minus total spending and displays how close the user is to hitting their savings target, with a progress bar.  
Difficulty: ⭐⭐ Medium

**P5. Recurring Transaction Support**  
Allows users to flag a transaction as recurring with a set frequency (monthly, weekly). On startup, the program checks if any recurring transaction is due today and automatically logs it or reminds the user. Directly addresses the subscription creep case study.  
Difficulty: ⭐⭐⭐ Hard

**P6. Simple Regression-Based Spending Forecasting**  
Uses the last 30 days of daily totals as data points to fit a linear trend using Python's built-in statistics library (no external libraries needed). Predicts the likely total spending by end of the current month and warns the user if it is projected to exceed their monthly budget.  
Difficulty: ⭐⭐⭐ Hard

**P7. Spending Heatmap (Text-Based ASCII Calendar)**  
Prints a calendar grid for the current month where each day cell is filled with a symbol indicating spending intensity (e.g., ░ \= low, ▒ \= medium, █ \= high) based on that day's total relative to the daily average.  
Difficulty: ⭐⭐⭐ Hard

---

# **FEATURES TO AVOID**

* ❌ GUI or Web Dashboard — not required and wastes time better spent on reports.  
* ❌ Live Bank/API Syncing — explicitly out of scope per project guidelines.  
* ❌ Machine Learning or Complex Forecasting — far beyond course level and not justified.  
  ---
# COMP1110 Project — Role & Task Assignments

**Project**: Personal Budget & Spending Assistant (Topic A)  
**Team**: 5 members  
**Status**: Phase 2 (Architecture & implementation 🔄)

---

## Team Members & Roles

### 1. **Yang Andi** (3036587092)
**Role**: Project Lead & UI Design Lead  
**GitHub**: Primary  
**Responsibilities**: Coordinate team, manage timeline, final code review

---

### 2. **Mao Yicheng** (3036483040)
**Role**: Algorithm & Logic Lead  
**Responsibilities**: Core business logic, statistical calculations

---

### 3. **Tao Xinran** (3036525393)
**Role**: Research & Documentation Lead  
**Responsibilities**: Official documentation, research writeups, user guides

---

### 4. **Wang Ziyi** (3036484020)
**Role**: Testing & Evaluation Lead  
**Responsibilities**: QA, test data generation, edge case validation

---

### 5. **Yao Junzhu** (3036590427)
**Role**: Data Modeling & File Management Lead  
**Responsibilities**: Data persistence, file I/O, schema management

---

## File-by-File Task Assignments

### Core Modules

| File | Primary Owner | Secondary | Purpose |
|------|---------------|-----------|---------|
| **main.py** | Yang Andi | Mao Yicheng | CLI menu loop, orchestration, user flows |
| **display.py** | Yang Andi | Tao Xinran | Rich UI rendering, report export, visualization |
| **analytics.py** | Mao Yicheng | Wang Ziyi | Statistics, trends, forecasting, heatmap |
| **alerts.py** | Mao Yicheng | Wang Ziyi | Budget rule enforcement, alert logic |
| **data.py** | Yao Junzhu | Wang Ziyi | File I/O, data persistence, config mgmt |
| **validator.py** | Wang Ziyi | Yao Junzhu | Input validation, edge case handling |

### Config & Data Files

| File | Owner | Purpose |
|------|-------|---------|
| **config/config.json** | Yao Junzhu | Categories, currencies, settings defaults |
| **data/transactions.json** | Yao Junzhu | Transaction ledger (auto-managed by app) |
| **data/budget_rules.json** | Yao Junzhu | Budget rule persistence (auto-managed by app) |

### Testing

| File | Owner | Purpose |
|------|-------|---------|
| **tests/test_generator.py** | Wang Ziyi | 120+ realistic test transactions + edge cases |
| **Test plans** | Wang Ziyi | Manual testing checklist, edge case matrix |

### Documentation

| File | Owner | Purpose |
|------|-------|---------|
| **documentation.md** | Tao Xinran | Comprehensive function & feature docs (created) |
| **roles.md** (this file) | Yang Andi | Task assignments & responsibilities |
| **README.md** | Tao Xinran | Project overview, quick links (maintain) |
| **GUIDELINES.md** | Tao Xinran | Official spec & requirements (maintain) |
| **PLAN.md** | Tao Xinran | Timeline, milestones, research notes |
| **FEATURES.md** | Tao Xinran | Feature list & acceptance criteria |
| **UI.md** | Yang Andi | UI design specs & mockups |

### Root Files

| File | Owner | Purpose |
|------|-------|---------|
| **requirements.txt** | Yao Junzhu | Dependencies (rich, questionary) |
| **.gitignore** | Yang Andi | Git config (exclude __pycache__, .pyc, etc.) |

---

## Detailed Task Breakdown

### 🎯 Yang Andi — Project Lead & UI Design

#### Responsibilities
- Coordinate team progress & communication
- Final code review before merge
- Ensure project timeline adherence
- UI/UX consistency across all flows

#### Primary Files
- **main.py** — Menu loop logic, user flow orchestration
  - `main()` — Entry point, menu dispatcher
  - `add_transaction_flow()`, `view_transactions_flow()`, `edit_delete_flow()`
  - `statistics_flow()`, `alerts_flow()`, `manage_budget_rules_flow()`
  - `manage_categories_flow()`, `settings_flow()`, `export_flow()`
  - Helper primitives: `ask()`, `choose()`, `confirm()`, `pause()`, `_sep()`

- **display.py** — All Rich rendering
  - `print_header()`, `print_transaction_table()`, `print_statistics()`
  - `print_top_categories()`, `print_trends()`, `print_alerts()`
  - `print_budget_bars()`, `print_budget_rules()`, `print_savings_goal()`
  - `print_forecast()`, `print_heatmap()`, `export_report()`

#### Secondary Tasks
- Review Mao's analytics functions for UI integration
- Coordinate with Yao on config updates (exchange rates, categories)

#### Deliverables
- ✅ Functional CLI with 9 major feature flows
- ✅ Rich terminal formatting (colors, panels, tables, progress bars)
- ✅ User feedback (alerts, headers, dividers)

---

### 🧮 Mao Yicheng — Algorithm & Logic Lead

#### Responsibilities
- Implement all statistical calculations
- Design & implement alert logic
- Ensure accuracy of trends, forecasts, and heatmaps

#### Primary Files
- **analytics.py** — All number-crunching
  - `filter_by_date()` — Date range filtering
  - `get_totals_by_category()` — Sum by category
  - `get_top_n_categories()` — Top N ranking
  - `get_spending_trends()` — 7-day & 30-day averages + trend direction
  - `get_daily_totals_by_category()` — Per-day sums
  - `get_consecutive_overspend()` — Streak counting
  - `get_savings_progress()` — Savings calculation
  - `linear_forecast()` — Month-end extrapolation
  - `spending_heatmap()` — Intensity mapping (░ ▒ ▓ █)

- **alerts.py** — Budget rule enforcement
  - `check_daily_caps()` — Today's cap validation
  - `check_percentage_thresholds()` — All-time % validation
  - `check_consecutive_overspend()` — Streak alerts
  - `check_uncategorized()` — Category validation
  - `get_all_alerts()` — Alert aggregation

#### Secondary Tasks
- Work with Wang on test cases for edge cases (negative amounts, zero days, etc.)
- Provide algorithm docs to Tao for documentation.md

#### Deliverables
- ✅ Accurate statistical calculations
- ✅ Correct trend & forecast computation
- ✅ Proper alert triggering logic

---

### 📚 Tao Xinran — Research & Documentation Lead

#### Responsibilities
- Official project documentation
- Research findings (competitor analysis, design justification)
- Maintain README, PLAN, FEATURES, GUIDELINES

#### Primary Files
- **documentation.md** — Complete function & feature reference (CREATED)
  - How to use all 9 features
  - Function documentation per module
  - Data model schemas
  - Module dependency map

#### Secondary Files (maintain)
- **README.md** — Project overview, quick links
- **PLAN.md** — Timeline, research, milestones
- **FEATURES.md** — Feature list & acceptance criteria
- **GUIDELINES.md** — Official spec & requirements
- **UI.md** — Interface design specs (with Yang)

#### Tasks
- [ ] Review documentation.md for completeness
- [ ] Document all 9 major feature flows with examples
- [ ] Create user guide (beginner, intermediate, advanced)
- [ ] Research justification: trade-offs, tool comparisons
- [ ] Case study documentation (with test data from Wang)

#### Deliverables
- ✅ Comprehensive documentation.md
- ✅ User-friendly guides
- ✅ Research & justification report

---

### 🧪 Wang Ziyi — Testing & Evaluation Lead

#### Responsibilities
- Test data generation
- Edge case identification & validation
- Manual testing checklist
- Verification of all features

#### Primary Files
- **tests/test_generator.py** — Test data factory
  - `generate_transactions(n)` — Realistic transaction data (0–30 days)
  - `generate_budget_rules()` — Sample budget rules
  - `rand_amount()` — Category-specific random amounts
  - Generate at least 120 transactions with edge cases:
    - IDs 1–5: `"Uncategorized"` category
    - IDs 106–120: Spending spike (recent 5 days)
    - Mix of currencies (HKD, CNY, USD, etc.)
    - Date range edge cases (today, 30 days ago, cross-month boundaries)

- **validator.py** — Input validation edge cases
  - Work with Yao: ensure all validation handles edge cases
  - Test empty strings, whitespace, boundary values

#### Test Plans to Create
- [ ] Manual testing checklist (9 major flows)
- [ ] Edge case matrix:
  - Empty transaction list
  - Single transaction
  - Date boundary cases (today, month boundary)
  - Negative/zero amounts (should reject)
  - Missing config files (should create defaults)
  - Invalid category (should trigger alert)
- [ ] Multi-terminal testing (macOS Terminal, VS Code, iTerm2)

#### Deliverables
- ✅ 120+ realistic test transactions
- ✅ 5 sample budget rules
- ✅ Test data with baked-in edge cases
- ✅ Manual testing checklist

---

### 💾 Yao Junzhu — Data Modeling & File Management Lead

#### Responsibilities
- File I/O & persistence
- Data schema design & validation
- Config management & defaults
- Exchange rate fetching & caching

#### Primary Files
- **data.py** — All file I/O
  - `load_transactions()`, `save_transactions()`
  - `load_budget_rules()`, `save_budget_rules()`
  - `load_config()`, `save_config()`
  - `get_next_id()` — Auto-incrementing ID assignment
  - `ensure_dirs()` — Create data/config/outputs directories
  - `fetch_exchange_rates()` — Live API call to open.er-api.com
  - Private helpers: `_load_json()`, `_save_json()`

- **validator.py** (secondary) — Data validation
  - Work with Wang on edge case handling

#### Data Files to Design
- **config/config.json** — Schema & defaults
  - Categories list (Food, Transport, Personal, Entertainment, Health, Utilities)
  - Currency rates (HKD base, live update from API)
  - Default currency (HKD)
  - Income & savings goal (user-configurable)

- **data/transactions.json** — Schema validation
  - Fields: id, date (YYYY-MM-DD), amount, currency, category, description
  - Ensure uniqueness of IDs
  - Type checking (amount must be float > 0, currency must be valid)

- **data/budget_rules.json** — Schema validation
  - Fields: category, daily_cap, monthly_cap, pct_threshold
  - All caps are optional; category is required
  - At most one rule per category (upsert logic)

#### Tasks
- [ ] Implement robust file I/O with error handling
- [ ] Test exchange rate API (timeout, parse error, network failure)
- [ ] Ensure data consistency (missing files → defaults)
- [ ] Validate schema on load (type checking, constraint validation)
- [ ] Design migration strategy if schema changes

#### Deliverables
- ✅ Correct file I/O for all data types
- ✅ Live exchange rate fetching
- ✅ Robust config defaults & merging
- ✅ Data validation on load/save

---

## Cross-Team Communication

### Dependencies & Handoff Points

1. **Yang → Mao**: Display functions receive data from Mao's analytics
   - Main displays `print_trends()` output from `get_spending_trends()`
   - Mao provides: sorted lists, calculated percentages, trend indicators

2. **Mao → Yao**: Analytics functions read data from Yao's file I/O
   - Mao's functions receive transaction/rule lists
   - Yao ensures: valid data format, ID uniqueness, category consistency

3. **Yao → Wang**: Validator functions called by file I/O
   - Yao calls validators on config updates (income, savings goal)
   - Wang provides: robust validation logic

4. **Yang → Tao**: Implement features → Document after
   - Yang writes main.py flows → Tao documents in documentation.md
   - Yang writes display.py functions → Tao adds examples to docs

5. **Wang → All**: Test data used by entire team
   - Wang generates test data in test_generator.py
   - Everyone uses this data to test their features

### Weekly Checklist (Every Sunday)

- [ ] Yang: Review all PRs, check timeline
- [ ] Mao: Share algorithm docs / test cases with Wang
- [ ] Tao: Update documentation.md with latest changes
- [ ] Wang: Run full test suite, report issues
- [ ] Yao: Verify data files, check API (exchange rates)

---

## Git Workflow

### Branch Naming
- Feature: `feature/mao-analytics-trends` (owner-feature)
- Bugfix: `fix/yao-json-parsing` (owner-fix)
- Docs: `docs/tao-user-guide` (owner-docs)

### Commit Messages
Follow conventional commits:
```
feat(analytics): add spending_heatmap function
fix(data): handle missing config.json gracefully
docs(tao): update documentation.md with examples
test(wang): add edge case for uncategorized transactions
```

### PR Process
1. Create branch from latest `main`
2. Make changes (keep scope focused)
3. Run tests locally
4. Push & create PR with description
5. Yang reviews (Project Lead)
6. Address feedback
7. Merge when approved

---

## Checklist: Before Submission

- [ ] Yang: Main.py fully functional, all 9 flows tested
- [ ] Mao: Analytics accurate, alerts triggering correctly
- [ ] Tao: Documentation complete, user guide clear
- [ ] Wang: 120+ test transactions generated, edge cases validated
- [ ] Yao: File I/O robust, exchange rate API working
- [ ] All: Code follows CLAUDE.md style guidelines
- [ ] All: Commit history clean, meaningful messages
- [ ] All: README links all docs, setup instructions clear
- [ ] All: Final test run on clean machine (pip install + python main.py)

---

## Resources

- **Code conventions**: See [CLAUDE.md](CLAUDE.md)
- **Full function docs**: See [documentation.md](documentation.md)
- **Feature list**: See [FEATURES.md](FEATURES.md)
- **UI specs**: See [UI.md](UI.md)
- **Project spec**: See [GUIDELINES.md](GUIDELINES.md)

---

**Last Updated**: 2026-04-14  
**Next Review**: Weekly team sync (Sundays)

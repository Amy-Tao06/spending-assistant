**COMP1110 B12 Project Plan**  
**Topic: (A) Personal budget and spending assistant**  
Members: Mao Yicheng, Tao Xinran, Wang Ziyi, Yang Andi, Yao Junzhu

1. **Problem Description**   
   Managing personal spendings is a major daily-life challenge for us university students. Our expenses mostly consist of small transactions like food, MTR/bus fares and personal items. Without an organised way to track these costs, it is incredibly easy to overspend or to miscalculate spendings by the end of the month. Hence, our group decides to solve our desperate needs with an intuitive program to sort it out for us.  
     
   Project Scope:   
   Our project focuses on building a text-based Personal Budget and Spending Assistant mainly using Python. The application will feature a text-based interface that allows users to manually log daily transactions and spending by selecting the date, amount, category and a brief description. The program involves simple file IO involving JSON files.  
     
2. **Role Assignment**

| Role | Name |
| :---- | :---- |
| Lead Algorithm & Logic Developer | Mao Yicheng (3036483040) |
| Lead Researcher & Documentation Manager | Tao Xinran (3036525393) |
| Testing & Evaluation Lead | Wang Ziyi (3036484020) |
| Project Lead & UI Design Lead | Yang Andi (3036587092) |
| Data Modelling & File Management Lead | Yao Junzhu (3036590427) |

   

   While each member serves as a Lead for a specific domain, all five group members will actively participate in coding, testing the program, writing the final reports, etc, to ensure a balanced workload.

   **Project Lead & UI Design Lead**

   Responsible for coordinating the overall timeline, integrating different parts of the program, managing group submissions, and leading the design of the user interface of the program to ensure a smooth user experience.

**Lead Algorithm & Logic Developer**  
In charge of structuring and writing the core algorithms that compute summary  
statistics, spending trends, etc.

**Data Modeling & File Management Lead**  
Manages the underlying transaction data schema and leads the implementation of the file input/output (I/O) functions for data storage via mainly JSON files.

**Lead Researcher & Documentation Manager**  
Heads the survey and comparison of existing budgeting tools (such as Goodbudget and YNAB), analyzes design trade-offs, and ensures formatting consistency across all final reports.

**Testing & Evaluation Lead**  
Leads the creation of the realistic case study scenarios, generates the sample test data,	evaluates the system's limitations, and is in charge of the recording of the final video demo.​

3. **Existing Tools/Apps**  
   We have researched several popular budget management tools to understand their core features, target audiences, and limitations before designing our own program:  
     
   **Spreadsheets (Excel/Google Sheets)**  
- Highly customizable and private.  
- Requires completely manual data entry and setup.


  
**Goodbudget [https://goodbudget.com/](https://goodbudget.com/)** 

- Permanent free tier that includes up to 20 budget categories  
- Requires manual entry for every transaction on the free tier

  **You Need A Budget (YNAB) [https://www.ynab.com/](https://www.ynab.com/)**

- Top 1 in budget managing utilities.  
- It adopts a zero-based budgeting method that requires time and effort to understand and learn, thus having a steep learning curve.  
- Requires a pricey paid subscription, USD14.99/month or USD99/year.


**Spendee [https://www.spendee.com/](https://www.spendee.com/)** 

- Offers visual summaries and allows both manual entry and bank syncing  
- Hides advanced alerts behind a paywall.

4. **Project Timeline**

**Phase 1: Planning (March 15 – March 23\)**

* Problem description, research and analyse the topic on budget managing  
* Research on existing budgeting tools  
* Outline the features to implement in our program

**Phase 2: Core Architecture & Data Models (March 24 – April 12\)**

* Establish the data architecture  
  * Define the transaction schema (date, amount, category, description) and budget rules (e.g., category caps, time periods).   
* Code the algorithms to compute summary statistics  
  * such as total spending and trends  
* Define our rule-based alert system (e.g., warnings for exceeding daily limits)  
* Design an interface with input validation

**Phase 3: Testing and Evaluation (April 13 – April 19\)**

* Construct a test data generator to simulate realistic spending.  
* Design realistic daily-life scenarios  
* Test the program against these scenarios  
* Evaluate the program’s strengths and limitations


**Phase 4: Final Deliverables (April 20 – May 2\)**

* Record the full workflow to produce the final video  
* Prepare the Group Final Report  
* Complete the Individual Final Reports
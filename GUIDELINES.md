# A. Personal Budget and Spending Assistant
Managing personal finances is a common daily-life challenge, especially when spending is
frequent and spread across categories such as meals, transport, and subscriptions. In this
topic, your group will model everyday spending as a computing problem by defining what
information should be recorded for each transaction (e.g., date, amount, category, description)
and how those records should be stored and processed to support practical questions such as
“Where did my money go?” and “When am I likely to overspend?”.

This topic does not aim to build a full-featured commercial budgeting app. Instead, the focus
is on (i) clear problem modeling, (ii) research and evaluation of existing budgeting tools, and
(iii) a simple, well-justified design that can be partially implemented using basic
programming (text-based interaction and simple file input/output). Your research should
include a short survey and comparison of existing solutions, as well as a discussion of design
trade-offs (at least five) to justify key choices such as manual entry vs automation, few vs
many categories, and different ways to set budgets and alerts. The implementation should
reflect your model: your program should read transaction data from files, support a text menu
for adding/viewing transactions, compute summary statistics (totals by category/period,
spending trends), generate rule-based alerts (e.g., daily category caps), and include input
validation with sample test cases. You are not required to handle complex forecasting or bank
syncing; simple grouping and thresholding is sufficient, as long as your approach is clearly
described and consistently applied.

Your final work should include 3–4 case studies that show how your design would be used in
realistic spending situations. A case study is a short, concrete scenario (for example: a student
capping food spending at HK$50/day, tracking transport for a monthly budget, or detecting
subscription creep), supported by specific sample inputs you provide (i.e., transaction files
and budget rules). For each case study, you should run your program on the sample data,
present the summaries and alerts produced, and discuss what the system does well, where it
may fail (e.g., miscategorized expenses, irregular one-offs), and how an existing tool would
handle the same scenario. Finally, discuss the strengths and limitations of your solution, and
directions for future improvement.


Your work should demonstrate three complementary competencies. First, problem modeling:
translating a real-world situation into a structured representation that a computer program can
handle. Second, research and evaluation: investigating existing tools or solutions, comparing
their strengths and limitations, and using this to motivate your design choices. Third,
implementation and evidence: proposing (and partially implementing) a simple solution in
Python with text-based interaction and basic file input/output, supported by test inputs and
realistic case studies.

The project is intended to be manageable for students with limited
programming experience, while still requiring meaningful teamwork, careful analysis, and
clear communication in the project plan and final reports.
# Payroll-tax-Calculator

Payroll Calculator - README

Sample Input/Output Case 1:
---------------------------
Enter employee name: John Doe
Enter hours worked: 45
Enter hourly rate: $20
Does the employee own property? (Yes/No): Yes

--- Payroll Summary ---
Employee Name: John Doe
Gross Pay: $950.0
HST Deduction (13%): $123.5
Property Tax (1.2% on $300,000): $3600.0
Net Pay: $-2773.5

Sample Input/Output Case 2:
---------------------------
Enter employee name: Jane Smith
Enter hours worked: 38
Enter hourly rate: $22
Does the employee own property? (Yes/No): No

--- Payroll Summary ---
Employee Name: Jane Smith
Gross Pay: $836.0
HST Deduction (13%): $108.68
Property Tax: $0.00
Net Pay: $727.32

Challenge Faced:
----------------
One challenge I faced was calculating the overtime pay only for the hours exceeding 40 and ensuring that regular pay was correctly capped at 40 hours. Initially, I used a single calculation without separating regular and overtime hours, which resulted in incorrect totals. I fixed this by adding a conditional block to separate regular and overtime pay.

Reflection:
-----------
This assignment helped me solidify my understanding of applying conditional logic and mathematical operations in a practical scenario. By working through regular vs. overtime pay and applying multiple taxes, I gained hands-on experience with real-world calculations. I also practiced string formatting and proper rounding for financial outputs. It reinforced the importance of testing with various inputs and structuring code for clarity and maintainability. Creating a summary with f-strings was a great way to see how presentation matters when delivering program results. Overall, this project was an effective way to apply key programming concepts in a business context.

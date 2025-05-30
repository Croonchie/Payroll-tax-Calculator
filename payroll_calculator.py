# payroll_calculator.py

def calculate_pay():
    # Collect Employee Input
    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: $"))
    owns_property = input("Does the employee own property? (Yes/No): ").strip().lower()

    # Calculate Regular and Overtime Pay
    if hours_worked <= 40:
        regular_hours = hours_worked
        overtime_hours = 0
    else:
        regular_hours = 40
        overtime_hours = hours_worked - 40

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Apply Taxes
    hst = gross_pay * 0.13
    property_tax = 0

    if owns_property == "yes":
        property_tax = 300000 * 0.012  # 1.2% on $300,000

    total_deductions = hst + property_tax
    net_pay = gross_pay - total_deductions

    # Round all financial figures to 2 decimal places
    gross_pay = round(gross_pay, 2)
    hst = round(hst, 2)
    property_tax = round(property_tax, 2)
    net_pay = round(net_pay, 2)

    # Print a Clean Summary
    print("\n--- Payroll Summary ---")
    print(f"Employee Name: {name}")
    print(f"Gross Pay: ${gross_pay}")
    print(f"HST Deduction (13%): ${hst}")
    if owns_property == "yes":
        print(f"Property Tax (1.2% on $300,000): ${property_tax}")
    else:
        print("Property Tax: $0.00")
    print(f"Net Pay: ${net_pay}")

if __name__ == "__main__":
    calculate_pay()

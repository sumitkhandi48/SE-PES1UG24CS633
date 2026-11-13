CATEGORIES = {"P": "Individual", "C": "Company", "H": "HUF", "F": "Firm"}

def parse_income(income):
    if not income:
        return 0
    try:
        return int(income.replace(',', ''))
    except (ValueError, AttributeError):
        return 0

def monthly_emi(details):
    if not details:
        return 0.0
    try:
        parts = details.split(',')
        if len(parts) != 3:
            return 0.0
        
        principal, rate, years = parts
        r = int(rate) / 1200
        n = int(years) * 12
        
        # Prevent ZeroDivisionError
        if n == 0:
            return 0.0
        if r == 0:
            return round(int(principal) / n, 2)

        return round(int(principal) * r * (1 + r) ** n / ((1 + r) ** n - 1), 2)
    except (ValueError, AttributeError):
        return 0.0

def pan_category(pan):
    if not pan or len(pan) < 4:
        return "Unknown"
    
    category_code = pan[3].upper()
    return CATEGORIES.get(category_code, "Unknown")

def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    result = parse_income(user_input)
    print("Income:", result)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    result = monthly_emi(user_input)
    print("Monthly EMI:", result)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    result = pan_category(user_input)
    print("PAN Category:", result)

if __name__ == "__main__":
    main()
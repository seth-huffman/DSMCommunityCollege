# Ensure that you have docstring at the top of your program with the following format:
"""
* Name         : m1t4_insurance_quote.py
* Author       : Seth Huffman
* Created      : 5/25/25
* Module       : 1
* Topic        : 4
* Description  : Insurance Quote Assignment
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

# Save this dictionary:
cost_dict = {
    16: {
        "min": 2593,
        "liability": 2957,
        "full": 6930
    },
    25: {
        "min": 608,
        "liability": 691,
        "full": 1745
    },
    35: {
        "min": 552,
        "liability": 627,
        "full": 1564
    },
    45: {
        "min": 525,
        "liability": 596,
        "full": 1469
    },
    55: {
        "min": 494,
        "liability": 560,
        "full": 1363
    },
    65: {
        "min": 515,
        "liability": 585,
        "full": 1402
    }
}  

# Utilize try/except to ensure the user input is valid
def intValidation(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input.isdigit():
                raise ValueError("Not a integer")
            return int(user_input)
        except ValueError:
            print("Invalid")

def stringValidation(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input.isalpha():
                raise ValueError("Not a string")
            return user_input
        except ValueError:
            print("Invalid")

# Determine the customer’s coverage cost according to the dictionary by their age and coverage desired.
def calc(age, coverage, accident, discount):
    key = { "SM": "min", "L": "liability", "F": "full" }[coverage]
    total = cost_dict[min(cost_dict.keys(), key=lambda x: abs(x - age))][key] 
       
    # If the user has had any accidents, their coverage rate increases by 41%
    if accident:
        total *= 1.41
    
    # If so, subtract the 10% discount
    if discount:
        total *= 0.9
    
    return total

# Gather user info
def main():
    # Driver Name (string)
    name = stringValidation("Driver Name - ")
    # Driver Age (integer)
    age = intValidation("Driver Age - ")
    # Coverage Level (string (SM, L, F))
    coverage = stringValidation("Coverage Level (SM, L, F) - ")
    # Ask the user if they've had any accidents
    accident = stringValidation("Accidents - ")
    # Ask the user if they want to pay up front for a 10% discount
    discount = stringValidation("Pay Up Front for a 10% Discount - ")

    total = calc(age, coverage, accident, discount)

    # Output the annual insurance cost for the customer
    print(f"Annual Insurance Cost for {name} - ${total}")

# In this assignment, we’re creating a program that will output the auto insurance rate for a customer based on their input
if __name__ == "__main__":
    main()
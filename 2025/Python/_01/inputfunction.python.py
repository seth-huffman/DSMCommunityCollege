# The program should contain a function for prompting the user for how many integers they want to store  
def max():
    while True:
        try:
            total = int(input("How many integers you want to store - ")) 
            # The number of integers stored must be at least 1
            if total <= 0:
                print("The number of integers stored must be at least 1")
            else:
                return total
        # If the user enters bad data, they should be told it's bad and be allowed to enter another integer
        except ValueError:
            print("It's Bad")

# The program should contain another function that prompts the user for the integers they want to store   
def content(count):
    numbers = []
    for i in range(count):
        while True:
            try:
                # This function should have an input parameter with a default value.  
                # The default value should be used for each integer request except 
                # the last one which should override the parameter with something like "Enter your last integer: "
                if i == count - 1:
                    value = int(input("Enter your last integer - "))
                else:
                    value = int(input("Value "))
                numbers.append(value)
                break
            # If the user enters bad data, they should be told it's bad and be allowed to enter another integer
            # The numbers entered by the user must be integers
            except ValueError:
                print("It's Bad")
    return numbers

def main():

    # Once the user has entered the correct number of integers, the program should print the list of integers
    entireIndex = max()
    nums = content(entireIndex)
    print(f"List - {nums}")

    # The program should then print the average value of the integers in the list
    average = sum(nums) / len(nums)
    print(f"Average - {average}")

if __name__ == "__main__":
    main()



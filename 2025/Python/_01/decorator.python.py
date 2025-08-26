# For this assignment, create a function and apply a decorator to this function that makes it run twice.
def decorator(x):
    def duplicate():
        x()
        x()
    return duplicate

#decorator
@decorator
def echo():
    print("Echo")

echo()
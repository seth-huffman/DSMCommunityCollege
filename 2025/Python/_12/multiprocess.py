import random
import multiprocessing

def greaterThan(n):
    return n > 5

def main():
    # Create a list of 1,000,000 random integers between 0-10 with 0 and 10 included.
    randomInt = [random.randint(0, 10) for _ in range(1_000_000)]

    # pass this list into a multiprocessing process that determines whether each item in the list is greater than 5.
    with multiprocessing.Pool() as pool:

        # In your main, count how many of the items were greater than 5.  You should get something like 450,000
        sums = pool.map(greaterThan, randomInt)
    count = sum(sums)

    # Return an appropriate output from the process that indicates whether the item is greater than 5.
    print(count)

if __name__ == "__main__":
    main()
#############################################
## Starting with the code below:
## Run the code as it stands to see the queue get filled and printed out.  You can see each word of the books is tagged with the book title.
#############################################

import re
import time
import multiprocessing
from multiprocessing import Process
import threading

def stream_two_books(book_stream_queue):
    def stream_two_cities():
        with open('A tale of two cities.txt', encoding="UTF-8") as book:
            for line in book:
                if not "THE END" in line:
                    output_str = re.sub('[^A-Za-z0-9\']+', ' ', line)
                    output_str = output_str.strip()
                    if output_str == "":
                        continue
                    if output_str is not None:
                        for word in output_str.split():
                            # print (word)
                            book_stream_queue.put({"two_cities":word.lower()},block=True)
                else:
                    break
        return
    def stream_dracula():
        with open('Dracula.txt', encoding="UTF-8") as book:
            for line in book:
                if not "THE END" in line:
                    output_str = re.sub('[^A-Za-z0-9\']+', ' ', line)
                    output_str = output_str.strip()
                    if output_str == "":
                        continue
                    if output_str is not None:
                        for word in output_str.split():
                            # print(word)
                            book_stream_queue.put({"dracula":word.lower()},block=True)
                else:
                    break
        return


    thread1 = threading.Thread(target = stream_two_cities)
    thread2 = threading.Thread(target = stream_dracula)
    # thread2.daeman = True
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    while not book_stream_queue.empty():
        print(book_stream_queue.get())
    print("threads complete")




# Once all is working, remove the interim prints of the queue so that the program as submitted will only determine the final count

def read_two_books_stream(book_stream_queue):
    time.sleep(4)

    #############################################
    ## Added Code: Start
    #############################################   
    count = {"dracula": 0, "two_cities": 0}

    # Write the read_two_books_stream process to read the queue and count how many words are in each of the books. (leaving in the 4 second delay will help avoid some empty queue issues)
    # Once all is working, remove the interim prints of the queue so that the program as submitted will only determine the final count
    while not book_stream_queue.empty():
        item = book_stream_queue.get()
        for book, word in item.items():
            if book in count:
                count[book] += 1

    # Print the final word counts
    print(count['dracula'])
    print(count['two_cities'])

    #############################################
    ## Added Code: Ended
    #############################################  

    pass

if __name__ == "__main__":
    book_stream_queue = multiprocessing.Queue()
    p1 = Process(target=stream_two_books,args=(book_stream_queue,))
    p2 = Process(target=read_two_books_stream,args=(book_stream_queue,))
    p1.start()
    p2.start()
    p1.join()
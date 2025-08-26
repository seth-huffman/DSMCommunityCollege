--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 1, CHAPTER 2 Assignment
--======================================================

-- Number 1
SELECT * 
  FROM books;

-- Number 2
SELECT title 
  FROM books;

-- Number 3
SELECT title, pubdate AS "Publication Date"
  FROM books;

-- Number 4
SELECT customer#, city, state
  FROM customers;

-- Number 5
SELECT name, contact AS "Contact Person", phone
  FROM publisher;

-- Number 6
SELECT DISTINCT category
  FROM books;

-- Number 7
SELECT DISTINCT customer#, order#
  FROM orders;

-- Number 8
SELECT category, title
  FROM books;

-- Number 9
SELECT lname || ', ' || fname
  FROM author;

-- Number 10
SELECT order#, item#, isbn, paideach, quantity, quantity * paideach AS "Item Total"
  FROM orderitems;

-- Number AC 1
SELECT lastname || ', ' || firstname AS "Name", address, city || ', ' || state AS "Location", zip
  FROM customers;

-- Number AC 2
SELECT title, ((retail - cost) / cost) * 100 AS "Profit %"
  FROM books;
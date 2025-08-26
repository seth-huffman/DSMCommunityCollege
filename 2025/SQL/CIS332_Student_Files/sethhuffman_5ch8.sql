--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 5, CHAPTER 8 Assignment
--======================================================

-- Number 1
SELECT lastname, firstname, state
FROM CUSTOMERS
WHERE state = 'NJ';

-- Number 2
SELECT order#,
       shipdate
FROM ORDERS
WHERE shipdate > TO_DATE('2009-04-01', 'YYYY-MM-DD');

-- Number 3
SELECT title, category
FROM BOOKS
WHERE category != 'Fitness';

-- Number 4
SELECT customer#, lastname, state
FROM CUSTOMERS
WHERE state = 'GA' OR state = 'NJ'
ORDER BY lastname;

-- Number 5
SELECT order#, orderdate
FROM ORDERS
WHERE orderdate <= TO_DATE('2009-04-01', 'YYYY-MM-DD');

-- Number 6
SELECT lastname, firstname
FROM AUTHORS
WHERE lastname LIKE '%IN%'
ORDER BY lastname, firstname;

-- Number 7
SELECT lastname, referred
FROM CUSTOMERS
WHERE referred IS NOT NULL;

-- Number 8
SELECT title, category
FROM BOOKS
WHERE category LIKE 'C%';

SELECT title, category
FROM BOOKS
WHERE category = 'Children' OR category = 'Cooking';

SELECT title, category
FROM BOOKS
WHERE category IN ('Children', 'Cooking');

-- Number 9
SELECT isbn, title
FROM BOOKS
WHERE title LIKE '_A_N%'
ORDER BY title DESC;

-- Number 10
SELECT title, pubdate
FROM BOOKS
WHERE category = 'Computer'
  AND pubdate BETWEEN TO_DATE('2005-01-01', 'YYYY-MM-DD') AND TO_DATE('2005-12-31', 'YYYY-MM-DD');

SELECT title, pubdate
FROM BOOKS
WHERE category = 'Computer'
  AND EXTRACT(YEAR FROM pubdate) = 2005;

SELECT title, pubdate
FROM BOOKS
WHERE category = 'Computer'
  AND TO_CHAR(pubdate, 'YYYY') LIKE '2005';


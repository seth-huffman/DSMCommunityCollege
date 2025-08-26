--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 7, CHAPTER 10 Assignment
--======================================================

--==========================
-- Number 1
--==========================
SELECT COUNT(*) AS "Total Cooking Books"
FROM BOOKS
WHERE CATEGORY = 'COOKING';

--==========================
-- Number 2
--==========================
SELECT COUNT(*) AS "Books Over $30"
FROM BOOKS
WHERE retail > 30;

--==========================
-- Number 3
--==========================
SELECT MAX(pubdate) AS "Most Recent"
FROM BOOKS;

--==========================
-- Number 5
--==========================
SELECT MIN(retail) AS "Least expensive"
FROM BOOKS
WHERE CATEGORY = 'COMPUTER';

--==========================
-- Number 6
--==========================
SELECT TO_CHAR(AVG(total_profit), '$1,000,000.00') AS "Average"
FROM (
    SELECT order#,
           SUM((oi.paideach - b.cost) * oi.qty) AS total_profit
    FROM ORDERITEMS oi
    JOIN BOOKS b ON oi.isbn = b.isbn
    GROUP BY order#
);

--==========================
-- Number 7
--==========================
SELECT c.customer#, c.firstname || ' ' || c.lastname AS "Customer",
       COUNT(o.order#) AS "Total"
FROM CUSTOMERS c
JOIN ORDERS o ON c.customer# = o.customer#
GROUP BY c.customer#, c.firstname, c.lastname;

--==========================
-- Number 8
--==========================
SELECT p.name AS "Publisher", b.category AS "Category",
       ROUND(AVG(b.retail), 2) AS "Average"
FROM BOOKS b
JOIN PUBLISHERS p ON b.publisher# = p.publisher#
WHERE b.category IN ('Children', 'Computer')
GROUP BY p.name, b.category
HAVING AVG(b.retail) > 50;

--==========================
-- Number 9
--==========================
SELECT DISTINCT c.customer#, c.firstname || ' ' || c.lastname AS "Customer",
       c.state, SUM(oi.qty * oi.paideach) AS "Total"
FROM CUSTOMERS c
JOIN ORDERS o ON c.customer# = o.customer#
JOIN ORDERITEMS oi ON o.order# = oi.order#
WHERE c.state IN ('GA', 'FL')
GROUP BY c.customer#, c.firstname, c.lastname, c.state, o.order#
HAVING SUM(oi.qty * oi.paideach) > 80;

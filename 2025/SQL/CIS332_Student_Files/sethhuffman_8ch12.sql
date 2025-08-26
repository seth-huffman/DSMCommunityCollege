--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 8, CHAPTER 12 Assignment
--======================================================

--==========================
-- Number 1
--==========================
SELECT title, retail
FROM BOOKS
WHERE retail < (SELECT AVG(retail) FROM BOOKS);

--==========================
-- Number 2
--==========================
SELECT title, retail, category
FROM BOOKS b1
WHERE retail < (
  SELECT AVG(retail)
  FROM BOOKS b2
  WHERE b1.category = b2.category
);

--==========================
-- Number 3
--==========================
SELECT order# 
FROM ORDERS
WHERE shipstate = (
  SELECT shipstate
  FROM ORDERS
  WHERE order# = 1014
);

--==========================
-- Number 4
--==========================
SELECT order#
FROM ORDERITEMS
GROUP BY order#
HAVING SUM(quantity * paideach) > (
  SELECT SUM(quantity * paideach)
  FROM ORDERITEMS
  WHERE order# = 1008
);

--==========================
-- Number 5
--==========================
SELECT DISTINCT a.authorid, a.firstname, a.lastname
FROM AUTHORS a
JOIN BOOKAUTHOR ba ON a.authorid = ba.authorid
WHERE ba.isbn IN (
  SELECT isbn
  FROM ORDERITEMS
  GROUP BY isbn
  HAVING SUM(quantity) = (
    SELECT MAX(total)
    FROM (
      SELECT SUM(quantity) AS total
      FROM ORDERITEMS
      GROUP BY isbn
    )
  )
);

--==========================
-- Number 6
--==========================
SELECT title
FROM BOOKS
WHERE category IN (
  SELECT DISTINCT b.category
  FROM BOOKS b
  JOIN ORDERITEMS oi ON b.isbn = oi.isbn
  JOIN ORDERS o ON oi.order# = o.order#
  WHERE o.customer# = 1007
)
AND isbn NOT IN (
  SELECT oi.isbn
  FROM ORDERITEMS oi
  JOIN ORDERS o ON oi.order# = o.order#
  WHERE o.customer# = 1007
);

--==========================
-- Number 7
--=========================
SELECT shipcity, shipstate
FROM ORDERS
WHERE order# = (
  SELECT order#
  FROM ORDERS
  WHERE shipdate - orderdate = (
    SELECT MAX(shipdate - orderdate)
    FROM ORDERS
  )
);

--==========================
-- Number 8
--==========================
SELECT DISTINCT o.customer#
FROM ORDERS o
JOIN ORDERITEMS oi ON o.order# = oi.order#
WHERE oi.isbn IN (
  SELECT isbn
  FROM BOOKS
  WHERE retail = (
    SELECT MIN(retail)
    FROM BOOKS
  )
);

--==========================
-- Number 9
--==========================
SELECT COUNT(DISTINCT o.customer#)
FROM ORDERS o
JOIN ORDERITEMS oi ON o.order# = oi.order#
WHERE oi.isbn IN (
  SELECT ba.isbn
  FROM BOOKAUTHOR ba
  JOIN AUTHORS a ON ba.authorid = a.authorid
  WHERE a.firstname = 'James' AND a.lastname = 'Austin'
);

--==========================
-- Number 10
--==========================
SELECT title
FROM BOOKS
WHERE pubid = (
  SELECT pubid
  FROM BOOKS
  WHERE title = 'The Wok Way to Cook'
);

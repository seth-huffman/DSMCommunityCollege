--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 6, CHAPTER 9 Assignment
--======================================================

--==========================
-- Number 1
--==========================
SELECT b.title, p.contact, p.phone -- SAME
-- FROM BOOKS b, publishers p
FROM BOOKS b
-- WHERE b.pubid = p.pubid;
JOIN publishers p ON b.pubid = p.pubid;

--==========================
-- Number 2
--==========================
SELECT o.order#, o.orderdate, c.firstname, c.lastname -- SAME
-- FROM ORDERS o, CUSTOMERS c
FROM ORDERS o
JOIN CUSTOMERS c ON o.customer# = c.customer#
WHERE o.shipdate IS NULL -- SAME
-- AND o.customer# = c.customer#
ORDER BY o.orderdate; -- SAME

--==========================
-- Number 4
--==========================
SELECT DISTINCT b.title  -- SAME
-- FROM CUSTOMERS c, ORDERS o, ORDERITEMS oi, BOOKS b
FROM CUSTOMERS c
JOIN ORDERS o ON c.customer# = o.customer#
JOIN ORDERITEMS oi ON o.order# = oi.order#
JOIN BOOKS b ON oi.isbn = b.isbn
WHERE c.firstname = 'Jake' -- SAME
AND c.lastname = 'Lucas'; -- SAME
-- AND c.customer# = o.customer#
-- AND o.order# = oi.order#
-- AND oi.isbn = b.isbn;


--==========================
-- Number 10
--==========================
SELECT e.firstname || ' ' || e.lastname AS employee_name, -- SAME
       e.job_title, -- SAME
       m.firstname || ' ' || m.lastname AS manager_name -- SAME
-- FROM EMPLOYEES e, EMPLOYEES m
FROM EMPLOYEES e
-- WHERE e.manager_id = m.empid(+)
LEFT JOIN EMPLOYEES m ON e.manager_id = m.empid
ORDER BY manager_name; -- SAME



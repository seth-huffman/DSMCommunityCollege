--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 6, CHAPTER 9 Assignment
--======================================================

--==========================
-- Number 3
--==========================
SELECT c.customer#,
       c.firstname,
       c.lastname,
       c.state,
       b.title,
       b.subject
FROM CUSTOMERS c, ORDERS o, ORDERITEMS oi, BOOKS b
WHERE c.customer# = o.customer#
  AND o.order# = oi.order#
  AND oi.isbn = b.isbn
  AND c.state = 'FL'
  AND b.subject = 'COMPUTER';

--==========================
-- Number 7
--==========================
SELECT b.title, b.retail, g.gift
FROM BOOKS b, giftchoices g
WHERE b.retail BETWEEN g.minretail AND g.maxretail
  AND b.title = 'Shortest Poems';

--==========================
-- Number 9
--==========================
SELECT b.title,
       b.isbn,
       o.order#,
       c.state
FROM BOOKS b,
     ORDERITEMS oi,
     ORDERS o,
     CUSTOMERS c
WHERE b.isbn = oi.isbn(+)
  AND oi.order# = o.order#(+)
  AND o.customer# = c.customer#(+);

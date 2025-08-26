--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 4, CHAPTER 5 Assignment
--======================================================

-- Number 1
INSERT INTO ORDERS 
(Order#, Customer#, OrderDate)
VALUES (1021, 1009, TO_DATE('20-JUL-2009', 'DD-MON-YYYY'));

-- Number 2
UPDATE ORDERS
SET ShipZip = '33222'
WHERE Order# = 1017;

-- Number 3
COMMIT;

-- Number 6
UPDATE BOOKS
SET Cost = &new_cost
WHERE ISBN = '&isbn';

COMMIT;

-- Number 9
DELETE FROM ORDERITEMS
WHERE Order# = 1005;
DELETE FROM ORDERS
WHERE Order# = 1005;

-- Number 10
ROLLBACK;
COMMIT;
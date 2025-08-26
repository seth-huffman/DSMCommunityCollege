--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 7, CHAPTER 10 Assignment
--======================================================

--==========================
-- Number 1
--==========================
SELECT 
  INITCAP(firstname) AS "First_Name", 
  INITCAP(lastname) AS "Last_Name"
FROM CUSTOMERS;

--==========================
-- Number 2
--==========================
SELECT 
  customer# AS "Customer_Number",
  CASE 
    WHEN referred IS NULL THEN 'NOT REFERRED'
    ELSE 'REFERRED'
  END AS "Referral_Status"
FROM CUSTOMERS;

--==========================
-- Number 3
--==========================
SELECT 
  b.title AS "Book_Title",
  TO_CHAR(SUM((oi.paideach - b.cost) * oi.qty), '$1,000,000.00') AS "Profit"
FROM BOOKS b
JOIN ORDERITEMS oi ON b.isbn = oi.isbn
WHERE oi.order# = 1002
GROUP BY b.title;


--==========================
-- Number 4
--==========================
SELECT 
  title AS "Book_Title",
  TO_CHAR(((retail - cost)/cost)*100, '999') || '%' AS "Markup_Percentage"
FROM BOOKS;

--==========================
-- Number 5
--==========================
SELECT 
  TO_CHAR(SYSDATE, 'Day') AS "Day",
  TO_CHAR(SYSDATE, 'HH24') AS "Hour",
  TO_CHAR(SYSDATE, 'MI') AS "Minutes",
  TO_CHAR(SYSDATE, 'SS') AS "Seconds"
FROM DUAL;

--==========================
-- Number 6
--==========================
SELECT 
  title AS "Book_Title",
  LPAD(TO_CHAR(cost, '1,000.00'), 12, '*') AS "Cost_Display"
FROM BOOKS;

--==========================
-- Number 7
--==========================
SELECT DISTINCT 
  LENGTH(isbn) AS "ISBN_Length"
FROM BOOKS;

--==========================
-- Number 8
--==========================
SELECT 
  title AS "Book_Title",
  TO_CHAR(pubdate, 'MM/DD/YYYY') AS "Publication_Date",
  TO_CHAR(SYSDATE, 'MM/DD/YYYY') AS "Current_Date",
  FLOOR(MONTHS_BETWEEN(SYSDATE, pubdate)) AS "Book_Age_Months"
FROM BOOKS;

--==========================
-- Number 9
--==========================
SELECT 
  NEXT_DAY(SYSDATE, 'WEDNESDAY') AS "Next_Wednesday"
FROM DUAL;

--==========================
-- Number 10
--==========================
SELECT 
  customer# AS "Customer_Number",
  SUBSTR(zip, 3, 2) AS "3AND4_Zip",
  INSTR(customer#, '3') AS "First_3_Position"
FROM CUSTOMERS;


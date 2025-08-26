--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 2, CHAPTER 3 Assignment
--======================================================

-- Number 1
CREATE TABLE CATEGORY (
    CatCode CHAR(2),
    CatDesc VARCHAR(10)
);

-- Number 2
CREATE TABLE EMPLOYEES (
    "Emp#" NUMBER(5),
    Lastname VARCHAR2(30),
    Firstname VARCHAR2(30),
    Job_Class VARCHAR2(4)
);

-- Number 3
ALTER TABLE EMPLOYEES
ADD (
    EmpDate DATE DEFAULT SYSDATE,
    EndDate DATE
);

-- Number 4
ALTER TABLE EMPLOYEES
MODIFY Job_Class VARCHAR2(2);

-- Number 5
ALTER TABLE EMPLOYEES
DROP COLUMN EndDate;

-- Number 6
RENAME EMPLOYEES TO JL_EMPS;

-- Number 7
CREATE TABLE BOOK_PRICING AS
SELECT 
    ISBN AS ID,
    Cost,
    Retail,
    Category
FROM BOOKS;

-- Number 8
ALTER TABLE BOOK_PRICING
SET UNUSED COLUMN Category;

-- Number 9
TRUNCATE TABLE BOOK_PRICING;

-- Number 10
DROP TABLE BOOK_PRICING PURGE;
SELECT COUNT(*) FROM JL_EMPS;
DROP TABLE JL_EMPS;

-- Number AC 1
ALTER TABLE ACCTMANAGER
ADD (
    Comm_id NUMBER(2) DEFAULT 10,
    Ben_id NUMBER(2)
);

-- Number AC 2
DROP TABLE COMMATE;
CREATE TABLE COMMATE (
    Comm_id NUMBER(2),
    Comm_rank VARCHAR2(15),
    Rate NUMBER(5,2) 
);

-- Number AC 3
DROP TABLE BENEFITS;
CREATE TABLE BENEFITS (
    Ben_id NUMBER(2),
    Ben_plan CHAR(1),
    Ben_provider NUMBER(3),
    Active CHAR(1) CHECK (Active IN ('Y', 'N'))
);


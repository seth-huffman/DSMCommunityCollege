--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 4, CHAPTER 6 Assignment
--======================================================

-- Number 1
CREATE SEQUENCE sequence
START WITH 1021
INCREMENT BY 1
NOCACHE
NOCYCLE;

-- Number 2
INSERT INTO CUSTOMERS (customer#, lastname, firstname, zip) 
VALUES (sequence.NEXTVAL, 'Shoulders', 'Frank', '23567');

-- Number 3
CREATE SEQUENCE MY_FIRST_SEQ
START WITH 5
INCREMENT BY -3
MINVALUE 0
NOCYCLE;

-- Number 4
SELECT MY_FIRST_SEQ.NEXTVAL FROM dual;
SELECT MY_FIRST_SEQ.NEXTVAL FROM dual;
SELECT MY_FIRST_SEQ.NEXTVAL FROM dual;

-- Number 5
ALTER SEQUENCE MY_FIRST_SEQ
MINVALUE -1000;

-- Number 6
CREATE TABLE EMAIL_LOG (
  emailid NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  emaildate DATE,
  "Customer#" NUMBER
);

INSERT INTO EMAIL_LOG (emaildate, "Customer#")
VALUES (SYSDATE, 1007);

INSERT INTO EMAIL_LOG (emaildate, "Customer#")
VALUES (SYSDATE, 1008);

INSERT INTO EMAIL_LOG (emailid, emaildate, "Customer#")
VALUES (25, SYSDATE, 1009);

-- Number 7
CREATE SYNONYM NUMGEN FOR MY_FIRST_SEQ;

-- Number 8
SELECT NUMGEN.CURRVAL FROM DUAL;
DROP SYNONYM NUMGEN;
DROP SEQUENCE MY_FIRST_SEQ;


-- Number 10
CREATE INDEX LNINDEX ON CUSTOMERS(Lastname);

SELECT index_name, table_name, index_type
FROM user_indexes
WHERE table_name = 'CUSTOMER'
  AND index_name = 'LNINDEX';

DROP INDEX LNINDEX;


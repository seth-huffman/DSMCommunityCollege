--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 2, CHAPTER 3 Assignment
--======================================================

-- Number 1
CREATE TABLE STORE_REPS (
    rep_id NUMBER(5) PRIMARY KEY,
    last VARCHAR2(15),
    first VARCHAR2(10),
    comm CHAR(1) DEFAULT 'Y'
);

-- Number 2
ALTER TABLE STORE_REPS
MODIFY (
    last VARCHAR2(15) NOT NULL,
    first VARCHAR2(10) NOT NULL
);

-- Number 3
ALTER TABLE STORE_REPS
ADD CONSTRAINT comm_check 
CHECK (
    comm IN ('Y', 'N')
);

-- Number 4
ALTER TABLE STORE_REPS
ADD base_salary NUMBER(7,2);

-- Number 5
CREATE TABLE BOOK_STORES (
    store_id NUMBER(8) PRIMARY KEY,
    name VARCHAR2(30) NOT NULL UNIQUE,
    contract VARCHAR2(30),
    rep_id NUMBER(5)
);

-- Number 6
ALTER TABLE BOOK_STORES
ADD CONSTRAINT value_entered
FOREIGN KEY (rep_id) REFERENCES store_reps(rep_id);

-- Number 7
ALTER TABLE BOOK_STORES
DROP CONSTRAINT value_entered;

ALTER TABLE BOOK_STORES
ADD CONSTRAINT value_entered
FOREIGN KEY (rep_id)
REFERENCES STORE_REPS(rep_id)
ON DELETE CASCADE;

-- Number 8
CREATE TABLE REP_CONTRACTS (
    store_id NUMBER(8),
    name NUMBER(5),
    quarter CHAR(3),
    rep_id NUMBER(5),
    PRIMARY KEY (rep_id, store_id, quarter),
    FOREIGN KEY (rep_id) REFERENCES STORE_REPS(rep_id),
    FOREIGN KEY (store_id) REFERENCES BOOK_STORES(store_id)
);

-- Number 9
SELECT constraint_name, constraint_type, search_condition
FROM user_constraints
WHERE table_name = 'STORE_REPS';

-- Number 10
ALTER TABLE STORE_REPS
DISABLE CONSTRAINT base_salary;
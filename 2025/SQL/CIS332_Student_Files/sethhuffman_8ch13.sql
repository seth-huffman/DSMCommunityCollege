--====================================================== 
-- Seth Huffman
-- CIS332: Database and SQL
-- UNIT 8, CHAPTER 13 Assignment
--======================================================

--==========================
-- Number 1
--==========================
CREATE VIEW contact AS
SELECT contact, phone
FROM PUBLISHERS;

--==========================
-- Number 2
--==========================
CREATE OR REPLACE VIEW contact AS
SELECT contact, phone
FROM PUBLISHERS
WITH READ ONLY;

--==========================
-- Number 3
--==========================
CREATE FORCE VIEW HOMEWORK13 (Col1, Col2) AS
SELECT Col1, Col2
FROM FIRSTATTEMPT;

--==========================
-- Number 4
--==========================
SELECT column_name, data_type, data_length 
FROM user_tab_columns 
WHERE table_name = 'HOMEWORK13';

--==========================
-- Number 5
--==========================
CREATE VIEW reorderinfo AS
SELECT b.isbn, b.title, p.contact, p.phone
FROM BOOKS b
JOIN PUBLISHERS p ON b.publisher_id = p.publisher_id;

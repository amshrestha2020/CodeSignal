-- You have your very own library at home, and it's getting bigger and bigger with each passing month. You've decided to create a database in which to store information about your books, in the hope that it will help you remember which books you have in your library.

-- Information about the books in your library is stored in the table catalogs, which contains the following columns:

-- doc_id - the unique ID of the catalog;
-- xml_doc - the catalog as an XML file in the following format:
-- <catalog>
--   <book id="...">
--     <author>...</author>
--     <title>...</title>
--   </book>
--   <book id="...">
--     <author>...</author>
--     <title>...</title>
--   </book>
--   ...
-- </catalog>.
-- Each catalog represents the work of one distinct <author> in your library. There is exactly one <catalog> element in each xml_doc, and the id for each book is unique.

-- Given the catalogs table, you want to find out which authors you have represented in your library. Your task is to create a new table with the author column that will contain all the distinct authors, sorted by their names.

-- Example

-- For given table catalogs

-- doc_id	xml_doc
-- 1	
-- <catalog>
--  <book id="11">
--   <author>Chuck Palahniuk</author>
--   <title>Fight Club</title>
--  </book>
--  <book id="12">
--   <author>Chuck Palahniuk</author>
--   <title>Survivor</title>
--  </book>
-- </catalog>
-- 2	
-- <catalog>
--  <book id="21">
--   <author>Bernard Werber</author>
--   <title>Les Thanatonautes</title>
--  </book>
-- </catalog>
-- 3	
-- <catalog>
--  <book id="31">
--   <author>Boris Vian</author>
--   <title>The Big Sleep</title>
--  </book>
--  <book id="32">
--   <author>Boris Vian</author>
--   <title>The Lady in the Lake</title>
--  </book>
--  <book id="33">
--   <author>Boris Vian</author>
--   <title>The World of Null-A</title>
--  </book>
-- </catalog>
-- the output should be

-- author
-- Bernard Werber
-- Boris Vian
-- Chuck Palahniuk


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT ExtractValue(xml_doc, '/catalog/book[1]/author') as author
    FROM catalogs
    ORDER BY author;

END
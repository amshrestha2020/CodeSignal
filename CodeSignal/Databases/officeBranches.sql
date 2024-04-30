-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- In order to optimize your business, you've decided to merge a couple of your office branches and get rid of the outdated branch types.

-- The existing office branches and branch types are stored in the tables branches and branch_types, respectively. The tables have the following structures:

-- branches:
-- branch_id: the branch ID;
-- name: the name of the branch;
-- branchtype_id: the branch type ID.
-- branch_types
-- id: the unique branch ID;
-- name: the name of the branch type.
-- You've decided to start small. As your first step, you want to delete the outdated branch types, all of which end with -outdated, from the branch_types table.

-- For now, you want to keep all the branches with the deleted branch types in the branches table, but to differentiate them you will set their branchtype_id to NULL. Update the database to make the required changes happen automatically when a record is deleted from branch_types.

-- Example

-- For the following tables branches

-- branch_id	name	branchtype_id
-- 1	Frankfurt branch	2
-- 2	Paris branch	3
-- 3	New York branch	2
-- 4	Madrid branch	1
-- and branch_types

-- id	name
-- 1	Small-outdated
-- 2	Big
-- 3	Medium
-- the output should be

-- branch_id	name	branchtype_id
-- 1	Frankfurt branch	2
-- 2	Paris branch	3
-- 3	New York branch	2
-- 4	Madrid branch	NULL


CREATE PROCEDURE solution()
BEGIN
    ALTER TABLE branches ADD FOREIGN KEY (branchtype_id)
    REFERENCES branch_types(id) ON DELETE SET NULL;

    DELETE FROM branch_types WHERE name LIKE '%-outdated';

    SELECT * FROM branches
    ORDER BY branch_id;
END

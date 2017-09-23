-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.



-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.

-- Write a SQL query for a report that provides the following information for each person in the Person table, 
-- regardless if there is an address for each of those people:

-- FirstName, LastName, City, State

-- init
select p.FirstName, p.LastName, a.City, a.State from Person p, Address a where p.PersonId = a.PersonId;

-- improved:
select p.FirstName, p.LastName, a.City, a.State from Person p LEFT JOIN Address a ON p.PersonId = a.PersonId;

-- due to no conflict field in two schema, so
select FirstName, LastName, City, State from Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;




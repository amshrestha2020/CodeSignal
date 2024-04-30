-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You are developing an application for working with different currencies. You've decided to represent each currency using three letter codes from ISO 4217.

-- You've parsed some data that you found on the Internet and stored it in a currencies table, which has the following structure:

-- code: the unique code of the currency;
-- country: the name of the country in which this currency is used.
-- Unfortunately, your parser didn't check the length of the codes and some erroneous data got into the table by mistake.

-- Your task is to delete all rows from the currencies table in which code is not exactly three letters long.

-- Example

-- The following table currencies

-- code	country
-- AD	Andorra
-- AUD	Australia
-- BRL	Brazil
-- MXN	Mexico
-- RUB	Russia
-- RUR	Russia
-- SEKR	Sweden
-- USD	USA
-- should become

-- code	country
-- AUD	Australia
-- BRL	Brazil
-- MXN	Mexico
-- RUB	Russia
-- RUR	Russia
-- USD	USA


CREATE PROCEDURE solution()
BEGIN
    DELETE FROM currencies
    WHERE LENGTH(code) != 3;

    SELECT * FROM currencies ORDER BY code;
END

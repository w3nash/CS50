-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get description of the crime
SELECT "description"
FROM "crime_scene_reports"
WHERE "month" = 7
AND "day" = 28
AND "year" = 2021
AND "street" = "Humphrey Street";

-- Get the witness report
SELECT "name", "transcript"
FROM "interviews"
WHERE "month" = 7
AND "day" = 28
AND "year" = 2021;

-- 3 Witnesses
-- Ruth
-- Eugene
-- Raymond

-- Get bakery secuity footage
SELECT *
FROM "bakery_security_logs"
WHERE "month" = 7
AND "day" = 28
AND "year" = 2021
AND "hour" = 10
AND "minute" >= 15
AND "minute" <= 25;

-- Get the owners of the license plate we had in footage.
SELECT "name"
FROM "people"
WHERE "license_plate" IN (
    SELECT "license_plate"
    FROM "bakery_security_logs"
    WHERE "month" = 7
    AND "day" = 28
    AND "year" = 2021
    AND "hour" = 10
    AND "minute" >= 15
    AND "minute" <= 25
);

-- Get ATM logs
SELECT *
FROM "atm_transactions"
WHERE "month" = 7
AND "day" = 28
AND "year" = 2021
AND "atm_location" = 'Leggett Street';

-- Get the owners of the account number we had in ATM logs
SELECT "name"
FROM "people"
WHERE "id" IN (
    SELECT "person_id"
    FROM "bank_accounts"
    WHERE "account_number" IN (
        SELECT "account_number"
        FROM "atm_transactions"
        WHERE "month" = 7
        AND "day" = 28
        AND "year" = 2021
        AND "atm_location" = 'Leggett Street'
    )
);

-- We eliminate some suspects
SELECT "name"
FROM "people"
WHERE "license_plate" IN (
    SELECT "license_plate"
    FROM "bakery_security_logs"
    WHERE "month" = 7
    AND "day" = 28
    AND "year" = 2021
    AND "hour" = 10
    AND "minute" >= 15
    AND "minute" <= 25
)
INTERSECT
SELECT "name"
FROM "people"
WHERE "id" IN (
    SELECT "person_id"
    FROM "bank_accounts"
    WHERE "account_number" IN (
        SELECT "account_number"
        FROM "atm_transactions"
        WHERE "month" = 7
        AND "day" = 28
        AND "year" = 2021
        AND "atm_location" = 'Leggett Street'
    )
);

-- SUSPECTS
-- Bruce
-- Diana
-- Iman
-- Luca

-- Get the phone calls of the suspects in that day.
SELECT "people"."name", "people"."passport_number", "phone_calls"."receiver"
FROM "phone_calls"
JOIN "people" ON "people"."phone_number" = "phone_calls"."caller"
WHERE "month" = 7
AND "phone_calls"."day" = 28
AND "phone_calls"."year" = 2021
AND "phone_calls"."duration" <= 60
AND "people"."name" IN (
    SELECT "name"
    FROM "people"
    WHERE "license_plate" IN (
        SELECT "license_plate"
        FROM "bakery_security_logs"
        WHERE "month" = 7
        AND "day" = 28
        AND "year" = 2021
        AND "hour" = 10
        AND "minute" >= 15
        AND "minute" <= 25
    )
    INTERSECT
    SELECT "name"
    FROM "people"
    WHERE "id" IN (
        SELECT "person_id"
        FROM "bank_accounts"
        WHERE "account_number" IN (
            SELECT "account_number"
            FROM "atm_transactions"
            WHERE "month" = 7
            AND "day" = 28
            AND "year" = 2021
            AND "atm_location" = 'Leggett Street'
        )
    )
);

-- SUSPECTS
-- Name, Passport No.
-- Bruce, 5773159633
-- Diana, 3592750733

-- PERSON ON THE PHONE WITH Bruce
SELECT "name", "passport_number"
FROM "people"
WHERE "phone_number" = "(375) 555-8161";
-- Name: Robin, No Passport

-- PERSON ON THE PHONE WITH Diana
SELECT "name", "passport_number"
FROM "people"
WHERE "phone_number" = "(725) 555-3243";
-- Name: Philip, 3391710505

-- QUERY ON AIRPORTS
SELECT *
FROM "airports";

-- GET FLIGHTS LOGS ON AND AFTER THE DAY OF CRIME
SELECT *
FROM "flights"
WHERE "year" = 2021
AND "month" = 7
AND "day" >= 28
AND "origin_airport_id" = (
    SELECT "id"
    FROM "airports"
    WHERE "abbreviation" = "CSF"
)
ORDER BY "day";

-- Flight made by Bruce, to airport 4 in 4A 29
SELECT "flights"."destination_airport_id", "flights"."day", "passengers"."seat"
FROM "flights"
JOIN "airports"
ON "flights"."origin_airport_id" = "airports"."id"
JOIN "passengers"
ON "flights"."id" = "passengers"."flight_id"
WHERE "airports"."id" = 8
AND "passengers"."passport_number" = 5773159633
AND "flights"."year" = 2021
AND "flights"."month" = 7
AND "flights"."day" >= 28;

-- Flight made by Diana, to airport 6-29, 5-30 in 4C, 6C
SELECT "flights"."destination_airport_id", "flights"."day", "passengers"."seat"
FROM "flights"
JOIN "airports"
ON "flights"."origin_airport_id" = "airports"."id"
JOIN "passengers"
ON "flights"."id" = "passengers"."flight_id"
WHERE "airports"."id" = 8
AND "passengers"."passport_number" = 3592750733
AND "flights"."year" = 2021
AND "flights"."month" = 7
AND "flights"."day" >= 28;

-- Flight made by Philip, to airport 6-29, 5-30 in 4C, 6C
SELECT "flights"."destination_airport_id", "flights"."day", "passengers"."seat"
FROM "flights"
JOIN "airports"
ON "flights"."origin_airport_id" = "airports"."id"
JOIN "passengers"
ON "flights"."id" = "passengers"."flight_id"
WHERE "airports"."id" = 8
AND "passengers"."passport_number" = 3391710505
AND "flights"."year" = 2021
AND "flights"."month" = 7
AND "flights"."day" >= 28;

-- I suspect Bruce
-- He went to New York City
-- ACCOMPLICE is Robin
SELECT "city"
FROM "airports"
WHERE "id" IN (
    SELECT "flights"."destination_airport_id"
    FROM "flights"
    JOIN "airports"
    ON "flights"."origin_airport_id" = "airports"."id"
    JOIN "passengers"
    ON "flights"."id" = "passengers"."flight_id"
    WHERE "airports"."id" = 8
    AND "passengers"."passport_number" = 5773159633
    AND "flights"."year" = 2021
    AND "flights"."month" = 7
    AND "flights"."day" >= 28
);
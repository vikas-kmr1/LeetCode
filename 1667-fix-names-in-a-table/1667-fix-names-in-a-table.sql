# Write your MySQL query statement below
SELECT USERS.USER_ID, CONCAT(
                                UCASE(LEFT(USERS.NAME, 1)),
                                LCASE(SUBSTRING(USERS.NAME,2))
                            ) AS NAME
FROM USERS
        ORDER BY USERS.USER_ID;
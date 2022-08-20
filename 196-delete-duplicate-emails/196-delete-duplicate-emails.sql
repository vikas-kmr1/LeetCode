# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE P0 
    FROM PERSON P0 , PERSON P1
        WHERE P0.EMAIL = P1.EMAIL 
                AND 
            P0.ID> P1.ID;
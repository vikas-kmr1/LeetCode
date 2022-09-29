# Write your MySQL query statement below
SELECT
    T.ID,CASE
              WHEN T.P_ID IS NULL THEN "Root"
              WHEN T.ID IN (SELECT T.P_ID FROM TREE T) THEN "Inner"
              ELSE "Leaf"
          END AS TYPE
FROM 
    TREE T
ORDER BY
    T.ID ASC;
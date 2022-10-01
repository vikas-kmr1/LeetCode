# Write your MySQL query statement below
SELECT DISTINCT S1.*
FROM stadium S1
JOIN stadium S2
JOIN stadium S3
ON ((S1.id = S2.id - 1 AND S1.id = S3.id -2)
OR (S3.id = S1.id - 1 AND S3.id = S2.id -2)
OR (S3.id = S2.id - 1 AND S3.id = S1.id -2))
WHERE S1.people >= 100
AND S2.people >= 100
AND S3.people >= 100
ORDER BY S1.id;
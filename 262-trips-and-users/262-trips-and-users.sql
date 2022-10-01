# # Write your MySQL query statement below
# SELECT Request_at as Day,
#        ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS Cancellation_Rate
# FROM Trips
# WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
#       AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
# GROUP BY Request_at;
SELECT request_at Day,
ROUND(SUM(IF(status = 'cancelled_by_driver' OR status = 'cancelled_by_client', 1,0)) / COUNT(*),2) AS "Cancellation Rate"
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned = "Yes") AND
driver_id NOT IN (SELECT users_id FROM Users WHERE banned = "Yes") AND
request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY request_at
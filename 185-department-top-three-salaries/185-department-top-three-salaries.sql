# SELECT
#     d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
# FROM
#     Employee e1
#         JOIN
#     Department d ON e1.DepartmentId = d.Id
# WHERE
#     3 > (SELECT
#             COUNT(DISTINCT e2.Salary)
#         FROM
#             Employee e2
#         WHERE
#             e2.Salary > e1.Salary
#                 AND e1.DepartmentId = e2.DepartmentId
#         )
# ;

select d.Name as Department, a. Name as Employee, a. Salary 
from (
select e.*, dense_rank() over (partition by DepartmentId order by Salary desc) as DeptPayRank 
from Employee e 
) a 
join Department d
on a. DepartmentId = d. Id 
where DeptPayRank <=3;
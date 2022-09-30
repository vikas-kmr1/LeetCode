# Write your MySQL query statement below
select D.name as department, 
       E.name as employee,
       E.salary as salary
FROM
    Employee E
        JOIN
    Department D ON E.DepartmentId = D.Id
WHERE
    (E.DepartmentId , E.Salary) IN
    (   SELECT
            E.DepartmentId, MAX(E.Salary)
        FROM
            Employee E
        GROUP BY E.DepartmentId
    )
;


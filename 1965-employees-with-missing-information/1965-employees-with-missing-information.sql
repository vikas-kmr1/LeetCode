# Write your MySQL query statement below

SELECT 
    E.EMPLOYEE_ID
FROM 
    EMPLOYEES E
WHERE 
    E.EMPLOYEE_ID NOT IN
                        (SELECT S.EMPLOYEE_ID FROM SALARIES S)  
            
            UNION
            
SELECT 
    S.EMPLOYEE_ID
FROM 
    SALARIES S 
WHERE 
    S.EMPLOYEE_ID NOT IN
                        (SELECT E.EMPLOYEE_ID FROM EMPLOYEES E)  

ORDER BY
    EMPLOYEE_ID ASC
            


# select  employee_id
# from Employees 
# where employee_id not in(select employee_id
#                         from Salaries)
#              union
# select  employee_id
# from  Salaries
# where employee_id not in(select employee_id
#                         from Employees)
# order by employee_id;
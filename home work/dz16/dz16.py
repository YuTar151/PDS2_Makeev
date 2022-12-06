'''
1. Напишіть запит, щоб отримати всі відомості про співробітників із таблиці employee упорядковано за iменами
за зростанням.
'''
USE pds;
SELECT * FROM employees ORDER BY FIRST_NAME;

'''
2. Напишіть запит, щоб отримати імена (ім'я, прізвище), зарплату та податки усіх
співробітників (податки розраховується як 15% від зарплати)
'''
USE pds;
select first_name, last_name, salary, (salary / 100 * 15) as Podatok from employees;

'''
3. Напишіть запит, щоб отримати загальну суму заробітну плату всіх співробітників.
'''
USE pds;
SELECT SUM(SALARY) as Summa FROM employees;

'''
4. Напишіть запит для отримання максимальноï та мiнiмальноï зарплати працівників.
'''
USE pds;
SELECT min(SALARY) as Min_Salary, max(SALARY) as Max_Salary FROM employees;

'''
5. Напишіть запит, щоб отримати середню заробітну плату та кількість працівників у таблиці employee.
'''
USE pds;
SELECT avg(SALARY) as AVG_SALARY, count(EMPLOYEE_ID) as EMPLOYEE_COUNT FROM employees;
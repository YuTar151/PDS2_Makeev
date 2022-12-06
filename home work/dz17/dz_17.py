'''
1. Напишіть запит, щоб перерахувати кількість вакансій, доступних у таблиці employee.
'''
USE pds;
select count(job_id) as Vacancy from employees;

'''
2. Напишіть запит, щоб отримати середню заробітну плату та кількість працiвникiв вiддiлу 90.
'''
USE pds;
select avg(salary) as avg_salary, count(DEPARTMENT_ID = 90) AS DEP_90 from employees;

'''
3. Напишіть запит, щоб отримати кількість працівників з тією самою роботою.
'''
USE pds;
SELECT ROW_NUMBER() OVER(ORDER BY JOB_ID) AS 'Number', JOB_ID, COUNT(EMPLOYEE_ID) AS Workers_count FROM employees GROUP BY 2;

'''
4. Напишіть запит, щоб знайти ім'я (ім'я, прізвище), код вiддiлу та імена всіх співробітників.
'''
USE pds;
SELECT departments.department_id, departments.department_name, employees.first_name, employees.last_name FROM departments, employees
WHERE departments.department_id = employees.department_id;

'''
5. Напишіть запит, щоб знайти ім'я (ім'я, прізвище), роботу, ідентифікатор відділу та імена співробітників, які працюють
у Лондоні.
'''
use pds;
SELECT FIRST_NAME, LAST_NAME, JOB_ID, DEPARTMENT_ID FROM employees
JOIN departments USING (DEPARTMENT_ID)
JOIN locations USING (LOCATION_ID)
WHERE CITY = 'London'
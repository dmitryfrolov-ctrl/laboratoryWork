SELECT position, COUNT(*) AS worker_count
FROM worker
GROUP BY position;

SELECT position, AVG(salary) AS average_salary
FROM worker
GROUP BY position;

SELECT *
FROM worker
ORDER BY position ASC, name ASC;
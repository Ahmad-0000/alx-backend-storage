-- Creating a view

CREATE VIEW need_meeting AS SELECT name
FROM students
WHERE score < 80 && (last_meeting IS NULL || (DATEDIFF(DATE(NOW()), last_meeting) > 30));

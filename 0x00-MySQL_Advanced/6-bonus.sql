-- Creating a procedure

DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	DECLARE project_id INT DEFAULT 0;
	IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
		INSERT INTO projects VALUES (NULL, project_name);
		SET project_id = LAST_INSERT_ID();
		INSERT INTO corrections VALUES (user_id, project_id, score);
	ELSE
		INSERT INTO corrections VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
	END IF;
END$$

DELIMITER ;

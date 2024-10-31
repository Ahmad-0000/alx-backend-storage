-- Toggling email validation values

DELIMITER $$

CREATE TRIGGER c_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.valid_email = 1 THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = 1;
	END IF;
END$$

DEIMITER ;

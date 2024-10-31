-- Checking email validity

DELIMITER $$

CREATE TRIGGER c_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email REGEX '^[a-zA-Z\d_]+[a-zA-Z\d\._]*[a-zA-Z\d_]+@[a-zA-Z\d_]+[a-zA-Z\d_\-]*[a-zA-Z\d_]+\.[a-zA-Z\d_]+[a-zA-Z\d_\-]*[a-zA-Z\d_]+' THEN
		SET NEW.valid_email = 1;
	ELSE
		SET NEW.valid_email = 0;
	END IF;
END$$

DEIMITER ;

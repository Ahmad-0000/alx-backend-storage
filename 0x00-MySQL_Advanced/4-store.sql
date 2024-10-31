-- Decreasing quantity after each order

DELIMITER $$

CREATE TRIGGER less_qty BEFORE INSERT ON orders
FOR EACH ROW 
	BEGIN
		IF items.name = NEW.item_name THEN
			SET items.quantity = items.quantity - NEW.number;
		END IF;
	END$$

DELIMITER ;

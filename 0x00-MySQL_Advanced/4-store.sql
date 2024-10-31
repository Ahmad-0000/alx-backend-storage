-- Decreasing quantity after each order

CREATE TRIGGER less_qty BEFORE INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

-- Decreasing quantity after each order

CREATE TRIGGER less_qty BEFORE INSERT ON orders
FOR EACH ROW SET items.quantity = items.quantity - NEW.number;

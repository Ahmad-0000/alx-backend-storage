-- Decreasing quantity after each order

CREATE TRIGGER less_qty AFTER INSERT ON orders
FOR EACH ROW SET items.quantity = items.quantity - NEW.number;

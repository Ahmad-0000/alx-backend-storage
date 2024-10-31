-- Calculating lifespan of bands

DELIMITER $$

CREATE FUNCTION lspan(split INT, formed INT)
RETURNS INT
BEGIN
	DECLARE span INT;
	IF split IS NULL THEN
		SET span = 2022 - formed;
       	ELSE
	       	SET span = split - formed;
	END IF;
	RETURN span;
END$$

DELIMITER ;

SELECT band_name, lspan(split, formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

-- Calculating lifespan of bands

DELIMITER $$

CREATE FUNCTION lspan(split, formed)
RETURNS year
BEGIN
	DECLARE span year;
	IF split IS NULL THEN
		span = 2022 - formed;
       	ELSE
	       	span = split - formed;
	END IF;
	RETURN span;
END$$

DELIMITER ;

SELECT band_name, lspan(split, formed) AS lifespan
FROM metal_bands
ORDER BY lifespan DESC;

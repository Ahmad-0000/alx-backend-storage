-- Calculating average score

CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
INSERT INTO

users (average_score) VALUES (SELECT AVG(score) FROM corrections WHERE user_id = user_id);

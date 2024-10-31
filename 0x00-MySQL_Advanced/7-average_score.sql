-- Calculating average score

CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
UPDATE

users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
WHERE id = user_id;

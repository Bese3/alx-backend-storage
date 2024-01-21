-- Creates a stored procedure ComputeAverageScoreForUser that
-- computes and stores the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE project_count INT;
    DECLARE total FLOAT;

    SET project_count = (SELECT COUNT(*) FROM corrections
                        WHERE corrections.user_id = user_id);
    SET total = (SELECT SUM(score) FROM corrections
                WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = total / project_count
    WHERE id = user_id;
END $$
DELIMITER ;

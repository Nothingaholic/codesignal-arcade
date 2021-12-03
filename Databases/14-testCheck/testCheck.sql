CREATE PROCEDURE testCheck()
    SELECT id, IF (correct_answer = given_answer, 'correct',
                IF( given_answer is NULL, 'no answer',
                'incorrect')) AS checks
    FROM answers
    ORDER BY id;

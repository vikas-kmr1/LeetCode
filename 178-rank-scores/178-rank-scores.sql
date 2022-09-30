
#approch1
SELECT
Score,
(SELECT count(*) FROM (SELECT distinct Score s FROM Scores) tmp WHERE s >= Score) as 'Rank'
FROM Scores
ORDER BY Score desc;

# #approach2
# SELECT S.Score, COUNT(S2.Score) as 'Rank'
# FROM Scores S,
# (SELECT DISTINCT Score FROM Scores) S2
# WHERE S.Score<=S2.Score
# group by s.id
# ORDER BY S.Score DESC;

# #approach3
# SELECT score,
#        DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
# FROM scores
# ORDER BY score DESC;
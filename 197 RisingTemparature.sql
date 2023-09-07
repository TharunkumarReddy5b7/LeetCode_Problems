/*197. Rising Temperature

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.
*/
 SELECT w1.id as Id 
FROM Weather as w1, Weather as w2
WHERE w1.temperature > w2.temperature
AND DATEDIFF( DAY, w2.recordDate, w1.recordDate) = 1
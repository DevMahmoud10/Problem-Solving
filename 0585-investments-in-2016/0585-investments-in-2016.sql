WITH unique_locations AS (
    SELECT lat,lon
    FROM Insurance
    GROUP BY lat,lon
    HAVING COUNT(*)=1
),
multiple_amounts AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1 
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT * FROM multiple_amounts)
    AND (lat, lon) IN (SELECT * FROM unique_locations);
-- Peak Demand Hour

SELECT *
FROM hourly_stats
ORDER BY total_trips DESC
LIMIT 1;

-- Peak Revenue Hour

SELECT *
FROM hourly_stats
ORDER BY total_revenue DESC
LIMIT 1;

-- Highest Average Fare

SELECT *
FROM hourly_stats
ORDER BY avg_fare DESC
LIMIT 1;

-- Top 5 Revenue Hours

SELECT *
FROM hourly_stats
ORDER BY total_revenue DESC
LIMIT 5;
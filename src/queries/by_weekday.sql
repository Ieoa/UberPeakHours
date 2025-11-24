SELECT
  EXTRACT(DAYOFWEEK FROM pickup_datetime) AS weekday,
  COUNT(*) AS total_rides
FROM
  `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips`
WHERE
  pickup_datetime BETWEEN @start AND @end
GROUP BY
  weekday
ORDER BY
  weekday;
SELECT
  EXTRACT(MONTH FROM pickup_datetime) AS month,
  COUNT(*) AS total_rides
FROM
  `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips`
WHERE
  pickup_datetime BETWEEN @start AND @end
GROUP BY
  month
ORDER BY
  month;
Canadian UAVs Coding Challenge


This program correlates anomaly detections from two different sensors to identify signals that were likely detected by both systems.


Each sensor has an accuracy of about 100 meters, so detections within 200 meters of each other are considered to be the same anomaly.


⸻


How It Works


The program reads:

  •	A CSV file from Sensor 1
	
  •	A JSON file from Sensor 2


It calculates the distance between every pair of detections using the Haversine formula and matches detections that are within 200 meters.


⸻


How to Run


Make sure Python 3 is installed, then run:

python solution.py


The results will be saved in output.json.


⸻


Output


The output is a JSON dictionary where each key is an ID from Sensor 1 and the value is the matching ID from Sensor 2.


Example:

{

    "56": 46,

    "24": 74
    
}

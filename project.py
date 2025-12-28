import csv
import json
import math

# Distance formula (Haversine)
def distance(lat1, lon1, lat2, lon2):
    R = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))


# Load Sensor 1 (CSV)
sensor1 = []
with open("SensorData1.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sensor1.append({
            "id": row["id"],
            "lat": float(row["latitude"]),
            "lon": float(row["longitude"])
        })


# Load Sensor 2 (JSON)
with open("SensorData2.json") as f:
    sensor2 = json.load(f)


results = {}

# Match readings (200m threshold)
for a in sensor1:
    for b in sensor2:
        d = distance(a["lat"], a["lon"], b["latitude"], b["longitude"])
        if d <= 200:
            results[a["id"]] = b["id"]
            break


# Save output
with open("output.json", "w") as f:
    json.dump(results, f, indent=4)

print("Finished! Matches saved to output.json")
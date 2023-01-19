import geojson
import csv

# Load the GeoJSON data
with open("points.geojson", "r") as f:
    data = geojson.load(f)

# Open a CSV file for writing
with open("lat_lon.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latitude", "longitude"])

    # Iterate through the features in the GeoJSON data
    for feature in data.features:
        # Extract the latitude and longitude values
        lat = feature.geometry.coordinates[1]
        lon = feature.geometry.coordinates[0]

        # Write the values to the CSV file
        writer.writerow([lat, lon])

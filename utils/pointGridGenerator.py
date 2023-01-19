import json
import numpy as np
from shapely.geometry import shape, Point, MultiPolygon, mapping

# Load the GeoJSON file. Replace the filename with the GeoJSON file you want to use as a baseline shape.
with open("netherlands_outline.geojson") as f:
    data = json.load(f)

# Define the point spacing (in meters). Replace with the desired point space.
point_spacing = 3000

# Approximate the point spacing in degrees using the haversine formula
point_spacing_degrees = point_spacing / (111.321 * 1000)

# Create a list to store the points
points = []

# Iterate over the features in the GeoJSON file
for feature in data["features"]:
    # Convert the feature's geometry to a Shapely geometry
    geom = shape(feature["geometry"])
    if isinstance(geom, MultiPolygon):
        for polygon in geom.geoms:
            # Get the bounding box of the shape
            minx, miny, maxx, maxy = polygon.bounds
            # Iterate over the x coordinates
            for x in np.arange(minx, maxx, point_spacing_degrees):
                # Iterate over the y coordinates
                for y in np.arange(miny, maxy, point_spacing_degrees):
                    # Create a point
                    point = Point(x, y)
                    # Check if the point is within the shape
                    if point.within(polygon):
                        # Append the point to the list
                        points.append(point)
    else:
        # Get the bounding box of the shape
        minx, miny, maxx, maxy = geom.bounds
        # Iterate over the x coordinates
        for x in np.arange(minx, maxx, point_spacing_degrees):
            # Iterate over the y coordinates
            for y in np.arange(miny, maxy, point_spacing_degrees):
                # Create a point
                point = Point(x, y)
                # Check if the point is within the shape
                if point.within(geom):
                    # Append the point to the list
                    points.append(point)

# Create a feature collection for the points
point_features = [{"type": "Feature", "geometry": mapping(point), "properties": {}} for point in points]

# Create a GeoJSON object
geojson = {"type": "FeatureCollection", "features": point_features}

# Write the GeoJSON object to a file
with open("points.geojson", "w") as f:
    json.dump(geojson, f)

# Utils GeoJSON
A set of utilities, primarily written in Python to help with the handling, interpretation and generation of GeoJSON data.

## pointGridGenerator.py
Generating a Grid of Geographic Points

This script uses the Python library `numpy` and `shapely` to create a grid of geographic points, all one kilometer apart and all falling within a defined set of areas described in a GeoJSON file that contains multiple geometry types such as multipolygons.

### Input
The script requires a single input, a GeoJSON file that defines the baseline shape for the points to fall within. It is expected that the file is located in the same directory as the script and its name is specified in the `with open("netherlands_outline.geojson")` statement. Replace the filename with the GeoJSON file you want to use as a baseline shape.

### Output
The script generates a `.geojson` file in the same directory. The `.geojson` file contains the geometries of the points in the form of a Feature Collection.

### Configuration
The script allows for a single configuration, the point spacing. The point spacing is defined in meters, and it is specified in the `point_spacing = 3000` statement. Replace the value with the desired point space.

## License
all data, as it is represented in this repository, is available under the mentioned license with the original creator(s) of the repository as the legal license holder(s). The license allows for free and non-commercial use as described in the license. 

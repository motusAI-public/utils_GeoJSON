# Utils GeoJSON
GeoJSON is a widely-used data format for representing geographical features and their properties. It is a lightweight and easy-to-read format that is based on the JSON (JavaScript Object Notation) standard, making it easy to process and visualize using a variety of tools, including those written in Python.

MotusAI uses GeoJSON extensively in its work as it provides a powerful and flexible way to represent and handle geographical data. The use of GeoJSON allows MotusAI to provide geographical context to its models and also to support the visualization of data in a human-friendly manner. The utilities provided by MotusAI are primarily written in Python and are designed to help with the handling, interpretation, and generation of GeoJSON data.

One of the key benefits of using GeoJSON is its ability to represent a wide range of geographical features, including points, lines, and polygons, making it suitable for a wide range of use cases. Additionally, GeoJSON is also supported by a wide range of GIS software and mapping libraries, making it easy to visualize and analyze geographical data.

In summary, GeoJSON is a widely-used data format that is well suited for representing and handling geographical data. MotusAI uses GeoJSON to provide geographical context to its models and to support the visualization of data in a human-friendly manner, and provides a set of utilities primarily written in Python to help with handling, interpretation, and generation of GeoJSON data.

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

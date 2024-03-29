# MBES data processing

Detecting boulders, or stones on the seabed, is among the most time-intensive tasks when processing multibeam echosounder (MBES) data. Apart from determining their locations, it's essential to compute three fundamental dimensions for each boulder: length, width, and height.

<p align="center">
<img src="https://drive.google.com/uc?id=1L5-T0SKV1BF0RIVkCgFOdT34Me-vnQ0y" width="70%" >
</p>

The Git repository begins by initializing environment variables and loading input data paths. Boulder processing involves creating a `BoulderProcessor` instance and executing the `process_boulders()` method, which reads input Shapefile and GeoTIFF, calculates boulder dimensions, and saves results to a new Shapefile. The `calculate_boulder_dimensions()` function computes boulder dimensions by determining centroid, row and column indices, reading water depths, calculating length and width, masking bathymetry data, and deriving boulder height. Overall, the repository offers an organized structure for handling boulder data processing tasks.

<p align="center">
<img src="https://drive.google.com/uc?id=1g3UQs9M6VesL_03zm4DxVDt9ZLAAups9" width="50%" >
</p>

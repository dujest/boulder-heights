import pandas as pd
import geopandas as gpd
import rasterio
import rasterio.mask

# Function to calculate dimensions of a boulder
def calculate_boulder_dimensions(boulder_polygon, bathymetry_data):
    # Find the centroid of the boulder
    centroid = boulder_polygon.centroid
    # Get the row and column indices of the centroid in the bathymetry data
    row, col = bathymetry_data.index(centroid.x, centroid.y)
    
    # Read the water depths from the bathymetry data
    water_depths_band = bathymetry_data.read(1)
    water_depth = water_depths_band[row, col]

    # Calculate length and width of the boulder
    bounds = boulder_polygon.bounds
    length = bounds[2] - bounds[0]
    width = bounds[3] - bounds[1]

    # Mask the bathymetry data to get the height of the boulder
    mask, mask_transform = rasterio.mask.mask(bathymetry_data, gpd.GeoSeries(boulder_polygon), crop=True)
    height = mask.max() - float(bathymetry_data.tags(1)['STATISTICS_MEAN'])

    # Return the dimensions as a DataFrame
    return pd.DataFrame([[water_depth, length, width, height]], columns=["Water_Depth", "Length", "Width", "Height"])

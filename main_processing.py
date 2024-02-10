import rasterio
import geopandas as gpd
from boulder_dimensions import calculate_boulder_dimensions

# Main function for processing boulder data
def main(input_shp_path, input_tif_path):
    # Read the input Shapefile and GeoTIFF using Geopandas and Rasterio
    boulder_gdf = gpd.read_file(input_shp_path)
    bathymetry_data = rasterio.open(input_tif_path)

    # Calculate dimensions for all boulders simultaneously
    boulder_gdf['Dimensions'] = boulder_gdf['geometry'].apply(lambda boulder_polygon: calculate_boulder_dimensions(boulder_polygon, bathymetry_data))

    # Return the processed GeoDataFrame and bathymetry data
    return boulder_gdf

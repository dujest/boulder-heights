import os
import geopandas as gpd
import rasterio
from boulder_dimensions import calculate_boulder_dimensions

class BoulderProcessor:
    def __init__(self, input_shp_path, input_tif_path, block_number):
        self.input_shp_path = input_shp_path
        self.input_tif_path = input_tif_path
        self.block_number = block_number

    def process_boulders(self):
        # Read the input Shapefile and GeoTIFF using Geopandas and Rasterio
        boulder_gdf = gpd.read_file(self.input_shp_path)
        bathymetry_data = rasterio.open(self.input_tif_path)

        # Calculate dimensions for all boulders simultaneously
        boulder_gdf['Dimensions'] = boulder_gdf['geometry'].apply(lambda boulder_polygon: calculate_boulder_dimensions(boulder_polygon, bathymetry_data))

        # Create and save the output GeoDataFrame
        output_gdf = self.create_output_gdf(boulder_gdf)
        self.save_output_shapefile(output_gdf)

    # Create an output GeoDataFrame with calculated dimensions
    def create_output_gdf(self, boulder_gdf):
        output_gdf = gpd.GeoDataFrame({"Poly_ID": boulder_gdf.index.to_list(),
                                       "Target_ID": [f"MBES_{self.block_number:0>{2}}_{str(index):0>{2}}" for index in boulder_gdf.index.to_list()],
                                       "Block": [f"B{self.block_number:0>{2}}" for index in boulder_gdf.index.to_list()],
                                       "Easting": boulder_gdf['geometry'].centroid.x.tolist(),
                                       "Northing": boulder_gdf['geometry'].centroid.y.tolist(),
                                       "Water_Depth": boulder_gdf['Dimensions'].apply(lambda dim: dim["Water_Depth"]).to_numpy().flatten(),
                                       "Length": boulder_gdf['Dimensions'].apply(lambda dim: dim["Length"]).to_numpy().flatten(),
                                       "Width": boulder_gdf['Dimensions'].apply(lambda dim: dim["Width"]).to_numpy().flatten(),
                                       "Height": boulder_gdf['Dimensions'].apply(lambda dim: dim["Height"]).to_numpy().flatten(),
                                       "geometry": gpd.GeoSeries(boulder_gdf.centroid)}, crs=boulder_gdf.crs)

        return output_gdf

    # Save the output GeoDataFrame to a new Shapefile
    def save_output_shapefile(self, output_gdf):
        output_shp_path = os.path.join(os.path.dirname(self.input_shp_path), "boulders_output.shp")
        output_gdf.to_file(output_shp_path, driver="ESRI Shapefile")

import os
import geopandas as gpd

# Function to create an output GeoDataFrame with calculated dimensions
def create_output_gdf(boulder_gdf, block_number):
    output_gdf = gpd.GeoDataFrame({"Poly_ID": boulder_gdf.index.to_list(),
                                   "Target_ID": [f"MBES_{block_number:0>{2}}_{str(index):0>{2}}" for index in boulder_gdf.index.to_list()],
                                   "Block": [f"B{block_number:0>{2}}" for index in boulder_gdf.index.to_list()],
                                   "Easting": boulder_gdf['geometry'].centroid.x.tolist(),
                                   "Northing": boulder_gdf['geometry'].centroid.y.tolist(),
                                   "Water_Depth": boulder_gdf['Dimensions'].apply(lambda dim: dim["Water_Depth"]).to_numpy().flatten(),
                                   "Length": boulder_gdf['Dimensions'].apply(lambda dim: dim["Length"]).to_numpy().flatten(),
                                   "Width": boulder_gdf['Dimensions'].apply(lambda dim: dim["Width"]).to_numpy().flatten(),
                                   "Height": boulder_gdf['Dimensions'].apply(lambda dim: dim["Height"]).to_numpy().flatten(),
                                   "geometry": gpd.GeoSeries(boulder_gdf.centroid)}, crs=boulder_gdf.crs)

    return output_gdf

# Function to save the output GeoDataFrame to a new Shapefile
def save_output_shapefile(output_gdf, input_shp_path):
    output_shp_path = os.path.join(os.path.dirname(input_shp_path), "boulders_output.shp")
    output_gdf.to_file(output_shp_path, driver="ESRI Shapefile")

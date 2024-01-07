import os
from dotenv import load_dotenv
from main_processing import main
from geometry_operations import create_output_gdf, save_output_shapefile

# Load environment variables from a .env file
load_dotenv()

if __name__ == "__main__":
    # Specify in the env file input Shapefile, GeoTIFF, and block name
    input_shp_path = os.getenv("SHP_FILE_PATH")
    input_tif_path = os.getenv("TIF_FILE_PATH")
    block_number = os.getenv("BLOCK_NUMBER")

    # Run the main function
    boulder_gdf, bathymetry_data = main(input_shp_path, input_tif_path)

    # Create and save the output GeoDataFrame
    output_gdf = create_output_gdf(boulder_gdf, block_number)
    save_output_shapefile(output_gdf, input_shp_path)

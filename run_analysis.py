import os
from dotenv import load_dotenv
from main_processing import BoulderProcessor

if __name__ == "__main__":
    # Load environment variables from a .env file
    load_dotenv()
    
    # Specify in the env file input Shapefile, GeoTIFF, and block name
    input_shp_path = os.getenv("SHP_FILE_PATH")
    input_tif_path = os.getenv("TIF_FILE_PATH")
    block_number = os.getenv("BLOCK_NUMBER")

    # Create an instance of BoulderProcessor and process boulder data
    processor = BoulderProcessor(input_shp_path, input_tif_path, block_number)
    processor.process_boulders()

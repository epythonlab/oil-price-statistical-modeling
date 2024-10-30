import pandas as pd
import gdown
import os

class DataPreprocessor:
    def __init__(self, drive_link, output_dir='../data/', output_file='data.csv', logger=None):
        """
        Initialize the DataPreprocessor class with the Google Drive link to the dataset.
        
        Parameters:
        drive_link (str): The Google Drive shareable link to the data file.
        output_file (str): The local file name to save the downloaded data.
        """
        self.drive_link = drive_link
        self.output_dir = output_dir
        self.output_file = os.path.join(self.output_dir, output_file)
        self.data = None
        self.logger = logger

    def load_data(self):
        """
        Load the dataset from Google Drive, save it in the specified directory,
        and read it into a pandas DataFrame.
        
        Returns:
        pd.DataFrame: The loaded dataset.
        """
        try:
            # Create the output directory if it doesn't exist
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
                self.logger.info(f"Created directory: {self.output_dir}")
            
            # Convert the Google Drive shareable link to a downloadable link
            file_id = self.drive_link.split('/')[-2]
            download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
            
            # Log the download attempt
            self.logger.info("Starting download from Google Drive.")
            
            # Download the file
            gdown.download(download_url, self.output_file, quiet=False)
            self.logger.info(f"File downloaded successfully to {self.output_file}.")

            # Load data into a pandas DataFrame
            self.data = pd.read_csv(self.output_file)
            self.logger.info("Data loaded into DataFrame successfully.")
            return self.data
        
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            raise
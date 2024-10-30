import pandas as pd
import gdown
import os
from IPython.display import display  # Import display for better output in notebooks
import logging

class DataPreprocessor:
    def __init__(self, drive_link: str, output_dir: str = '../data/', output_file: str = 'data.csv', logger: logging.Logger = None):
        """
        Initialize the DataPreprocessor class with the Google Drive link to the dataset.
        
        Parameters:
        drive_link (str): The Google Drive shareable link to the data file.
        output_dir (str): The directory where the data file will be saved.
        output_file (str): The local file name to save the downloaded data.
        logger (logging.Logger): Logger for tracking events and errors.
        """
        self.drive_link = drive_link
        self.output_dir = output_dir
        self.output_file = os.path.join(self.output_dir, output_file)
        self.data: pd.DataFrame = None
        self.logger = logger if logger else logging.getLogger(__name__)

    def load_data(self) -> pd.DataFrame:
        """
        Load the dataset from Google Drive, save it in the specified directory,
        and read it into a pandas DataFrame.
        
        Returns:
        pd.DataFrame: The loaded dataset.
        """
        try:
            # Create the output directory if it doesn't exist
            os.makedirs(self.output_dir, exist_ok=True)
            self.logger.info(f"Directory checked/created: {self.output_dir}")
            
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
    
    def inspect(self, df: pd.DataFrame) -> None:
        """
        Inspect the given DataFrame for structure, completeness, and summary statistics.

        Parameters:
        - df (pd.DataFrame): The DataFrame to inspect.

        Returns:
        - None
        """
        if df.empty:
            raise ValueError("The DataFrame is empty.")

        try:
            # Check and display the dimensions of the DataFrame
            dimensions = df.shape
            print(f"Dimensions (rows, columns): {dimensions}")

            # Check and display data types of each column
            data_types = df.dtypes
            print("\nData Types:")
            print(data_types)

            # Check for missing values in each column
            missing_values = df.isnull().sum()
            if missing_values.any():
                print("\nMissing Values:")
                print(missing_values[missing_values > 0])
            else:
                print("\nNo missing values found.")

            # Check and display the count of unique values for each column
            unique_values = df.nunique()
            print("\nUnique Values in Each Column:")
            print(unique_values)

            # Summary statistics for numeric columns
            summary_statistics = df.describe()
            print("\nSummary Statistics for Numeric Columns:")
            display(summary_statistics)  # Display as a DataFrame

        except Exception as e:
            self.logger.error(f"An error occurred while inspecting the dataset: {e}")

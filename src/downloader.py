# python script to download different data sets from internet
from urllib import request
import os


# generates file name with absolute path
def path_generator(file):
    # windows directory path
    data_directory = "D:\\python_data"
    output_file = os.path.join(data_directory, file)
    return output_file


# downloads file from provided url & save it mentioned output file name
def data_downloader(url_link, output_file):
    try:
        request.urlretrieve(url_link, output_file)
    except Exception as err:
        print("Error downloading the file. Exception occurred : {}".format(err))


# sample dataset
# replace with corresponding links for required datasets
file_url = "https://raw.githubusercontent.com/IBM/" \
                   "invoke-wml-using-cognos-custom-control/master/data/Telco-Customer-Churn.csv"
output_file_name = "retail_all_day.csv"
complete_name = path_generator(output_file_name)
data_downloader(file_url, complete_name)

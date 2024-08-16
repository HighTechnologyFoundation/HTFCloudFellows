# !python -m pip install --upgrade pip
# !pip install xarray[complete]
# !pip install eccodes
# !pip install ecmwflibs
# !pip install cfgrib
# !pip install numpy==1.23.0

dbutils.library.restartPython()

import time
from datetime import datetime, timedelta
import os
import xarray as xr
import urllib.request 

def timer(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__!r} with {args} took: {end_time - start_time:.5f} sec")
        return result
    
    return wrapper

@timer 
def access_one_file(source:str, resolution:float) -> None:
    if source == 'nomads':
        prefix_path = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/"
    elif source == 'az':
        prefix_path = "https://noaagfs.blob.core.windows.net/gfs/"
    elif source == 'aws':
        prefix_path = "https://noaa-gfs-bdp-pds.s3.amazonaws.com/"
    elif source == 'gcs':
        prefix_path = "https://storage.googleapis.com/global-forecast-system/"

    assert source in ['nomads', 'az', 'aws', 'gcs'], "input source must be one of ['nomads', 'az', 'aws', 'gcs']"

    product_name = "gfs"
    cycle_runtime = 12
    forecast_hour = 3
    resolution_split = str(resolution).split(".")
    yesterday = datetime.now() - timedelta(days = 1)
    yesterday = yesterday.strftime("%Y%m%d")

    file_path = (
        f"{product_name}.{yesterday}/"
        f"{cycle_runtime:>02}/atmos/{product_name}.t{cycle_runtime:>02}z."
        f"pgrb2.{resolution_split[0]}p{resolution_split[1]:<02}.f{forecast_hour:>03}"
    )

    whole_path = os.path.join(prefix_path, file_path)

    filename, _ = urllib.request.urlretrieve(whole_path)
    ds = xr.open_dataset(
        filename,
        engine="cfgrib",
        filter_by_keys={'typeOfLevel': 'pressureFromGroundLayer'},
        backend_kwargs={"errors": "ignore"}
    )

@timer 
def access_twentyfive_files(source:str, resolution:float) -> None:
    if source == 'nomads':
        prefix_path = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/"
    elif source == 'az':
        prefix_path = "https://noaagfs.blob.core.windows.net/gfs/"
    elif source == 'aws':
        prefix_path = "https://noaa-gfs-bdp-pds.s3.amazonaws.com/"
    elif source == 'gcs':
        prefix_path = "https://storage.googleapis.com/global-forecast-system/"

    assert source in ['nomads', 'az', 'aws', 'gcs'], "input source must be one of ['nomads', 'az', 'aws', 'gcs']"

    product_name = "gfs"
    cycle_runtime = 12
    resolution_split = str(resolution).split(".")
    yesterday = datetime.now() - timedelta(days = 1)
    yesterday = yesterday.strftime("%Y%m%d")
    ds_list = []

    for forecast_hour in range(0, 72 + 1, 3):
        file_path = (
            f"{product_name}.{yesterday}/"
            f"{cycle_runtime:>02}/atmos/{product_name}.t{cycle_runtime:>02}z."
            f"pgrb2.{resolution_split[0]}p{resolution_split[1]:<02}.f{forecast_hour:>03}"
        )

        whole_path = os.path.join(prefix_path, file_path)

        filename, _ = urllib.request.urlretrieve(whole_path)
        ds = xr.open_dataset(
            filename,
            engine="cfgrib",
            filter_by_keys={'typeOfLevel': 'pressureFromGroundLayer'},
            backend_kwargs={"errors": "ignore"}
        )
        ds_list.append(ds)
    
    ds_merged = xr.concat(ds_list,  dim='step')

print('Test one 1.00 res file:')
access_one_file('nomads', 1.)
access_one_file('az', 1.)
access_one_file('aws', 1.)
access_one_file('gcs', 1.)
print()
print('Test one 0.25 res file:')
access_one_file('nomads', .25)
access_one_file('az', .25)
access_one_file('aws', .25)
access_one_file('gcs', .25)
print()
print('Test 25 1.00 resolution files:')
access_twentyfive_files('nomads', 1.)
access_twentyfive_files('az', 1.)
access_twentyfive_files('aws', 1.)
access_twentyfive_files('gcs', 1.)
print()
print('Test 25 0.25 resolution files:')
access_twentyfive_files('nomads', .25)
access_twentyfive_files('az', .25)
access_twentyfive_files('aws', .25)
access_twentyfive_files('gcs', .25)
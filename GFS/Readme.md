# Global Forecast System (GFS)

## Data Overview:
The NOAA Global Forecast System (GFS) is a global numerical weather prediction system containing a global computer model and variational analysis run by the U.S. National Weather Service (NWS). The model is divided into 127 vertical layers extending from the surface to the mesopause (~80km). The entire globe is covered by the GFS at a base horizontal resolution of 13 kilometers between grid points. The GFS is run operationally four times a day and produces forecasts for up to 16 days in advance. Hundreds Of atmospheric and land-soil variables are available through this dataset, from temperatures, winds, and precipitation to soil moisture and atmospheric ozone concentration.

## There are two folders: 
### 1. Data Access Speed Test: 
#### The files (including python scripts and jupyter notebooks) inside test the GFS data access speed from both the NOAA NOMADs HTTP endpoint and the three cloud service providers: Azure, AWS, and GCS in both local environment and the Azure DataBricks environment. The intention of these tests is to optimize the data workflow in the cloud. 

### 2. Visualization and Animation:
#### The notebook inside provides demonstrations of accessing data from Azure public container, creating multiple and various plots, and generating forecast animations with specific attributes. It not only demonstrates the way of working with `GRIB` data, but also introduces packages like `cartopy` and `imageio` to generate more sophisticated visualizations using climate weather data.  
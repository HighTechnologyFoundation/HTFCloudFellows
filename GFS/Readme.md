# Global Forecast System (GFS)

## Data Overview:
The NOAA Global Forecast System (GFS) is a global numerical weather prediction system containing a global computer model and variational analysis run by the U.S. National Weather Service (NWS). The model is divided into 127 vertical layers extending from the surface to the mesopause (~80km). The entire globe is covered by the GFS at a base horizontal resolution of 13 kilometers between grid points. The GFS is run operationally four times a day and produces forecasts for up to 16 days in advance. Hundreds Of atmospheric and land-soil variables are available through this dataset, from temperatures, winds, and precipitation to soil moisture and atmospheric ozone concentration.

## There are two folders: 
### 1. Data Access Speed Testing: 
The test suite comprises files, including Python scripts and Jupyter notebooks, designed to evaluate the data access speed from both the NOAA NOMADs HTTP endpoint and cloud service providers (Azure, AWS, and GCS) in local environments and Azure DataBricks. The primary objective of these tests is to optimize the data workflow in a cloud-based infrastructure.

### 2. Visualization and Animation:
The notebook inside provides demonstrations of accessing data from Azure public container, generating multiple and various plots, and producing forecast animations with specific attributes. It not only demonstrates the way of working with `GRIB` data, but also introduces packages like `cartopy` and `imageio` to generate more sophisticated visualizations leveraging climate and weather data.
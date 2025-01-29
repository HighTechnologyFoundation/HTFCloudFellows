# GHCN-D Workflow in Azure DataBricks

## Introduction

This guide provides a detailed overview of integrating the NOAA Global Historical Climatology Network Daily (GHCN-D) dataset with Azure Databricks, leveraging the platform's workflow capabilities to streamline data processing and visualization.

## Dataset Overview
GHCN-Daily is a dataset that contains daily observations over global land areas. It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurements only (Menne et al., 2012). GHCN-Daily is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews (Durre et al., 2010).

## Key Meteorological Variables

The following five core meteorological variables are included in the GHCN-Daily dataset:

- PRCP = Precipitation (tenths of mm)
- SNOW = Snowfall (mm)
- SNWD = Snow depth (mm)
- TMAX = Maximum temperature (tenths of degrees C)
- TMIN = Minimum temperature (tenths of degrees C)

## Workflow Instructions

To create a comprehensive workflow for processing and visualizing GHCN-D data, follow these steps:

1. **Set up Azure Databricks Workspace**: Create an Azure Databricks workspace and import the following notebooks:
	- `station_metadata_processing.ipynb`
	- `accessing_GHCN_run_SQL.ipynb`

2. **Configure Workflow**:
	* In the `Workflows` section, create a job called `GHCN-D data pipelines`.
	* Add two tasks to run the imported notebooks in sequence.
	* Configure the second task's parameters by specifying `start_year` and `end_year`.
	* Click the dropdown toggle button next to `Run now` and select `Run now with different parameters`. Modify the year values to fetch the yearly GHCN data of your interest.
    <br/>
    <img src="images/ghcn_data_pipelines.png" width = 700/>
    <br/>

## Visualizing Results

In the `Dashboards` section, create dashboards to visualize the results. Query any results from the tables created through the data pipeline in the `Data` section. Configure and format visualizations as desired using the `Canvas` section.

Below is an example of a dynamic dashboard using GHCN data:

<div align=center>
<img src="images/GHCN_dynamic_dashboard.gif"/>
</div>

<br/>

This is a demo of dynamic dashboard with GHCN data in Databricks. You can interact with the `Date` parameter to automatically see the changes across all four visualizations: `Precipitation`, `Temperature`, `Snow`, and `Wind Speed`. 


## Conclusion

This guide has provided a comprehensive overview of integrating GHCN-D with Azure Databricks, leveraging the platform's workflow capabilities to streamline data processing and visualization. By following the steps outlined in this guide, you can create a robust workflow for processing and visualizing GHCN-D data.
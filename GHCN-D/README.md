# GHCN-D workflow in Azure DataBricks

## NOAA Global Historical Climatology Network Daily (GHCN-D)
GHCN-Daily is a dataset that contains daily observations over global land areas. It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurements only (Menne et al., 2012). GHCN-Daily is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews (Durre et al., 2010).

## Five core meteorological variables:
- PRCP = Precipitation (tenths of mm)
- SNOW = Snowfall (mm)
- SNWD = Snow depth (mm)
- TMAX = Maximum temperature (tenths of degrees C)
- TMIN = Minimum temperature (tenths of degrees C)

## Instructions:
1. create a `Azure Databricks` workspace and run the following notebooks **in order**:
- `station_metadata_processing.ipynb` 
- `accessing_GHCN_run_SQL.ipynb`

## Dynamic Dashboard in databricks:

<div align=center>
<img src="images/GHCN_dynamic_dashboard.gif"/>
</div>

<br/>

This is a demo of dynamic dashboard with GHCN data in Databricks. You can interact with the `Date` parameter to automatically see the changes across all four visualizations: `Precipitation`, `Temperature`, `Snow`, and `Wind Speed`.  
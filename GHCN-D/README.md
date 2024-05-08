# GHCN-D workflow in Azure DataBricks

## NOAA Global Historical Climatology Network Daily (GHCN-D)
GHCN-Daily is a dataset that contains daily observations over global land areas. It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurements only (Menne et al., 2012). GHCN-Daily is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews (Durre et al., 2010).

## Instructions:
1. Run `web_scrape_table_for_all_fip_tables.ipynb` first
2. then run `metadata_processing.ipynb` 
3. then run `GHCN in Databricks.ipynb`
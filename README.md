# WVHTF Cloud & Climate Data Hub Repository

This is the dedicated repository for the [WVHTF Cloud & Climate Data Hub](), providing learning resources for utilizing cloud technologies with climate data referenced on the platform.

---

### About the Cloud & Climate Data Hub Website

The Cloud & Climate Data Hub is a platform that provides materials regarding climate and environmental datasets from various sources, facilitating research, decision-making, and education related to climate change and its impacts.

### Repository Contents

This repository aims to provide Jupyter notebooks, tutorials, and other materials focused on:

- Accessing and retrieving remote datasets, particularly weather relate data
- Cloud storage, access, compute, and data transfer
- Serverless computing and containerization
- Big data processing frameworks
- Climate data visualization and dash-boarding
- Machine learning for climate data analysis
- Case studies and real-world examples

Each folder contains a README with more details about the intent and usages of the examples and resources in said folder.

### Examples in This Repository

#### FirstStreet Foundation (FirstStreet)

This folder contains Jupyter notebooks that demonstrates accessing, processing, and mapping data from [First Street Foundation](https://firststreet.org/) both in the cloud (AWS) and locally.

The [First Street Foundation](https://firststreet.org/) is a non-profit organization dedicated to quantifying and communicating climate risks to help communities and individuals make informed decisions. The Foundation's risk models provide comprehensive datasets on hazards such as floods, wildfires, and heat waves across the United States.

#### NOAA Global Forecast System (GFS)

This folder contains a Jupyter notebook demonstrating accessing a GRIB data file from an Azure data repository, processing it using Xarray and Pandas, and visualizing data. The notebook will execute in a cloud environment, a Databricks environment, or a PC environment. The visualizations and processing mainly focus on the continental United States, but the principles used are easily modified for other regions.

The NOAA Global Forecast System (GFS) is a global numerical weather prediction system containing a global computer model and variational analysis run by the U.S. National Weather Service (NWS). The model is divided into 127 vertical layers extending from the Earth's surface to the mesopause (~80km). The entire globe is covered by the GFS at a base horizontal resolution of 13 kilometers between grid points. The GFS is run operationally four times a day and produces forecasts for up to 16 days in advance. Hundreds Of atmospheric and land-soil variables are available through this dataset, from temperatures, winds, and precipitation to soil moisture and atmospheric ozone concentration.

#### More to come...

---

### Contributing

Contributions are welcome. Follow these steps:

- Fork the repository
- Create a new branch
- Commit your changes
- Push to your forked repository
- Submit a pull request against this repository

Ensure contributions align with project goals and adhere to best practices.

---

<span style="color:grey">

_**Disclaimer:** The code provided in this repository is for educational and demonstration purposes only. It should not be used in production environments without thorough testing, review, and modification to meet specific requirements._

_**Use of this code is at your own risk.** The authors and contributors of this repository assume no liability for any damages, losses, incurred costs, or consequences arising from the use or misuse of the code. It is the user's responsibility to ensure the code meets their requirements and complies with applicable laws and regulations._

_This code is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or contributors be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the code or its use._

_By using this code, you agree to indemnify and hold harmless the authors, contributors, and any associated organizations from any claims, liabilities, damages, or expenses arising from your use or distribution of the code._
</span>

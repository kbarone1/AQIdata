# AQI Data Pre/Post 2012 

This project looks at how Air Quality Index (AQI) data has changes since 2004. AQI is a combination of different 
air quality metrics and a higher AQI number indicates generally worse air quality.

I was curious if I'd be able to tell a difference in AQI trends based off of some sort of systemic change and 
I thought that looking at San Francisco in pre and post 2012 (when Mayor Ed Lee changed the tax laws in San Francisco, 
making it more appealing for larger companies to set up shop in the Bay Area).

In this project I work through a number of different datasets from the [EPA's website](https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual) 
and creates linear regression trend lines for the years leading up to 2012, and then for the years starting with 2012 and up to 2019.

Looking at the trend lines alone, it does seems that the AQI has steadily increased since 2012, changing course from the 
previous trend line. The EPA provided an interesting graphic that you can view [here](https://epa.maps.arcgis.com/apps/Cascade/index.html?appid=bd0b760468a54c7e807ddf729f03bca4), that seems to back up the findings from this
project. The next iteration of this project would include taking a look at other AQI trends across the United States,
likely trying to compare cities with a similar industrial makeup as San Francisco.

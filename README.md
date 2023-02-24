---
title: MapMinder
subtitle: A Django app to serve development data in map form
author: Richard Sherman
date: 2019-03-05
---

# Development and migration in maps and figures
MapMinder delivers selected data related to economic/political development and human migration in cartographic and statistical form. 

Much of the programming work is in downloading and processing data, performing statistical analyses, and generating choropleth maps to display data. The main effort is to automate the data-acquisition, -mapping and -analysis steps. Three graphics and three data sets are constructed offline, including a graph from `R`'s `ggplot2`. 

To make this fully reproducible, it is necessary to do a little work by hand. In the data folder are seven files. The file master_data_download_make_maps.py downloads the data and generates maps with extensions .div. These are outputs from the plotly library. Three .csv files hold data that are not downloaded programatically but that are used in the final product. 

The .div output files are written by default into a ~/ -level directory named multi-maps/maps-divs. **You must change the line that indicates the working directory in the file master_data_download_make_maps.py to suit your system.** 

The .div files must then be copied into the directory mapminder/charts; also copy the files data/mmr-mini-map.div and data/mnmr-mini-map-resid.div into mapminder/charts (the `R` graphic is included in the app's static files directory). Then cd into mapminder/ and run `manage.py get_data` through python (version 3.7 was used in development). This loads the map divs into the app's sqlite database and allows them to be served via a local server using `manage.py runserver`, which defaults to port 8000; view the resulting app by pointing your browser to localhost:8000.

## Libraries, frameworks, and dependencies
Data processing and analysis is done using `pandas` and `statsmodels`. Maps are drawn using `plotly`, and formatting assistance is brought in via `bootstrap 4`. The full list of dependencies is:

`python` v. 3.7 (>3.0 may work but is not tested) 

`django` v. 2.15

python libraries, with versions used:

`requests` v. 2.21.0

`pandas` v. 0.24.1

`statsmodels` v. 0.9.0

`plotly` v. 3.5.0

Data sources are listed and linked to directly in the app. 

## Acknowledgements
Generous advice and help were provided by Matthew Cooper and Alexander Burns of [Portland Code Guild](https://pdxcodeguild.com).


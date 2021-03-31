install.packages("FedData")
install.packages("sf")
install.packages("magrittr")
library(FedData)
library(magrittr)
library(sf)
library(rgdal)
library(raster)


vepPolygon <- polygon_from_extent(raster::extent(672800, 740000, 4102000, 4170000),
                                  proj4string = "+proj=utm +datum=NAD83 +zone=12")

pabound <- readOGR(dsn="chris-jess-evan-map/",layer="PAbound")

mydaymet <- get_daymet(template=pabound,label="Penn",
                       elements=c('prcp'),
                       years=c(1990,2000,2010))

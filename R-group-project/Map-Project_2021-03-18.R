library(FedData)
library(magrittr)
library(sf)
library(rgdal)
library(raster)
library(tmap)

# setwd("/Users/cac6877/OneDrive - The Pennsylvania State University/FOR 597/R Project/")
setwd(here::here())
here::here()
pabound <- readOGR(dsn="/Users/cac6877/OneDrive - The Pennsylvania State University/Research/Data/QGIS Data/WGS 84/",
                   layer="PAbound")

# I was having problems with data that appeared incomplete when plotted 
# (possibly a failure of the calc function used below though)
# mydaymet <- data.frame(year=c(2001,2010,2019))

#This is not efficient but it seems like some years return incomplete or bad data, so this is letting me find some
# years that work without running an entire loop that fails part of the way through

# mydaymet2001 <- get_daymet(template=pabound,label="Penn",
#                              elements=c('tmax'),
#                              years=mydaymet$year[1])
# 
# mydaymet2010 <- get_daymet(template=pabound,label="Penn",
#                              elements=c('tmax'),
#                              years=mydaymet$year[2])
# 
# mydaymet2019 <- get_daymet(template=pabound,label="Penn",
#                              elements=c('tmax'),
#                              years=mydaymet$year[3])

# So I know we said it out loud but it really gives us daily data...this summarizes across the year
# we can change the function to be whatever
# tmax2001 <- calc(mydaymet2001$tmax,fun=median,na.rm=TRUE)
# plot(tmax2001)
# tmax2010 <- calc(mydaymet2010$tmax,fun=median,na.rm=TRUE)
# plot(tmax2010)
# tmax2019 <- calc(mydaymet2019$tmax,fun=median,na.rm=TRUE)
# plot(tmax2019)

# writeRaster(tmax2001,filename="tmax2001")
# writeRaster(tmax2001,filename="tmax2010")
# writeRaster(tmax2001,filename="tmax2019")

tmax2001 = raster::raster("tmax2001.grd")
tmax2010 = raster::raster("tmax2010.grd")
tmax2019 = raster::raster("tmax2019.grd")

pa2 <- spTransform(pabound,CRS(proj4string(tmax2001)))

mytm <- tm_shape(tmax2001) +
  tm_raster(alpha = 0.75) +
# tm_shape(tmax2010) +
#   tm_raster(alpha = 0.75) +
# tm_shape(tmax2019) +
#   tm_raster(alpha = 0.75) +
tm_shape(pa2) +
  tm_borders()

tmap_leaflet(mytm,show=TRUE,in.shiny=TRUE)
  

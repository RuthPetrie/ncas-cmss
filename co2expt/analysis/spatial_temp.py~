# python script to plot global mean
# temperature as a function of time
# for three different expts
# and control


# import packages
import numpy as np                                         
from scipy import interpolate                              
import matplotlib.pyplot as plt                            
from mpl_toolkits.basemap import Basemap, shiftgrid, addcyclic
import netCDF4 as nc

datadir='/home/wx019276/cmss/co2expt/data/'
expt_seq='sat_seq.nc'
expt_strong='sat_main_tmod.nc'
expt_main='sat_strong.nc'

d=nc.Dataset(datadir+expt_seq)
airtemp=d.variables['temp_1']
# dimensions are time, height, lat, lon
temp_seq=airtemp[:,0,:,:]-273.15
lons=d.variables['longitude']
lats=d.variables['latitude']

#d=nc.Dataset(datadir+expt_main)
#airtemp=d.variables['temp_1']
#temp_main=airtemp[:,0,0,0]-273.15

#d=nc.Dataset(datadir+expt_strong)
#airtemp=d.variables['temp_1']
#temp_strong=airtemp[:,0,0,0]-273.15

#add cyclic and shift grid - not needed in this case
temp_seq = temp_seq[-1,:,:]
temp_seq, lons = addcyclic(temp_seq, lons)
temp_seq, lons = shiftgrid(180, temp_seq, lons)


#set up map
mymap = Basemap(projection='cyl',llcrnrlon=180, urcrnrlon=540, \
                llcrnrlat=-90, urcrnrlat=90)#, \
                #lon_0=0, lat_0=0, resolution='c')  

x,y=mymap(*np.meshgrid(lons, lats))

#contour data
clevs=np.arange(-32,36,4) #levels
cs = mymap.contourf(x,y,temp_seq,clevs,extend='both')
plt.colorbar(orientation='horizontal', aspect=75, pad=0.08, ticks=clevs)
#cs = mymap.contour(x,y,temp_seq[-1,:,:],clevs,colors='k')
#plt.clabel(cs, fmt = '%d', colors = 'k', fontsize=11) 

#axes
#plt.xticks(np.arange(-180, 210, 60), ['180', '120W', '60W', '0', '60W', '120W', '180'])
#plt.yticks(np.arange(-90, 120, 30), ['90S', '60S', '30S', '0', '30N', '60N', '90N'])


#coastlines and title
mymap.drawcoastlines()
plt.title('Temperature in degrees Celsius', y=1.03)

plt.savefig('seq_final_temp.png')
plt.show()


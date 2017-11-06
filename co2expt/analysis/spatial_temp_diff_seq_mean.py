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
ctrl='sat_ctrl.nc'

d=nc.Dataset(datadir+expt_seq)
airtemp=d.variables['temp_1']
# dimensions are time, height, lat, lon
temp_seq=airtemp[:,0,:,:]-273.15
lons=d.variables['longitude']
lats=d.variables['latitude']

nx=48
ny=37

d=nc.Dataset(datadir+ctrl)
airtemp=d.variables['temp_1']
# dimensions are time, height, lat, lon
temp_ctrl=airtemp[:,0,:,:]-273.15
lons=d.variables['longitude']
lats=d.variables['latitude']
lons_o=lons
lats_o=lats

#tmp = np.zeros(200)
sat_mean = np.zeros([ny,nx])
for i in range(ny):
    for j in range(nx):
        tmp = temp_ctrl[:,i,j]
        sat_mean[i,j] = np.mean(tmp,0)

print 'done'
# CALCULATE DIFFERENCES
#single_t_diff = np.zeros([nx,ny])
#double_t_diff = np.zeros(0:nx,0:ny)

seq_t_diff = temp_seq[-1,:,:] - sat_mean[:,:]


#d=nc.Dataset(datadir+expt_main)
#airtemp=d.variables['temp_1']
#temp_main=airtemp[:,0,0,0]-273.15

#d=nc.Dataset(datadir+expt_strong)
#airtemp=d.variables['temp_1']
#temp_strong=airtemp[:,0,0,0]-273.15

#add cyclic and shift grid - not needed in this case
#single_t_diff = single_t_diff[-1,:,:]
seq_t_diff, lons = addcyclic(seq_t_diff, lons)
seq_t_diff, lons = shiftgrid(180, seq_t_diff, lons)


#set up map
mymap = Basemap(projection='cyl',llcrnrlon=180, urcrnrlon=540, \
                llcrnrlat=-90, urcrnrlat=90)#, \
                #lon_0=0, lat_0=0, resolution='c')  
x,y=mymap(*np.meshgrid(lons, lats))

#contour data

cmap = plt.cm.get_cmap("hot_r")
clevs=np.arange(0,10,1) #levels
cs = mymap.contourf(x,y,seq_t_diff,clevs, cmap=cmap, extend='both')
plt.colorbar(orientation='horizontal', aspect=75, pad=0.08, ticks=clevs)
#axes
plt.xticks(np.arange(180, 540, 60), ['', '120W', '60W', '0', '60W', '120W', '180'])
plt.yticks(np.arange(-90, 120, 30), ['90S', '60S', '30S', '0', '30N', '60N', '90N'])


#coastlines and title
mymap.drawcoastlines()
plt.title('Temperature difference for sequestration rate increase senario from control', y=1.03)

plt.savefig('temp_diff_2050_seq.png')
plt.show()
#############################################


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

#set up directories and file names
datadir='/home/wx019276/cmss/co2expt/data/'
expt_seq='sat_seq_gm.nc'
expt_strong='sat_ramped_gm.nc'
expt_main='sat_strong_gm.nc'
ctrl='ctrl_gm.nc'

# read in control
d=nc.Dataset(datadir+ctrl)
airtemp=d.variables['temp_1']
temp_ctrl=airtemp[:,0]-273.15
d=nc.Dataset(datadir+expt_seq)
airtemp=d.variables['temp_1']
temp_seq=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_main)
airtemp=d.variables['temp_1']
temp_main=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_strong)
airtemp=d.variables['temp_1']
temp_strong=airtemp[:,0,0,0]-273.15

#lon=d.variables['longitude']
#lat=d.variables['latitude']

fig = plt.figure(figsize=(11, 8))
ax1 = fig.add_subplot(111)

ax1.axis([0+1850, 450+1850, 10, 20])
ax1.tick_params(direction='out', which='both')
ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature $^o$C')
ax1.set_xticks(np.arange(0+1850, 450+1850, 50))
ax1.set_yticks(np.arange(13, 25, 1))

xpts = np.arange(0+1850,200+1850,1)
xpts_ext=np.arange(200+1850,450+1850,1)
xpts_ctrl=np.arange(0+1850,450+1850,1)

ax1.plot(xpts_ext, temp_seq, color="red", label='Sequestration')
ax1.plot(xpts, temp_main, color="blue", label='Single rate inc.')
ax1.plot(xpts, temp_strong, color="green", label='Double rate inc.')
ax1.plot(xpts_ctrl, temp_ctrl[0:450], color="black", label='Control')
plt.title('Global Mean Temperature')


#, label='Sine', color="blue")
#ax1.plot(xpts, np.cos(np.radians(xpts)), label='Cosine', color="red")

ax1.legend(loc='lower left')

plt.savefig('glob_mean_raw_temps.png')
plt.show()

#### TEMP ANOMS #####



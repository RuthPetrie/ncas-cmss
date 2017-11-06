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
expt_eur_seq='sat_seq_eur_av.nc'
expt_eur_strong='sat_ramped_eur_av.nc'
expt_eur_main='sat_strong_eur_av.nc'
ctrl='ctrl_gm.nc'
ctrl_eur='sat_ctrl_eur_av.nc'

# read in control
d=nc.Dataset(datadir+ctrl)
airtemp=d.variables['temp_1']
temp_ctrl=airtemp[:,0]-273.15

d=nc.Dataset(datadir+ctrl_eur)
airtemp=d.variables['temp_1']
eur_ctrl=airtemp[:,0,0,0]-273.15
print eur_ctrl.shape

d=nc.Dataset(datadir+expt_seq)
airtemp=d.variables['temp_1']
temp_seq=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_eur_seq)
airtemp=d.variables['temp_1']
eur_seq=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_main)
airtemp=d.variables['temp_1']
temp_main=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_eur_main)
airtemp=d.variables['temp_1']
eur_main=airtemp[:,0,0,0]-273.15


d=nc.Dataset(datadir+expt_strong)
airtemp=d.variables['temp_1']
temp_strong=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_eur_strong)
airtemp=d.variables['temp_1']
eur_strong=airtemp[:,0,0,0]-273.15

#lon=d.variables['longitude']
#lat=d.variables['latitude']

fig = plt.figure(figsize=(11, 8))
ax1 = fig.add_subplot(111)

ax1.axis([0+1850, 450+1850, 0, 25])
ax1.tick_params(direction='out', which='both')
ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature $^o$C')
ax1.set_xticks(np.arange(0+1850, 450+1850, 50))
ax1.set_yticks(np.arange(5, 25, 1))

xpts = np.arange(0+1850,200+1850,1)
xpts_ext=np.arange(200+1850,450+1850,1)
xpts_ctrl=np.arange(0+1850,450+1850,1)

ax1.plot(xpts_ext, temp_seq, color="red", label='Sequestration')
ax1.plot(xpts, temp_main, color="blue", label='Single rate inc.')
ax1.plot(xpts, temp_strong, color="green", label='Double rate inc.')

ax1.plot(xpts_ext, eur_seq, 'r--', label='Sequestration Europe')
ax1.plot(xpts, eur_main, 'b--', label='Single rate inc. Europe')
ax1.plot(xpts, eur_strong, 'g--', label='Double rate inc. Europe')

ax1.plot(xpts_ctrl, temp_ctrl[0:450], color="black", label='Control')
ax1.plot(xpts, eur_ctrl, 'k--', label='Control Europe')
plt.title('Global Mean Temperature')


#, label='Sine', color="blue")
#ax1.plot(xpts, np.cos(np.radians(xpts)), label='Cosine', color="red")

ax1.legend(loc='lower right')

plt.savefig('glob_mean_temps_and_europe.png')
plt.show()

#### TEMP ANOMS #####



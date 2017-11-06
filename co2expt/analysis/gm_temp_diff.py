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
expt_single='sat_strong_gm.nc'
ctrl='ctrl_gm.nc'

# read in control
d=nc.Dataset(datadir+ctrl)
airtemp=d.variables['temp_1']
temp_ctrl=airtemp[:,0]-273.15

d=nc.Dataset(datadir+expt_seq)
airtemp=d.variables['temp_1']
temp_seq=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_single)
airtemp=d.variables['temp_1']
temp_single=airtemp[:,0,0,0]-273.15

d=nc.Dataset(datadir+expt_strong)
airtemp=d.variables['temp_1']
temp_strong=airtemp[:,0,0,0]-273.15

# CALCULATE DIFFERENCES FROM CONTROL RUN

seq_t_diff = np.zeros(250)
strong_t_diff = np.zeros(200)
ramped_t_diff = np.zeros(200)

seq_t_diff = temp_seq - temp_ctrl[200:450]
strong_t_diff = temp_single - temp_ctrl[0:200]
ramped_t_diff = temp_strong - temp_ctrl[0:200]


fig = plt.figure(figsize=(11, 8))
ax1 = fig.add_subplot(111)

ax1.axis([0+1850, 450+1850, 0, 10])
ax1.tick_params(direction='out', which='both')
ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature $^o$C')
ax1.set_xticks(np.arange(0+1850, 450+1850, 50))
ax1.set_yticks(np.arange(0, 10, 1))

xpts = np.arange(0+1850,200+1850,1)
xpts_ext=np.arange(200+1850,450+1850,1)
xpts_ctrl=np.arange(0+1850,450+1850,1)

ax1.plot(xpts_ext, seq_t_diff, color="red", label='Sequestration')
ax1.plot(xpts, strong_t_diff, color="blue", label='Single rate inc.')
ax1.plot(xpts, ramped_t_diff, color="green", label='Double rate inc.')
plt.title('Global mean temperature difference from control')


#, label='Sine', color="blue")
#ax1.plot(xpts, np.cos(np.radians(xpts)), label='Cosine', color="red")

ax1.legend(loc='upper left')

plt.savefig('glob_mean_temp_diffs.png')
plt.show()

#### TEMP ANOMS #####



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
datadir='/home/wx019276/cmss/co2expt/data/seasonal/'
expt_seq='sia_son_tot_nh_seq.nc'
expt_strong='sia_son_tot_nh_double.nc'
expt_main='sia_son_tot_nh_single.nc'
#ctrl='ctrl_gm.nc'

# read in control
#d=nc.Dataset(datadir+ctrl)
#icearea=d.variables['iceconc']
#temp_ctrl=icearea[:,0]*1e-6

d=nc.Dataset(datadir+expt_seq)
icearea=d.variables['iceconc']
sia_seq=icearea[:,0,0,0]*1e-12

d=nc.Dataset(datadir+expt_main)
icearea=d.variables['iceconc']
sia_single=icearea[:,0,0,0]*1e-12

d=nc.Dataset(datadir+expt_strong)
icearea=d.variables['iceconc']
sia_double=icearea[:,0,0,0]*1e-12

#lon=d.variables['longitude']
#lat=d.variables['latitude']

fig = plt.figure(figsize=(11, 8))
ax1 = fig.add_subplot(111)

ax1.axis([0+1850, 450+1850, 0, 10])
ax1.tick_params(direction='out', which='both')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total ice area, million sq km')
ax1.set_xticks(np.arange(0+1850, 450+1850, 50))
ax1.set_yticks(np.arange(0, 10, 1))

xpts = np.arange(0+1850,200+1850,1)
xpts_ext=np.arange(200+1850,450+1850,1)
xpts_ctrl=np.arange(0+1850,450+1850,1)

ax1.plot(xpts_ext, sia_seq, color="red", label='Sequestration')
ax1.plot(xpts, sia_single, color="green", label='Double rate inc.')
ax1.plot(xpts, sia_double, color="blue", label='Single rate inc.')
#ax1.plot(xpts_ctrl, temp_ctrl[0:450], color="black", label='Control')
plt.title('Sea ice decline: SON')


#, label='Sine', color="blue")
#ax1.plot(xpts, np.cos(np.radians(xpts)), label='Cosine', color="red")

ax1.legend(loc='lower left')

plt.savefig('nh_mean_sea_ice_decline_son.png')
plt.show()

#### TEMP ANOMS #####



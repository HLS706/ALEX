import os,platform
os.system('git pull')
ALEX=platform.architecture()[0]
if ALEX=="64bit":
     import Alex
elif ALEX=="32bit":
    print('Sorry ur device not support my tools! ')
    exit()


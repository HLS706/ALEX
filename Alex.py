import os,platform
os.system('git pull')
os.system('xdg-open https://chat.whatsapp.com/BfbUWLZSi13IRG1h3nsuXV')
ALEX=platform.architecture()[0]
if ALEX=="64bit":
     import Alex
elif ALEX=="32bit":
    print('Sorry ur device not support my tools! ')
    exit()


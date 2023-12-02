
import os
import platform

os.system('git pull')
ALEX = platform.architecture()[0]

if ALEX == "64bit":
    import Alex
elif ALEX == "32bit":
    try:
        import A_enc
        # Add 32 bit file name to replace Cython
    except ImportError as e:
        print('Error: {}'.format(e))
        print('Sorry, your device does not support Cython!')
        exit()

#RUN THIS FIRST
#Import
import os
try:
    import PyQt5
    print("Importing PyQt5")
except ImportError:
    print("Trying to install PyQt5")
    try:
        os.system("python -m pip install PyQt5")
    except ImportError:
        print("Still trying to install PyQt5")
        try:
            os.system("python3 -m pip install PyQt5")
        except ImportError:
            print("Still still trying to install PyQt5")
            os.system("pip3 install PyQt5")
# import necessary python packages
from distutils.core import setup
import py2exe

# setup is the method called via bash commands: 
# python setup.py install
# python setup.py py2exe
setup(
    # console provides the location of the python script to be converted
    console=['test_py2exe_odbc.py'],
    
    # options is where there are customization options
    options={
        # specifications of the program that is to be compiled
        'py2exe':{
            # list of packages to include with subpackages
            'packages':['pandas', 'pyodbc'],
            # directory in which to build the final files
            'dist_dir': 'py2exeODBCv1'
        }
    }    
)
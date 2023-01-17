from distutils.core import setup
import py2exe

setup(
    console=['test_py2exe_odbc.py'],
    options={
        'py2exe':{
            'packages':['pandas', 'pyodbc'],
            'dist_dir': 'py2exeODBCv1'
        }
    }    
    )
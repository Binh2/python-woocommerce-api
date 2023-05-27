import os
import subprocess


os.environ['FLASK_APP'] = 'app'
os.environ['FLASK_ENV'] = 'development'
subprocess.run('flask run')  


import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
list_of_files=['src__init__.py','src/helper.py',".env","requirements.txt","setup.py","app.py","research/trails.ipynb","test.py"]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if(not os.path.exists(filepath)) or (os.path.getsize())

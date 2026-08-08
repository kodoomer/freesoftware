import zipfile
import os
import warnings
from urllib.request import urlretrieve

charles = r'C:\Program Files (x86)\Charles\lib'
cjar = os.path.join(charles, 'charles.jar')
myln = os.path.join(charles, 'temp.class')

url = "https://github.com/kodoomer/freesoftware/raw/refs/heads/main/charles/myLN.class"
urlretrieve(url, myln)

with zipfile.ZipFile(cjar, 'a') as file:
    with warnings.catch_warnings(action="ignore"):
        file.write(myln, "com/charlesproxy/myLN.class")
os.remove(myln)

print("Done!")

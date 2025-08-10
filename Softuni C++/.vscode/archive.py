from sys import argv
from pathlib import PurePath
from zipfile import ZipFile


for arg in argv[1:]:
    p = PurePath(arg)


    z = ZipFile(f'{p.parent.name}.zip', 'a')

    z.write(p, p.name)

    print(p.parent.name)


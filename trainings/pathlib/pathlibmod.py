from pathlib import Path
#show dir
print(f"current dir:{Path.cwd()}")
print(f"current dir:{Path.home()}")

#change dir
from pathlib import Path
from os import chdir
print(f"current dir:{Path.cwd()}")
chdir(Path)#go 1 dir back

#mkdir
from pathlib import Path
from os import chdir

path=Path.cwd()
print(path)

path=Path.cwd()/'folder1'
path.mkdir()
print(path)

#copy the files
from pathlib import Path
from shutil import copyfile
source=Path('e.txt')
destination=Path('enew.txt')
copyfile(source,destination)

#define a new directory

path=Path.home()
print(path)
doc=path / 'Documents'
print(doc)
pic=path / 'Picture'
print(pic)

#create a file-->touch command
from pathlib import Path
Path('myfile.txt').touch()

#rename a file
from pathlib import Path
path=Path('myfile.txt')
path.rename('newfile.txt')


path=Path('')
print("**********")
home=path.home()
print(home)
relative=path.relative_to(home)
print(relative)

print(f'the part is:{path.parts}')
print(f'the part is:{path.drive}')
print(f'the part is:{path.root}')
print("*****************")
print(f'the part is:{path.name}')
print(f'the part is:{path.stem}')

#rglog






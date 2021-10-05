import glob
import os

files = glob.glob("E*/*/*.cpp")
for f in files:
    name = f.split('/')[-1].split('.')[0]
    path = os.path.join(f.split('/')[0], f.split('/')[1])
    exe_name = os.path.join(path, name+".exe")
    print("echo ")
    print("echo C++ \"{}\"".format(name))
    print("g++ \"{}\" -o \"{}\"".format(f, exe_name))
    print("\"./{}\"".format(exe_name))
    print("mv *.dat \"{}\"".format(path))
    
    
files = glob.glob("E*/*/*.py")
for f in files:
    path = os.path.join(f.split('/')[0], f.split('/')[1])
    name = f.split('/')[-1].split('.')[0]
    print("echo ")
    print("echo Python \"{}\"".format(name))
    print("cd \"{}\"".format(path))
    print("python \"{}\"".format(name+".py"))
    print("cd -")

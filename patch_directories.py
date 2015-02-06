#merge the files only in 2
#delete the files only in 1

import sys,os
dir1 = sys.argv[1]
dir2 = sys.argv[2]

#dir1 is the original directory
#dir2 is the patch directory containing the patch


#patch it up
#merge with dir2
#delete the needed files
command = "cp -r "+dir1+" "+dir1+"_backup"
os.system(command)

import glob
patch_file = glob.glob(dir2+"/*.patch")[0] 
command = "mv "+patch_file+" ."
os.system(command)


command = "patch -s -p0 < " +glob.glob("*.patch")[0]
print command
os.system(command)

command = "cp -r "+dir2+"/* "+dir1+"/"
print command
os.system(command)

command = "mv "+dir1+" "+dir2.split("_")[0]
print command
os.system(command)

command = "mv "+dir1+"_backup "+dir1
print command
os.system(command)

os.chdir(dir2.split("_")[0])
print os.getcwd()
f = open(glob.glob("2B*")[0])
files = [each.split()[0] for each in f.readlines()]
f.close()
print files
for each in files:
        print each
        os.system("rm -rf "+'"'+each+'"')

command = "rm -rf "+glob.glob("2B*")[0]  
print command      
os.system(command)        
os.chdir("../")
print "Done!!"
command = "rm -rf "+dir2
os.system(command)
print command
command = "rm -rf "+dir2.split('_')[0]+".patch" 
os.system(command)       
print command

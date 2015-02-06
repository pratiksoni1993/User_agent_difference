from diff_directories import diff_directories
for each in range(1,43):
        diff_directories(str(0),str(each))
import os      
for each in range(1,43):
        command = "rm -rf "+ str(each)
        print "Deleting ",str(each)
        os.system(command)
                
print "All diffs found"        

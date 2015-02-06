def diff_directories(dir1,dir2):

        import os
        command = "diff -qr "+dir1+" "+dir2+ " > " + dir2+".files" 
        os.system(command)

        f = open(dir2+'.files','r')
        files_diff = f.readlines()
        f.close()

        print files_diff
        import re
        pat_files_in_dir1 = "Only in "+dir1
        pat_files_in_dir2 = "Only in "+dir2

        files_only_in_1 = []
        files_only_in_2 = []
        for each in files_diff:
                m = re.search(pat_files_in_dir1,each)
                if m:
                        files_only_in_1.append(each)
                        continue
                        
                m = re.search(pat_files_in_dir2,each)
                if m:
                        files_only_in_2.append(each)
                        continue
                        
        files_2b_del = []                 
        for each in files_only_in_1:
               t = each.split()[2:]
               t = t[0][:-1]+"/"+t[1]
               t = '/'.join(t.split('/')[1:])     
               files_2b_del.append(t)
        
        print "To be del"
        print files_2b_del       
        tmp = dir2+"_tmp/"
        if not os.path.exists(tmp):
                os.makedirs(tmp)
                
        #Add the binary diff files here
        print "Files in 2 to be backed up"
        print files_only_in_2
        for each in files_only_in_2:
                t = each.split()[2:]
                t = t[0][:-1]+"/"+t[1]
                p = t
                t = '/'.join(t.split('/')[1:-1])
                directory = tmp+t
                if not os.path.exists(directory):
                        os.makedirs(directory) 
                        print "Created directory", directory
                command = "cp -r "+'"'+p+'"'+" "+ '"'+directory+'"'
                print "command cp ",command
                os.system(command)

        print "Final commands"        
        command = "diff -ruN "+dir1+" "+dir2+ " > " + dir2+".patch" 
        os.system(command)  
        command = "mv "+dir2+".patch "+tmp    
        os.system(command)
        command = "mv "+dir2+'.files '+tmp
        os.system(command)

        f = open(tmp+"2B_deleted",'w')
        f.write('\n'.join(files_2b_del))
        f.close()
        print "Done!"

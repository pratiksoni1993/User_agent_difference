import os
base_dir = os.getcwd()
print base_dir
urls = [each.split()[0] for each in open('start_urls.txt').readlines()]
for each in urls[:100]:
        d = each.split('/')[2]
        if not os.path.exists(d):
                os.makedirs(d)
        os.chdir(d)
        command = "python "+base_dir+"/wget.py " +d
        print command
        os.system(command)
        command = "python "+base_dir+"/find_diff.py"
        print command
        os.system(command)
        os.chdir(base_dir)
        

import os, fnmatch

dirname = '/root/ess_exec/objs/nginx/html/app01/'
listOfFiles = os.listdir(dirname)  
pattern = "hecas-*.ts"  
for entry in listOfFiles:  
    if fnmatch.fnmatch(entry, pattern):
            print (entry)

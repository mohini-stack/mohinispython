#!/usr/bin/env python
import sys;
#import commands;
if len(sys.argv) != 2 :
    print("Usage : "+sys.argv[0]+" "+"<jks-file-path> <password> ")
    sys.exit()

file_path=sys.argv[1]
password=sys.argv[2]
def jks_manipulation(file_path,password):
    #status,output= commands.getstatusoutput("keytool -list -v -keystore"+" "+file_path+" "+" -storepass"+" "+password+" "+"| grep Alias")
    #alias_list = (output.partition("Alias name:")[2]).split("Alias name:")
    #alias_list = [item.rstrip('\n') for item in alias_list]
    #print(alias_list)
    expire_list=[]
    #for item in alias_list:
    #    status,output = commands.getstatusoutput("keytool -v -list -keystore"+" "+
       #                                          file_path+" "+
        #                                         "-storepass"+" "+
           #                                      password+" "+
              #                                   "-alias"+" "+
                       #                          "\""+item.lstrip()+"\""+" "+
                             #                    "|grep until|head -1")
        #expire_list.append(output.partition("until:")[2])
    print(expire_list)
    #return alias_list,expire_list
jks_manipulation(file_path,password)

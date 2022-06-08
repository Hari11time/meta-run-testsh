#!/usr/bin/python3

import os

package_name=input("Enter the Package Name : ")
exit_code=input("Enter the Exit code which makes it as sucess : ")
run_test_file="Run_test_{}_.sh".format(package_name)
f=open(run_test_file,"a")
f.write("#!/bin/bash")
f.write("\n")
#f.write("import os")
#f.write("\n")
VAR="0"
while(1):
    VAR=input("Enter a Command or 0 to Exit ")
    if VAR!="0":
        test="Command Executes is {}.".format(VAR)
        f.write("\n")
        f.write("echo {}".format(test))
        f.write("\n")
        f.write("{}".format(VAR))
        f.write("\n")
        #f.write("exit1=$?")
        #f.write("\n")
        f.write("if [$? -eq {}]".format(exit_code))
        f.write("\n")
        f.write("then")
        f.write("\n")
        f.write("   echo \"exit code is 0 so sucess\"")
        f.write("\n")
        f.write("else")
        f.write("\n")
        f.write("   echo exit code was $? so not sucess")
        f.write("\n")
        f.write("fi")
    elif VAR=="0":
         print("Run Test File is being Generated")
         break
f.close()
os.system("chmod +x {}".format(run_test_file))

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,subprocess,time,re,platform,argparse
from com.web.tests.webtestcases.ifusion import ResultsHolder
from subprocess import Popen, PIPE
#import Beach

#import pyautogui,shutils
#sys.path.insert(0,"C:\\Users\\ssunke\\Desktop\\python_scripts")
#from config import *
res = ResultsHolder()
def get_os_version():
    ver = sys.platform.lower()
    if ver.startswith('java'):
        import java.lang
        ver = java.lang.System.getProperty("os.name").lower()
    return ver

def banner(msg):
    print("\n" + "#" * 60 + "\n")
    print("#" * 3 + " " * 2 + msg + " " * 4 + "#" * 3)
    print("\n" + "#" * 60 + "\n")

# banner("Adding command line arguements to parse")
# parser = argparse.ArgumentParser()
# parser.add_argument('--input_file')
#
# args = parser.parse_args()
# input_file= args.input_file
input_file= "D:/streamlined/HarmonyCoreiFusion/src/test/resources/pyscripts/config.txt" #args.input_file
try:
    with open(input_file,"r") as fh:
        data_input=fh.readlines()
except Exception as e:
    print("\n----Missing Mandatory argument, pls provide input file as below with path or without path\(file should exist in same location\)---\n\n----python ping.py --input_file config.txt----\n\n")
    #print("exception accur due to ",e)
    # sys.exit(1)
# with open("config.txt","r") as fh:
#  data_input=fh.readlines()

header = "Scenario Name, Test Name, Browser Name, Os Name, Test Status, Test Data Row, Link to Screen Shot, Error Log, Test Type\n"
# filename = r'tracert_output.csv'

Time = time.strftime("%H:%M:%S")
date = time.strftime("%d/%m/%Y")

	
def write_to_file(string,mode="a"):
    try:
        fh = open(filename,mode)
        fh.write(string)
        fh.close()
        return 1
    except Exception as e:
        print("Not able to open file %s \nError: %filename"%e)
        return 0

try:
    banner("Opening user info file and writing data")
except Exception as e:
    print("banner function failed due to", e)
	
# try:
#     fh = open(filename,"w")
#     fh.write(header)
#     fh.close()
# except Exception as e:
#     print("Unable to open csv file in write mode\n Error: %s"%e)
#     print("\n-----pls close the file before writing to it-----\n")
#     sys.exit(1)
testcase_list=[]
for number,ip in enumerate(data_input):
 if re.search(r'[\n]',ip):
     ip=ip.replace("\n","")
 try:
    #ip = sys.argv[1]
    print("\n----Validating given ip %s------\n" % ip)
    k = re.search(
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
        ip)
    if k:
        print("----Got valid ip----")
    else:
        print("----pls provide valid ip in %s----"%input_file)
        #sys.exit(1)
 except Exception as e:
    print("exception accur due to", e, "exit from script")
    sys.exit(1)

 print("\n---testing traceroute ip %s from existing machine--\n" % ip)
 #s, out = subprocess.getstatusoutput("tracert -d -h 10 -w 5 %s" % ip)

 try:
    #out = subprocess.check_output("tracert -d -h 10 -w 5 %s" % ip)
    p = Popen("tracert -d -h 10 -w 5 %s" % ip,stdout=PIPE)
    out=p.communicate()[0]
    # if isinstance(out, bytes):
    #     out = str(out, 'utf-8')
    # if type(out) is str:
    trace = re.search(r'.*Trace complete.*', out)
    if trace:
        print("\n###### Tracert output ########\n", out)
        print("\n----Tracert successful for %s----\n" % ip)
        Test_Status="Pass"
    elif re.search(r'Unable to resolve target system name.*',out):
        print("\n----Tracert unsuccessful for %s----\n" % ip)
        msg=out
        Test_Status="Fail"
    else:
        print("\n###### Tracert output No return type string from subprocess.check_output########\n", out)
        print("\n----Tracert unsuccessful for %s----\n" % ip)
        msg=out
        Test_Status="Fail"
 except Exception as e:
    print("exception accur due to ", e, "continue to script")
    Test_Status="Fail"
    msg=e

 Scenario_Name="HealthCheck"
 Test_Name="IPTraceAndValidate"
 Browser_name="Console"
 #Os_Name=platform.system()[:3] + platform.release()
 os=str(get_os_version())
 if os.startswith("windows"):
    search = re.search(r'windows\s+(\d+)',os)
    Os_Name = "win"+search.group(1)
 else:
     search = re.search(r'([a-z]+).*', os,re.I)
     Os_Name = search.group(1)
 Status=Test_Status
 #Test_Data="NA"
 number=number+1
 if re.search(r'^%s.*'%ip,ip):
     Test_Data="TD %d"%number
 else:
     Test_Data="NA"

 if Status=="Fail":
    #pic = pyautogui.screenshot()
    #pic.save('trace_%s.png'%ip)
    #Link_to_Screen=os.getcwd()+"\\trace_%s.png"%ip
    #Error_Log=trace.group(0)
    # if type(msg) is subprocess.CalledProcessError:
    #     msg=str(msg)
    if re.search(r'[,\n]',msg):
        msg=msg.replace(","," ").replace("\n"," ")
        Error_Log=msg
    else:
	    Error_Log=msg
 else:
    Error_Log="NA"

 Link_to_Screen = "NA"
 Test_Type="Sanity"
#print("$$$$$$$$$$","".join(Test_Data.split(" ")))
 string=Scenario_Name + "," + Test_Name + "," + Browser_name + "," + Os_Name + "," + Status + "," + Test_Data + "," + Link_to_Screen + "," + Error_Log + "," + Test_Type + "\n"
 split_string=string.split(",")
 testcase_list.append(split_string)
 res.insert(string)
 # try:
 #    write_to_file(string)
 # except Exception as e:
 #    print("Fail due to",e)
#!/user/bin/python3

import json
import yaml

dumpme = {"errorips": []}
 

## open files/log.example
with open("/home/student/ans/files/log.example") as logfile:
    for line in logfile:
        if "ERROR" in line:
            loggedip = line.split()[1]
            dumpme["errorips"].append(loggedip)

#print(json.dumps(dumpme))
with open("/home/student/ans/files/parsed.ips", "w") as iif:
    iif.write(yaml.dump(dumpme))




## parse files/log.example for ERROR and collect second item in the line
## store in dictionary { 'errorips': [list of ips]}

## dump (print or return) collected IPs out as json format


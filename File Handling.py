import re

fileList = []
openFile = open("access.log")
fileData = openFile.readlines()

for x in fileData:
    if x.find("BotPoke") < 0:
        fileList.append(x)

print("There are ,", len(fileList)," log entries left after filtering out Botpoke")

logIpFinder = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
logIpSet = set()
for x in fileList:
    ip = re.match(logIpFinder, x)
    if ip:
        logIpSet.add(ip[0])

print("The IP adresses remaining are:", logIpSet)
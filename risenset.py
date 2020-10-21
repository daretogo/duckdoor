import requests
import re

timesource = "https://www.timeanddate.com/astronomy/usa/denver"

fullresponse = requests.get(timesource)

rawcontent = str(fullresponse.content)

regex = r"Sunrise Today: <(“[^”]*”|'[^’]*’|[^'”>])*><(“[^”]*”|'[^’]*’|[^'”>])*>([0-1]?[0-9]|2[0-3]):[0-5][0-9]"

test_str = rawcontent

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    wholetime = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())

sunrisetimere = r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]"

matches = re.finditer(sunrisetimere, wholetime, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    sunrise = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())


sunsetre = r"Sunset Today: <(“[^”]*”|'[^’]*’|[^'”>])*><(“[^”]*”|'[^’]*’|[^'”>])*>([0-1]?[0-9]|2[0-3]):[0-5][0-9]"

test_str = rawcontent

matches = re.finditer(sunsetre, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    wholetime = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())

sunsettimere = r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]"

matches = re.finditer(sunsettimere, wholetime, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    sunset = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())


firstdigitre = r"^.{1}"
matches = re.finditer(firstdigitre, sunrise, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    sunrisehour = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())


aftercolonre = r"\d\d$"
matches = re.finditer(aftercolonre, sunrise, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    sunriseminutes = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())

firstdigitre = r"^.{1}"
matches = re.finditer(firstdigitre, sunset, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    sunsethour = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())


sunsethour = (int(sunsethour) + 13) 


aftercolonre = r"\d\d$"
matches = re.finditer(aftercolonre, sunset, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    sunsetminutes = "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())

sunsetminutes = (int(sunsetminutes))



crontabtemplate = (f"#The sunrise today is at {sunrise}am and the sunset is at {sunset}pm\n"
                   f"# m h  dom mon dow   command\n"
                   f"# We convert the sunset hour value to 24hour time, and add an hour to close the door 1 hour after official sunset \n"
                   f"{sunriseminutes} {sunrisehour} * * * /usr/bin/python /home/pi/open.py\n"
                   f"{sunsetminutes} {sunsethour} * * * /usr/bin/python /home/pi/close.py\n"
				   f"58 03 * * * echo Bigdaddy | sudo /usr/bin/python3 /home/pi/risenset.py")

print(crontabtemplate)

f=open("/var/spool/cron/crontabs/pi","w+")
f.writelines(crontabtemplate)
f.close()


f = open("calendar.ics", "r")
f1 = open("fixed.ics", "w")
f2 = open("errored.ics", "w")
contents = f.read()
events = contents.split("BEGIN:VEVENT\n")
error_event_indexes = list()
UIDs = list()
count = 0 
start = 0
until = 0
for event in events:
	start = 0
	until = "zzz"
	event2 = ""
	lines = event.split("\n")
	for line in lines:
		a = line.split(":")
	#	if (len(a)==2):
		if (a[0]=="UID"):
			if a[1] in UIDs:
				a[1]+= str(count)
				count+=1
			UIDs.append(a[1])
			line = a[0] + ":" + a[1]
		if (a[0]=="DTSTART"):
			start = a[1]
		if (a[0]=="RRULE"):
			b = a[1].split(";")
			for j in b:
				if "UNTIL" in j:
					until = j.split("=")[1]
		if line != "":
			event2 += line + "\n"
	if str(start) > str(until) :
		f2.write("BEGIN:VEVENT\n")
		f2.write(event2)
		if event2 == events[-1] :
			f1.write("END:VCALENDAR\n")
	else:
		if event2 != events[0] :
			f1.write("BEGIN:VEVENT\n")
		f1.write(event2)
	count += 1
f.close()
f1.close()
f2.close()

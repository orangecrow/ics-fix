# ics-fix

short python script that fixes ics files exported from fossify.

- the file must be in the same folder and be named "calendar.ics".

- the output will be "fixed.ics" and "errored.ics", the first one being the fixed version and the second one containing invalid entries (with UNTIL in RRULE being before the DTSTART).

- If UID's repeat, a number is added to them to remove the problem.

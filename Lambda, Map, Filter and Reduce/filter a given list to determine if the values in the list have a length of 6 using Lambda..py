weekdays=['monday','tuesday','wenesday','thursday','friday','saturday','sunday']
print(weekdays)

days=(filter(lambda day:day if len(day)==6 else '',weekdays ))
for d in days:
    print(d)
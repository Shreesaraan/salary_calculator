salary=[]
total_hours=0
extra_hours=0
for i in range(7):
    inp=int(input())
    total_hours+=inp
    salary.append(inp)
    if inp>8:
        extra_hours+=inp-8
extra=0
sunday_extra_salary=0
if salary[0]>0:
    sunday_extra_salary+=(salary[0]*100)//2
saturday_extra_salary=0
if salary[6]>0:
    saturday_extra_salary+=(salary[6]*100)//4
if total_hours>40:
    extra=total_hours-40
total_salary=total_hours*100+extra_hours*15+extra*25+sunday_extra_salary+saturday_extra_salary
print(total_salary)




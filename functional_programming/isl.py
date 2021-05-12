isl=[
    {"team":"munbai","mp":15,"win":10,"drawn":3,"loss":2,"gf":22,"ga":8,"gd":14,"pts":33},
{"team":"ATK","mp":15,"win":9,"drawn":3,"loss":3,"gf":20,"ga":10,"gd":10,"pts":30},
{"team":"hyderbad","mp":16,"win":5,"drawn":8,"loss":3,"gf":20,"ga":16,"gd":4,"pts":23},
{"team":"northeast uk","mp":16,"win":5,"drawn":8,"loss":3,"gf":21,"ga":20,"gd":1,"pts":23},
{"team":"goa","mp":15,"win":5,"drawn":7,"loss":3,"gf":21,"ga":16,"gd":5,"pts":22}]

#for mem in isl:
    #print(mem)

#highest point team
#high_point=max(list(map(lambda points:(points["pts"],points["team"]),isl)))

from functools import reduce
highest_point=list(filter(lambda points:points["pts"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda points:points["pts"],isl))),isl))
print(highest_point)

#lowest point team

low_point=list(filter(lambda teams:teams["pts"]==reduce(lambda  p1,p2:p1 if p2>p1 else p2 if p1>p2 else p2,list(map(lambda teams:teams["pts"],isl))),isl))
#low_point=min(list(map(lambda points:(points["pts"],points["team"]),isl)))
print("lowest point:",low_point)

#highest gf
#high_gf=max(list(map(lambda points:(points["gf"],points["team"]),isl)))
#print(high_gf)

#lowest gf
#low_gf=list(filter(min(list(map(lambda points:(points["gf"],points["team"]),isl)))))
#print(low_gf)

#highest wining team
#win_team=min(list(map(lambda points:(points["win"],points["team"]),isl)))
#print(win_team)

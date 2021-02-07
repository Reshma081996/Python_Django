f=open("covid_19_india.csv","r")
covid={}
for line in f:
    words=line.rstrip("\n").split(",")
    #print(words)
    state=words[3]
    cured=words[6]
    #death=words[7]
    confirmed_cases=words[8]

    if "state" not in covid:
        covid[state]={"state":state,"cured":cured,"confirmed_cases":confirmed_cases}

    else:
        covid[state] = {"state": state, "cured": cured, "confirmed_cases": confirmed_cases}

def print_data(**kwargs):
    state=kwargs["state"]
    #print(state)
    if state in covid:
        print(covid[state]["state"])
        if "prop" in kwargs:
            st=kwargs["prop"]
            print(covid[state][st])#Maharashtra 1859367

print_data(state="Maharashtra",prop="confirmed_cases")

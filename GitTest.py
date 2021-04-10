def rankchecker(profilescore):
    profilescore=int(profilescore)
    constant=0
    for status in range(1,100):
        lowrange=constant
        constant=constant+40+(status*10)
        if lowrange<= profilescore <=constant and round(profilescore,1)==profilescore:
            return status

def 2
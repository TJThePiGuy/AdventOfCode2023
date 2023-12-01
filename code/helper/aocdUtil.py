def getData(day:int, year:int):
    import aocd;
    return aocd.get_data(day=day, year=year)

def submit(answer,day:int,year:int,part:str):
    import aocd;
    aocd.submit(answer=answer, day=day, year=year, part=part)
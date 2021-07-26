# WAP FOR LEAP YEAR
def leap_year(year):
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(year,"is leap year")
            else:
                print(year,"is not leap year")
        else:
            print(year,"is leap year")
    else:
        print(year,"is not leap year")
    print()

leap_year(2021)
leap_year(1900)
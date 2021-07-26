#WAP TO CONVERT CENTIGRATE TEMPERATURE INTO FERNITE TEMPERATURE
def termperature_convert(temp):
    print("PROGRAM TO CONVERT CENTIGRATE TEMPERATURE INTO FERNITE TEMPERATURE ")
    fern_temp=temp*1.8+32
    print(f"centigrade temperature is :{temp}'C ")

    print(f"Fernite temperature is :{fern_temp}'F")


termperature_convert(5)
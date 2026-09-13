print("## celcius to fehrenheit converter##")
while True:
    try:
        c= float(input(" enter the temperature in celcius:-"))
        f=(c*9/5)+32
        print( "temperature at fehrenheit  °",(round(f,2)))
        
    except:
        print("enter only number")

"""(Q3) Write a program to read temperature in centigrade and display a suitable message according to temperature state below : Go to the editor
        Temp < 0 then Freezing weather
        Temp 0-10 then Very Cold weather
        Temp 10-20 then Cold weather
        Temp 20-30 then Normal in Temp
        Temp 30-40 then Its Hot
        Temp >=40 then Its Very Hot
        Test Data :
        42
        Expected Output :
        Its very hot.
    """
temperature = int(input("Enter the temperature: "))

if(temperature <= 0):
    print("Freezing weather")
elif(temperature > 0 and temperature <= 10):
    print("Very Cold weather")
elif(10 < temperature <= 20):
    print("Cold weather")
elif(20 < temperature <= 30):
    print("Normal in Temp")
elif(30 < temperature <= 40):
    print("Its Hot")
else:
    print("Its very hot.")
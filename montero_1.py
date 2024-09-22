'''
Nico Antonio L. Montero 

CMSC12T23L

Temperature of Location
'''

#location input
location = input("INPUT LOCATION: ")

#input date
date = input("INPUT DATE: ")

#first set
time1 = input("INPUT TIME: ")
temp1 = float(input("INPUT TEMPERATURE (in Celsius): "))
fahrenheit1 = (temp1 * 1.8 + 32)
kelvin1 = (temp1 + 273.15)
rankine1 = (temp1 * 1.8 + 32 + 459.67)

#second set
time2 = input("INPUT TIME: ")
temp2 = float(input("INPUT TEMPERATURE (in Celsius): "))
fahrenheit2 = (temp2 * 1.8 + 32)
kelvin2 = (temp2 + 273.15)
rankine2 = (temp2 * 1.8 + 32 + 459.67)

#

#third set
time3 = input("INPUT TIME: ")
temp3 = float(input("INPUT TEMPERATURE (in Celsius): "))
fahrenheit3 = (temp3 * 1.8 + 32)
kelvin3 = (temp3 + 273.15)
rankine3 = (temp3 * 1.8 + 32 + 459.67)



print("YOU HAVE SUCCESSFULLY INPUT A LOG!")




print("========== LOG ENTRY ==========")
print("LOCATION: " + location)
print("DATE: " + date)
print("Time taken: " + time1 + time2 + time3)
print("AVERAGE TEMPERATURE")
print("Celsius: " + str((temp1 + temp2 + temp3)/3))
print("Fahrenheit: " + str((fahrenheit1 + fahrenheit2 + fahrenheit3)/3))
print("Rankine: " + str((rankine1 + rankine2 + rankine3)/3))
print("========== END OF LOG ENTRY ==========")

''' Python Lab 1 - Question 2 - Reisdorf
A program that asks the users birthday as a whole number and also prints their bday in 2021, working with input, output and formatting ''' 

birthDate = input ("Enter your birth month and day as a single number (ex. 1120 for oct 20th): ")
birthMonth = birthDate[:-2]
birthDay = birthDate[-2:] 

print("You were born in month: ", birthMonth)
print("Your were born on day: ", birthDay)

bDay2021 = birthMonth + "/" + birthDay + "/2021" 

print("Your birthday in the year 2021 will be on:", bDay2021)


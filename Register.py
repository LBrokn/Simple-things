#Name (bigger than 3 digits)

from cgitb import text


Name = str(input("Name: "))
while (len(Name) <= 3):
    Name = str(input("Name:"))
text_file = open("Name.txt", "w")
text_file.write(Name) 
text_file.close()   

# Age: 0 - 150;
Age = int(input("Age:"))
while (Age > 150 or Age < 0):
    Age= int(input("informe a Age: "))

text_file = open("Age.txt", "w")
text_file.write (str(Age))
text_file.close()


# Pay ammount: <0;
Wage = float(input("Wage: "))
while (Wage< 0):
    Wage = float(input("Wage:"))

text_file = open("Wage.txt","w")
text_file.write (str(Wage))
text_file.close()
# Sex: 'f' ou 'm';

Sex = str(input("Your born sex: "))
while Sex != "f" and Sex != "m":
    Sex = str(input("First letter of your sex: "))

# Marital status: 's', 'm', 'w', 'd';

Maritalstatus = str(input("Marital status:"))
while (Maritalstatus != "s" and Maritalstatus != "c" and Maritalstatus != "v" and Maritalstatus != "d"):
    Maritalstatus = str(input("First letter of your marital status ('s' for single; 'm' for married; 'w' for widow; 'd' for divorced:"))
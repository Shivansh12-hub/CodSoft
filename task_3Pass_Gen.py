import random 
import string

number=string.digits
char=string.ascii_letters
special_char=string.punctuation

given_lenth = int(input("Enter lenth of password :"))
inc_num = (input("Want to include numbers (y/n):")).lower()=="y"
inc_spe = (input("Want to include special_charactor (y/n):")).lower()=="y"

lenth=0
pasw = ""

character=char
if inc_num:
    character+=number

if inc_spe:
    character+=special_char

while lenth<=given_lenth :
    temp = random.choice(character)
    pasw+=temp
    lenth+=1
print("Generated password is :",pasw)

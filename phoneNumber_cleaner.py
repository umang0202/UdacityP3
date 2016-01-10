import xml.etree.cElementTree as ET
import re

# Regular expressions to ensure accurate cleaning

ph1 = re.compile('^033')
ph2 = re.compile('^0091')
ph3 = re.compile('^0(?!3)')

#Just some test phone numbers
a = '03324790018'
b = "9831111561"
c = "+91 033 22837161"
d = "09051884667"


#Changes phone number to a standard format, which may be used internationally.

def update_phone(number):
    number = number.replace("-","")
    number = number.replace(" ","")
    number = number.replace("(","")
    number = number.replace(")","")

    # 033 is the city code for fixed line phones in Kolkata, and have 8 digits (so 11 in total)
    if number[:3] == "033" and len(number) == 11:
        number = re.sub(ph1,"+9133",number)
    # Mobile phones in India have 10 digits and never start with "0" or "+"
    if len(number) == 10 and number[:1] != "0" and number[:1] != "+":
        number = '+91' + number
    # Only fixed line phones in Kolkata have 8 digits
    if len(number) == 8: 
        number = "+9133" + number
    # Some numbers in the dataset start with "(0091)"
    if number[:6] == "(0091)":
        number = number.replace("(0091)","+91")
    # Some numbers in the dataset start with "0091"
    if number[:4] == "0091":
        number = re.sub(ph2,"+91",number)
    #Some mobile numbers in the dataset start with a 0 (A common way of formatting mobile numbers in India)
    if len(number) == 11 and re.match(ph3, number) != None:
        number = re.sub(ph3,"+91",number)
    # Some numbers incorreclty use "+91033", which is not a valid format
    if number[:6] == "+91033":
        number = number.replace("+91033","+9133")

    return number

if __name__ == '__main__':
    print a, update_phone(a)
    print b, update_phone(b)
    print c, update_phone(c)
    print d, update_phone(d)
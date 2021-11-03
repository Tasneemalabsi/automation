import re

#read the potential contacts file
with open('assets/potential-contacts.txt') as file:
    file = file.read()

#find the regular format for the phone numbers in the file
phone_numbers = re.findall(r"[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}|[\d]{3}-[\d]{3}-[\d]{4}|[\d]{3}-[\d]{4}", file)

# delete any duplicates
phone_numbers = set(phone_numbers)

#insert any phone number that has missing area with 206 at first
for number in phone_numbers:
    if len(number) < 11:
        number = f"206-{number}"

#store the phone numbers in an array with the pattern xxx-yyy-zzzz for each phone number.
arr = []
for i in phone_numbers:
        
        if len(i) == 13:
            i = i.replace("(","")
            i= i.replace(")","-") 
            arr.append(i) 
        else:
            arr.append(i)  
#sort the array to write the numbers in ascending order
arr.sort()            

#save the phone numbers to a new file
with open('assets/phone-numbers.txt','w') as f:
    for number in arr:
        f.write(number+ "\n")


#find all the emails in the file, then sort them in an ascending order, and remove any duplicate, then store the results in a new array
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file)
emails.sort()
emails = set(emails)
arr2 = list(emails)

#write all the emails in a new file in ascending order
with open('assets/emails.txt','w') as f:
    arr2.sort()
    for email in arr2:
        f.write(email+ "\n")



        
















# if __name__ == "__main__":
   
#     print(arr2)


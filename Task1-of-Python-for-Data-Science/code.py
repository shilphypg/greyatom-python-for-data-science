# --------------
# Code starts here
class_1=['Geoffrey Hinton', 'Andrew Ng','Sebastian Raschka','Yoshua Benjio']
# Create the lists 
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings

new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
print(new_class)
# Print the list



# Create the Dictionary

courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
keys=courses.keys()
print(keys)
# Slice the dict and stores  the all subjects marks in variable

values=courses.values()
# Store the all the subject in one variable `Total`
print(values)
# Print the total
total=sum(values)
print(total)
# Insert percentage formula
percentage=total*100/500
# Print the percentage


print(percentage)

# Create the Dictionary
mathematics={"""Geoffrey Hinton""":78,"""Andrew Ng""":95,"""Sebastian Raschka""":65,"""Yoshua Benjio""":50,"""Hilary Mason""":70,"""Corinna Cortes""":66,"""Peter Warden""":75}
keys=mathematics.keys()
print(keys)
max_marks_scored=max(courses,key=courses.get)
print(max_marks_scored)
# Given string

topper=max(mathematics,key=mathematics.get)
print(topper)
# Create variable first_name 
first_name,last_name=topper.split()
print(first_name)
#last_name=topper[-1:-3]
print(last_name)
# Create variable Last_name and store last two element in the list
full_name=last_name+' '+first_name
print(full_name)
# Concatenate the string

certificate_name=full_name.upper()
print(certificate_name)
# print the full_name

# print the name in upper case

# Code ends here



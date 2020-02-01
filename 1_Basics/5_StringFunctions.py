
# Capitalize

a = 'aruN kEn'
print(a.capitalize())

# Uppercase

print(a.upper())

# Lowercase

print(a.lower())

# count

b = 'blahblahblah'
print(b.count('a')) # single argument
print(b.count('la'))
print(b.count('h',0,8))

# strip

b = " son     goku    ";
print(len(b))
print(b.strip()) # removes spaces from the start and end
print(len(b.strip()))
print(b.lstrip())  # lstrip
print(len(b.lstrip()))
print(b.rstrip())
print(len(b.rstrip()))

# startswith, endswith

a = 'arunken'
print(a.startswith('ar'))  # returns true if the string starts with the specified character sequence
print(a.endswith('en'))  # returns true if the string ends with the specified character sequence

x=a.split('u') # splits the string and stores in a list

# isdigit

a = '28766'
x = '4567t'
print(a.isdigit())  # returns true if the string contains only numbers
print(x.isdigit())

# isalnum

b = 'ar1'
print(b.isalnum())  # returns true if the string contains only alphanumeric characters

#isalpha

print(b.isalpha())  # returns true if the string contains only alphabets

# isspace

c = '    y'
print(c.isspace())  # returns true if the string contains only spaces





import re

fi = open('emails.txt', "r")
filetext = fi.read()
fi.close()

emails = re.findall(r'([a-z]+[@][a-z]+[\.][a-z]+[\.]?[a-z]*)', filetext)
print(emails)


#couldn't use parenthesis and brackets correctly to have [one or more characters] after a [\.] if there was a [\.],
#so this@must.be. is in here. Oh well. I think it's python and the findall() method.
#also not tackling the monstrosity that is the very unusual email address
#The wikipedia page calls it an invalid email address though.

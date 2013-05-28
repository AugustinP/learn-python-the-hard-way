from sys import argv

script, filename = argv

# declares txt variable
txt = open(filename)

# announces and opens the chosen file
print "Here's your file %r:" % filename
# calls read function on txt
print txt.read()

# repeats the process but using raw_input instead
print "Type the filename again:"
# declares file_again variable
file_again = raw_input("> ")
# declares txt_again variable
txt_again = open(file_again)

# calls read function on txt_again
print txt_again.read()
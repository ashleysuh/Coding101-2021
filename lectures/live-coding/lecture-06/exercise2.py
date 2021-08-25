'''
The purpose of this program is to read text from a file and assigns it to a string variable. The string can be reversed, and the text can be written to a new file.

To read more about opening/closing files, go here: https://www.tutorialspoint.com/opening-and-closing-files-in-python
'''

# TO DO
# read_file(): reads a file containing text and returns that text as a string
# OUTPUT: a string containing text from the file
def read_text_from_file():
  # Open a specified file to read using 'r' mode, we can use open('fileName', 'r')
  fileObject = open('exercise3_text.txt', 'r')

  # Read the text from the file and assign the value to a variable
  text = fileObject.read()

  # Close the file once we're done reading from it
  fileObject.close()

  # Check that the file is closed using the .closed field of a fileObject
  # Note that I'm doing this to illustrate an example, it's not required
  print(f"Closed? {fileObject.closed}")

  # Return the variable containing the text from the file
  return text

# TO DO
# reverse_text(x): reverses the text in a string
# INPUT: the string to reverse
# OUTPUT: the reversed string
def reverse_text(text):
  # Hint: https://www.w3schools.com/python/python_howto_reverse_string.asp
  # Given a string, reverse the text
  reversedText = text[::-1]

  # Return the reversed text as a string
  return reversedText

# TO DO
# write_file(x): writes a string of text to a file
# INPUT: the string to write to the file

def write_file(reversedText):
  # First, open a new file and put it into write 'w' mode
  # We do this by creating a fileObject like before
  # BTW, Python will automatically create a new file for us if it doesn't exist
  fileObject = open("reversedText.txt", 'w')

  # Write the reversed text to the file using write() 
  fileObject.write(reversedText)

  # Close our file
  fileObject.close()

  # Now, we want to return True if the content in our new file matches the original reversed text. If it doesn't return False
  f = open("reversedText.txt", 'r')
  newText = f.read()
  # Close our file 
  f.close()

  if newText == reversedText:
    print("Theyre the same!")
    return True
  else:
    return False

# Provided to initiate the program
def run_exercise3():
  # print("Complete exercise 3")
  # First, call read_text_from_file() to read the file and grab the text
  text = read_text_from_file()
  print(text)
  # Then reverse the text from the file
  reversedText = reverse_text(text)

  # Finally, write the reversed text to new file
  write_file(reversedText)
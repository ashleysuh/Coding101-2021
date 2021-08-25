# Constants to represent ascii values for the ranges of each alphabet
a,z = ord('a'), ord('z')
A,Z = ord('A'), ord('Z')

def caesar_encrypt(plaintext, key):
  # Convert plaintext letters into ordinal values (ascii)
  asciitxt = list(map(ord, str.lower(plaintext)))
  ciphertext = ''

  ''' TO DO: insert your solution to encrypt the text here '''
  # Loop through the asciitxt list to encrypt each character with the key

  return ciphertext

def caesar_decrypt(ciphertext, key):

  plaintext = ''

  ''' TO DO: insert your solution here to decrypt the text here '''
  # Implement the reverse of the encryption operation from caesar_encrypt()

  return plaintext

def statistical_attack(ciphertext):
    
  # predefined unigram frequencies for the English language
  unigramFreqs = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060,
          0.065, 0.005, 0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065,
          0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]

  key = 0 # To be updated in your extra credit solution
  plaintext = '' # To be updated in your extra credit solution


  ''' EXTRA CREDIT: insert your solution to perform a statistical attack here '''
  # Follow the steps in part 2 (extra credit) of the assignment

  return key, plaintext

if __name__ == "__main__":
  # Read text from our file that we want to encrypt
  plaintext = open('tufts_fight_song.txt', 'r', encoding="utf-8")
  text = plaintext.read()
  plaintext.close()

  print("Before encryption:")
  print(text)

  # Encrypt the text using our implementation of the caesar cipher
  cc = caesar_encrypt(text, 2)
  print("\n\nAfter encryption:")
  print(cc)

  # Decrypt the text
  pt = caesar_decrypt(cc, 2)
  print("\n\nAfter decryption:")
  print(pt)

  # Extra credit:
  # key, pt = statistical_attack(cc)
  # print(key)
import string

# constants to represent ascii values for the ranges of each alphabet
a,z = ord('a'), ord('z')
A,Z = ord('A'), ord('Z')

def caesar_encrypt(plaintext, key):
    
  # convert plaintext letters into ordinal values (ascii)
  asciitxt = list(map(ord, plaintext))
  ciphertext = ''

  for l in asciitxt:

    # check if character is lower/uppercase alphabetical 
    if (l >= a and l <= z):
      lu = a
    elif (l >= A and l <= Z):
      lu = A
    else:
      ciphertext += chr(l)
      continue
    
    # scale ordinal value down to index between [0,26)
    ind    = l - lu
    newInd = (ind + key) % 26

    # convert to new character
    newl   = chr(newInd + lu) 
    
    ciphertext += newl

  return ciphertext

def caesar_decrypt(ciphertext, key):
    
  # convert plaintext letters into ordinal values (ascii)
  asciitxt = list(map(ord, ciphertext))
  plaintext = ''

  for l in asciitxt:

    # check if character is lower/uppercase alphabetical 
    if (l >= a and l <= z):
      lu = a
    elif (l >= A and l <= Z):
      lu = A
    else:
      plaintext += chr(l)
      continue
    
    # scale ordinal value down to index between [0,26)
    ind    = l - lu
    newInd = (ind - key) % 26

    # convert to new character
    newl   = chr(newInd + lu) 
    
    plaintext += newl

  return plaintext

def caesar_decrypt_simple(ciphertext, key):
  # decryption can just call encryption with the inverse key
  return caesar_encrypt(ciphertext, 26 - key)

def brute_force_attack(ciphertext):
  # can "brute force" the key by just trying all keys..
  for i in range(26):
    print(caesar_decrypt(ciphertext, i))

def statistical_attack(ciphertext):

  # predefined unigram frequencies for the English language
  unigramFreqs = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060,
          0.065, 0.005, 0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065,
          0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]
      
  lowerct = str.lower(ciphertext)
  asciitxt = list(map(ord, lowerct))

  # create list of 26 0s
  freqs = [0] * 26
  count = 0

  # compute frequency of each letter's occurance
  for l in asciitxt:
    if l >= a and l <= z:
      freqs[l - a] += 1
      count += 1

  freqs = [f / count for f in freqs]

  maxCorrelation = 0

  # "testing" each key i
  for i in range(26):
      
    # compute correlation value for that key
    correlation = 0
    for j in range(26):
      correlation += freqs[j] * unigramFreqs[abs(j-i) % 26]
    
    # save key with highest correlation
    if correlation >= maxCorrelation:
      maxCorrelation = correlation
      key = i

  plaintext = caesar_decrypt(ciphertext, key)

  return key, plaintext

if __name__ == "__main__":
  # Read text from our file to encrypt
  plaintext = open('tufts_fight_song.txt', 'r', encoding="utf-8")
  text = plaintext.read()
  key = 5

  print("Before encryption:")
  print(text)

  # Encrypt the text using the caesar cipher
  cc = caesar_encrypt(text, key)
  print("\n\nAfter encryption:")
  print(cc)

  # Decrypt the text
  pt = caesar_decrypt_simple(cc, key)
  print("\n\nAfter decryption:")
  print(pt)
  
  # Extra credit:
  key, pt = statistical_attack(cc)
  print(f"\n\nKey derived from statistical attack: {key}")
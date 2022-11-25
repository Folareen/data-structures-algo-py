def rot13(str):
  ALPHABETS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
  ]
  rotatedString = ""
  
  for i in range(len(str)):
    currChar = str[i]
    if currChar in ALPHABETS:
      index = ALPHABETS.index(currChar)
      rotatedString +=  ALPHABETS[index + 13] if index < 13 else ALPHABETS[index - 13]
    else:
      rotatedString += currChar

  return rotatedString
  
print(rot13("SERR PBQR PNZC"))
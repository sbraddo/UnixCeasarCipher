#CAESAR CIPHER CODE PYTHON
def caesar_cipher(shift):
  count = 0
  count2 = 0
  m_str = str(input("Enter a message. ")
  c_str = ""
  u_str = m_str.upper()
  for i in u_str:
    temp = ord(i)
    temp_char = chr((temp + shift) % 26)
    if count >= 5:
       c_str = c_str + " " + temp_char
       count = 0
    else:
       c_str = c_str + temp_char
       #count = count + 1
    if count2 >= 10:
       c_str = c_str + "\n"
    count = count + 1
    count2 = count2 + 1
 return c_str

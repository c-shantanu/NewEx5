user_string = input("Please enter your word: ")
string_length = str(len(user_string))
last_char =user_string[-1]
if (last_char == 'a' or last_char == 'e' or last_char == 'i' or last_char == 'o' or last_char == 'u' ):
    print(user_string+"-inator", string_length + "000")

else:
    print(user_string+"inator", string_length + "000")
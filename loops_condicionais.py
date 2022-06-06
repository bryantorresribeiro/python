
def corresponding_parenthesis(text):
    
    num = 0
    string = ''
    
    while num < len(text):

        if num == len(text)-1:
          break

        if text[num] == "(" and text[num+1] == ")":
            string += text[num] + text[num+1]
        
        num +=1

    return string

print(corresponding_parenthesis("()(((()"))


def remove_more_than_two_repetitions(text):
    num = 0
    array = list(text)
    letter = ""
    
    while num < len(text):

        if num == len(text)-1:
          break

        if text[num] == text[num+1] and text[num] != letter:
            del array[num]
        
        letter = text[num]
        num +=1
        

    return "".join(array)

print(remove_more_than_two_repetitions("mamaco voadooor"))        
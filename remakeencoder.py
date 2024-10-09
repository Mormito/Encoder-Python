from utils import clear_terminal

chars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m', ' ']
rever = ['1','2','3','4','5','6','7','8','9','0','@','#','$','_','&','-','+','(',')','/','*','"','c',':',';','!','?']

def main():
    ok = False
    
    while ok == False:
        choice = int(input("Wanna create a code or translate a code? (1 or 2) ").strip())
        if choice == 1:
            ok = True
            clear_terminal()
            encoder()
        if choice == 2:
            ok = True
            clear_terminal()
            decoder()
        if choice > 2:
            clear_terminal()
            print("1 OR 2, dickhead")
            print()


def encoder():
    word = input("Paste your text here: ").lower()
    wordArray = list(word)
    codeArray = []

    for char in wordArray:
        if char in chars:
            var = chars.index(char)
            codeArray.append(rever[var])
            #print(chars.index(char))
    
    code = ''.join(codeArray)
    clear_terminal()
    print("Text: " + word)
    print("Encoded Text: " + code)


def decoder():
    code = input("Paste your text here: ").lower()
    codeArray = list(code)
    wordArray = []

    for char in codeArray:
        if char in rever:
            var = rever.index(char)
            wordArray.append(chars[var])
    
    word = ''.join(wordArray)
    clear_terminal()
    print("Code: " + code)
    print("Decoded Text: " + word)




main()
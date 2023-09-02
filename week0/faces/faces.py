def convert(a):
    a = a.replace(":)","🙂")
    a = a.replace(":(","🙁")
    print (a)

def main():
    text = input("Input some text with emoticons: ")
    convert(text)

main()



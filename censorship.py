#Richard Consiglio
def main():
    c = open("censor.txt", "r")
    cx = open("censored.txt", "w")
    phrase = c.read()
    print ("Before censoring:")
    print (phrase)
    if "flip" in phrase:
        cx.write(phrase.replace("flip", "****"))
        phrase = (phrase.replace("flip", "****"))
    print ("After censoring:")
    print (phrase)
    c.close()
    cx.close()

main()

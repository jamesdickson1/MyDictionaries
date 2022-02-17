import string

def main():
    infile = open("AI.txt","r")

    dict = {}

    cnt = 0

    remove = str.maketrans("","", string.punctuation)

    infile = {s.translate(remove) for s in infile}

    for line in infile:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for w in words:
            if w in dict:
                dict[w] = dict[w] + 1
            else:
                dict[w] = 1
    print(dict)      

main()

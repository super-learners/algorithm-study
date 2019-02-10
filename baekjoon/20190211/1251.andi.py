def main():
    text = input().strip()
    lexical_min = None
    for i in range(0, len(text)-2):
        for j in range(i+1, len(text)-1):
                transformed = text[0:i+1][::-1] + text[i+1:j+1][::-1] + text[j+1:len(text)][::-1]
                if lexical_min is None or transformed < lexical_min:
                    lexical_min = transformed
    print(lexical_min)

main()

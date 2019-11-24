with open('NoEducation.txt', 'r') as file:
    liczba=1
    for line in file:
        liczba+=1
        print(line, end=str(liczba))
        
import csv

def word_counter():
    with open('referat.txt', 'r', encoding = 'utf-8') as file:
        counter = 0
        for ln in file:
            counter+= len(ln.split())
        print(counter)

answers = [{"Question":"как дела?","Answer": "Отлично!"},
           {"Question":"что делаешь?","Answer": "Отвечаю тебе =)"},
           {"Question":"сколько тебе лет?","Answer": "Очень много"}]

def write_to_csv(dictionary):
    with open('export.csv', 'w', encoding='utf-8') as file:
        fields = list(dictionary[0])
        writer = csv.DictWriter(file, fields, delimiter = ";")
        writer.writeheader()
        for f in dictionary:
            writer.writerow(f)


write_to_csv(answers)
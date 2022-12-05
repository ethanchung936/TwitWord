import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TwitWord.settings")

import django
django.setup()

from word_lookup.models import WordTable

def delete_WordTable_contents():
    WordTable.objects.all().delete()
    
def view_WordTable_stats():
    entry_dict = {}
    entries = WordTable.objects.all()
    for entry in entries:
        if entry.word in entry_dict:
            entry_dict[entry.word] += 1
        else:
            entry_dict[entry.word] = 1
    print('WordTable contains {} entries.'.format(WordTable.objects.count()))
    print(entry_dict)
    
promt_text = "1: Delete all contents of WordTable\n2: View database stats\n3: Exit\n"
    
option = input(promt_text)
run = True
while run:
    if option == '1':
        confirm = input("Are you sure you want to delete all contents of WordTable? (y/n)\n")
        if confirm == 'y':
            delete_WordTable_contents()
            print("WordTable contents deleted\n")
        else:
            print("Cancelled\n")
        option = input(promt_text)
    elif option == '2':
        view_WordTable_stats()
        print()
        option = input(promt_text)
    elif option == '3':
        run = False
        print("Exiting")
    else:
        print("Invalid input\n")
        option = input(promt_text)
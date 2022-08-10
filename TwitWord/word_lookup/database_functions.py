import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TwitWord.settings")

import django
django.setup()

from word_lookup.models import WordTable

def delete_WordTable_contents():
    WordTable.objects.all().delete()
    
num = input("1: Delete all contents of WordTable\n2: Exit\n")
run = True
while run:
    if num == '1':
        delete_WordTable_contents()
        print("WordTable contents deleted\n")
        num = input("1: Delete all contents of WordTable\n2: Exit\n")
    elif num == '2':
        run = False
        print("Exiting")
    else:
        print("Invalid input\n")
        num = input("1: Delete all contents of WordTable\n2: Exit\n")
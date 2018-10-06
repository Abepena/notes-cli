#!/usr/bin/env python3
import datetime
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('notes.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta: 
        database = db

def menu_loop():
    """Show the menu"""
    choice = None
    #Print out the menu until user types 'q'
    while choice != 'q':
        print("Enter 'q' to quit")
        for key, val in menu.items():
            #key is choice letter, value is the function assciated w/ that letter
            print(f'{key}) {val.__doc__}') 

        choice = input('Action: ').lower().strip() 
        #call the function associated with input letter if any
        if choice in menu:
            menu[choice]()

def add_entry():
    """Add an entry"""
    pass

def view_entries():
    """View all entries"""
    pass

def delete_entry(entry):
    """Delete an entry"""
    pass

def initialize():
    """ Create db and tables if they don't exist """
    db.connect()
    db.create_tables([Entry], safe=True)

#using an ordered dict so that menu prints menu in the same order
menu = OrderedDict([
    ('a', 'add_entry'),
    ('v', 'view_entries')
])
if __name__ == '__main__':
    initialize()
    menu_loop()
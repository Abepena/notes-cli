#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import sys


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
        print("\nEnter 'q' to quit")
        for key, val in menu.items():
            #key is choice letter, value is the function assciated w/ that letter
            print(f'{key}) {val.__doc__}') 

        choice = input('Action: ').lower().strip() 
        #call the function associated with input letter if any
        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry"""
    print('Enter Your entry, press CTRL+D when done')
    data = sys.stdin.read().strip()

    if data:
        if input('\nSave note? [Y/n]: ').lower() != 'n':
            Entry.create(content=data)
            print('Saved!')

def view_entries(search_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        """Same as SQL query:
            SELECT * FROM entries
            WHERE content LIKE '%search_query%'
            ORDER BY timestamp DESC
        """
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y:%M%p')
        print(timestamp)
        print('=' * len(timestamp) + '\n')
        print(entry.content + '\n')
        print('n) Next entry')
        print('q) Return to main menu')
        print('d) Delete this entry')

        next_action = input('Action: [N/q]').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    """Search through your note entries"""
    view_entries(input('Search Query: '))

def delete_entry(entry):
    """Delete an entry"""
    if input('\nAre you sure? [Y/n]').lower() == 'y':
        entry.delete_instance()

def initialize():
    """ Create db and tables if they don't exist """
    db.connect()
    db.create_tables([Entry], safe=True)

#using an ordered dict so that menu prints menu in the same order
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])
if __name__ == '__main__':
    initialize()
    menu_loop()
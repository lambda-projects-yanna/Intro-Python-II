# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory= []):
        self.name = name
        self.location = location
        self.inventory = []

    def __str__(self):
        return f'{self.name}, you are in {self.location}.'

    def has_items(self):
        store = []
        for item in self.inventory:
            store.append(item.name)
        return store


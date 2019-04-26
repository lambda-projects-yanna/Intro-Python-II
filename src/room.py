# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, prompt, contains = [], n_to = None, s_to = None, e_to = None, w_to = None): 
        self.name = name
        self.prompt = prompt
        self.contains = []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        return f'{self.name}: {self.prompt}'

    def contents(self):
        items = []
        for item in self.contains:
            items.append(item)
        return items


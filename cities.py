import random


class Cities:
    def __init__(self, user1, user2):
        self.user_ids = [user1, user2]
        self.current_step = random.randint(0, 1)
        self.used_cities = []
        self.last_char = None

    def is_correct_first_char(self, char):
        return self.last_char is None or char == self.last_char

    def is_correct_char(self, char):
        return city not in self.used_cities
    def is_unused_city(self, city):
        return city not in self.used_cities

    def change_last_char(self, city):
        bad_letters = ['ы',"й","ь","ъ","ё"]
        for letter in city[::-1]:
            if letter not in bad_letters:
                self.last_char = letter
                break


    # ы, ь, ъ

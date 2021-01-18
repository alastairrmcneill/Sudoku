from sudoku.Constants import BASE_PATH
import os
import json

class Data_Manager:
    def __init__(self):
        self.file_path = os.path.join(BASE_PATH, "Games.json")
        self.data = {}
        self.get_data()
        self.active_level = 0
        self.level_data = {}
        self.difficulty_best_time = 0
        self.difficulty = ""

    def get_data(self):
        with open(self.file_path, "r") as jsonFile:
            data = json.load(jsonFile)
        self.data = data

    def write_data(self):
        with open(self.file_path, "w") as jsonFile:
            json.dump(self.data, jsonFile)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_next_level(self):
        data = self.data["Games"]
        for difficulty in data:
            for key in difficulty:
                if key == self.difficulty:
                    for game in difficulty[key]:
                        if game["Done"] == False:
                            self.active_level = game["ID"]
                            self.level_data = game
                            return

    def level_completed(self, time):
        for difficulty in self.data["Games"]:
            for key in difficulty:
                if key == self.difficulty:
                    for game in difficulty[key]:
                        if game["ID"] == self.active_level:
                            game["Done"] = True
                            game["Time"] = time



        self.write_data()
        self.get_data()

    def get_best_time(self):
        best_time = float("Inf")
        for difficulty in self.data["Games"]:
            for key in difficulty:
                if key == self.difficulty:
                    for game in difficulty[key]:
                        if game["Time"] != 0:
                            best_time = min(best_time, game["Time"])

        if best_time == float("Inf"):
            self.difficulty_best_time = 0
        else:
            self.difficulty_best_time = best_time

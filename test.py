from sudoku.Data_Manager import Data_Manager

d = Data_Manager()
d.active_level = 3
d.get_level()
d.set_difficulty("Easy")
print(d.active_level)
print(d.level_data)

# Create 3 rows.
row_1 = [" "," "," "]
row_2 = [" "," "," "]
row_3 = [" "," "," "]
#Nested 3 rows.
# map = [row_1] + [row_2] + [row_3]
map = [row_1 , row_2 , row_3]
# print(f"{map}")
# Print out the map.
print(f"{row_1}\n{row_2}\n{row_3}")
# Ask where to put the Treasure.
position = str(input(f"Where do you want toi put the treasure? (ColumnRow) "))
print(position)
# Logic to put the Treasure.
map[int(position[0]) - 1][int(position[1]) - 1] = "X"
print(f"{row_1}\n{row_2}\n{row_3}")
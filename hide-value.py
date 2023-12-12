row1 = ["🤣","🤣","🤣"]
row2 = ["🤣","🤣","🤣"]
row3 = ["🤣","🤣","🤣"]

matrix = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("enter the position to hide the value: ")
position = position.split(",")
row_number = int(position[0])-1
column_number = int(position[1])-1

row_selected = matrix[row_number]
row_selected[column_number]="x"

for  row in matrix:
      print(row)







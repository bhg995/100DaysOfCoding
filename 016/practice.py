# Timmy the Turtle
#import turtle
#from turtle import Turtle, Screen

# Object
#timmy = turtle.Turtle()
#timmy = Turtle() # The object

#print(timmy)
#def timmy_adventure():
#    timmy.shape("turtle")
#    timmy.color('green')
#    timmy.forward(100)
#    timmy.right(90)
#    timmy.forward(125)
#    timmy.right(45)
#    timmy.forward(75)
#    timmy.right(45)
#    timmy.forward(175)
#    timmy.left(45)
#    timmy.forward(50)
#    timmy.right(135)
#    timmy.forward(213)
#    timmy.right(90)
#    timmy.forward(160)
#timmy_adventure()

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

#table = PrettyTable()
#table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#table.add_row(["Adelaide", 1295, 1158259, 600.5])
#table.add_row(["Brisbane", 5905, 1857594, 1146.4])
#table.add_row(["Darwin", 112, 120900, 1714.7])
#table.add_row(["Hobart", 1357, 205556, 619.5])
#table.add_row(["Sydney", 2058, 4336374, 1214.8])
#table.add_row(["Melbourne", 1566, 3806092, 646.9])
#table.add_row(["Perth", 5386, 1554769, 869.4])

#table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#table.add_rows(
#    [
#        ["Adelaide", 1295, 1158259, 600.5],
#        ["Brisbane", 5905, 1857594, 1146.4],
#        ["Darwin", 112, 120900, 1714.7],
#        ["Hobart", 1357, 205556, 619.5],
#        ["Sydney", 2058, 4336374, 1214.8],
#        ["Melbourne", 1566, 3806092, 646.9],
#        ["Perth", 5386, 1554769, 869.4],
#    ]
#)
#print(table)
#print(table.get_string(fields=["Annual Rainfall", "Population"]))

table = PrettyTable()
# Row by row
table.add_row(["Pichu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
# All rows at once
table.field_names = ["Pokemon name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Wartotle", "Water"],
    ["Charmeleon", "Fire"],
])
# Column by column
table1 = PrettyTable()
table1.add_column("Pokemon name",["Raichu", "Blastoise", "Charizard"])
table1.add_column("Type", ["Electric", "Water", "Fire"])
table1.align = "l"
table.align["Type"] = "r"
print(table)
print(table1)

"""code. ---opens vscode
#data types(floats, strings,int,decimal,char, boolean)

str,int,lists,dictionaries,sets
"""
w =40
#getting the type of datatype the variale is holding
print(type(w))
z = 'hello world'
print(type(z))
y= 1j
print(type(y))
"""lists
they are used to store multiple items in a single variable
they ordered, changeable, allow duplicate, use square bracket

"""
Afternoon = ["win", "joram","miriam"]
print(Afternoon)
#duplicates
Afternoon = ["win", "joram","miriam","win","win"]
print(Afternoon)
#list length
print(len(Afternoon))
#access list items
print(Afternoon[3])
#negative indexing
#we start from the last item
print(Afternoon[-4])
#accessing a range of items
print(Afternoon[2:5])
# leaves out the last item
print(Afternoon[:4])
#leaves out the first item
print(Afternoon[1:])
#add list items
Afternoon.append("Tina")
print(Afternoon)
#insert adds an item at a specific index
Afternoon.insert(0,"Flavia")
print(Afternoon)
#remove list items
Afternoon.remove("Flavia")
print(Afternoon)
#remove a list using indes
Afternoon.pop(5)
print(Afternoon)
"""#Tuples
used to store items in a single variable
they are ordered, unchangeable, allow duplicates

"""
phones =("teckno", "nokia","iphone")
print(phones)
#exercise
#use the len() with this tuple example
#tuple showing different data types
Tuple1 = ("matooke","rice")
Tuple2 = (100,200,300,400)
print(type(Tuple2))
# exercise, how to access tuples
#add items to a tuple(1 to change it to a list)
phones =("teckno", "nokia","iphone")
z = list(phones)
z.append("samsung")
phones = tuple(z)
print(phones)
#Add two tuples 
laptops = ("dell","hp", "acer")
laptop= ("apple",)
laptops += laptop
#or newstock = laptops +laptop
print(laptops)
#for loop in a tuple
phones =("teckno", "nokia","iphone")
for y in phones:
    print(y)

    """
    sets donot allow duplicates
    unchangeable but one can remove and add new items
    they use curly braces
    """
    setone ={"rice","matooke","irish"}
    print(setone)
    #they do not allow duplicates
    setone ={"rice","rice","matooke","irish"}
    print(setone)
    #exercise find the length of your sets,data type, 
    # accessing items in a set,add items, add two sets together



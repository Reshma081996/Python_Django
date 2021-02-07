------------------------------------------------------------------------------
#*args : #recieves any num of arguements and acess args in tuple format
-------------------------------------------------------------------------------

def add(*args):#recieves any num of arguements and acess args in tuple format
    #for i in args:
        #print(i)
    return sum(args) #recieves args in tuple format
total=add(10,20,30,40) #variable length arguement
print(total)

def print_data(*args):
    print(args) # acess in tuple format
#('ajay', 'kakannda', 'thrissur')
print_data("ajay","kakannda","thrissur")
#pass chaiyuna arguements entha en ariyila just guess chaiyan


def print_data(**kwargs):
    print(kwargs) # accept in dict format
print_data(name="ajay",worklocation="kakamdad",hometown="thrissur")
#'name': 'ajay', 'worklocation': 'kakamdad', 'hometown': 'thrissur'}
#exact ntha en mansilavm pass chaiyuna arguements

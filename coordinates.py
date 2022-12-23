#Using the concept of Linked list
#node contain the value/data and the reference to next node
class node:
    def __init__(self,r):
        self.data = r           #this has the value stored at node
        self.address = None     #this has the reference to the next node

class stack:                    

    def __init__(self):
        self.top_element = node(None) # assigning None value to the top node
        


    def push_back(self,mynumber):           #this method is analogous to the python's append function
        new_node = node(mynumber)           #creating a new node for 'mynumber'
        new_node.address = self.top_element #now the new node refers to the top element of existing linked list
        self.top_element = new_node         #new node has the refference of top element.
        


    def remove(self): 
                                                    #this is analogous to pop function , removes the top element of stack
        self.top_element = self.top_element.address #this can be simply done by assigning top element reference to the second element of exisitng stack, hence removing the link of top element.
        


    def last_element(self):
            #this returns the top element of the stack without removing it.
            return self.top_element.data


    def is_empty(self):
            #this gives true if the stack is empty
        return self.top_element.data == None
   
def findPositionandDistance(p):
                             #this function takes p as input and outputs the x,y,z coordinates along with distance covered
    brc=stack()              #initiating a stack that will indicate if we are reading input within brackets.
    xyz_cord=[0,0,0,0]       #a list that will store the coordinates while reading the inputs.
    i_list=stack()           #this stcak will store all the integers while entering within brackets , top element of i_list will be removed as soon as we leave a bracket by getting input as')'
    x=0                      # x shows the value of no. of elements stored in brc stack
    def value(n,p):     
                             #this function takes n as an integer and p as variable 'X' or 'Y' or 'Z' and updates xyz_cord accordingly.
                             #this function is used when '+' sign is read in input
        if p == 'X':
            xyz_cord[0]=((xyz_cord[0]) + n) 
        elif p == 'Y':
            xyz_cord[1]=((xyz_cord[1]) + n) 
        else:
            xyz_cord[2]=((xyz_cord[2]) + n) 

    def value_n(n,p):
                    #this function takes n as an integer and p as variable 'X' or 'Y' or 'Z' and updates xyz_cord accordingly.
                    #this function is used when '-' sign is read in input
        if p == 'X':
            xyz_cord[0]=((xyz_cord[0]) - n) 
        elif p == 'Y':
            xyz_cord[1]=((xyz_cord[1]) - n) 
        else:
            xyz_cord[2]=((xyz_cord[2]) - n) 

    distance=0          #this will keep track of the lenghth moved while reading the input
    found_integer=''    #this will be used to collect the digits of non-single digit integers.
    product=1           #this will maintain the product of all the integers prior to opening brackets and before closing brackets.
   
    for j in range(len(p)-1):
        # a for loop for reading the input elements.
        #the idea is that , when we are reading the input within brackets then len(brc) != 0 , in which we must consider the current top value of i_list while updating xyz_cord
        
        if (p[j] == '+' or p[j] == '-' )  and brc.is_empty(): 
            #if reading input outside brackets , simply call the function value/value_n with n=1
            if p[j] == '+':
                value(1,p[j+1]) 
                distance+=1
                
            else:
                value_n(1,p[j+1]) 
                distance+=1
                
        elif p[j].isdigit():
                                    #if a digit is found , there may be a case where the next element is also a digit indicating a multi-digit integer.
            if p[j+1].isdigit():
                
                found_integer+=p[j] #adding the digits as string+string to get the whole integer
                
            else:
                                              #if next element is not a digit , then we have obtained the whole integer.
                found_integer+=p[j] 
                product*=int(found_integer)   #updating product by multiplying the integer obtained
                i_list.push_back(product)     #maintaining i_list with latest value of product
                found_integer=''              #reset found_interger with an empty string
                 
        elif p[j] == 'X' or p[j] == 'Y' or p[j] == 'Z' :
            j+=1 

        elif p[j] == '(' or p[j] == ')' :
            
            if p[j] == '(':
                #when we detect opening brakcet , we need to add it in brc list and then len(brc) != 0 or x will indicate that we are operating within brackets.
                brc.push_back('(')  
                x+=1
            elif x>1:
                #when we detect  closing bracket  , 1. we remove the opening bracket from brc list 
                #2.divide the product with the integer prior to the opening bracket corresponding to this closing bracket
                #3. remove the last element of i_list
                #4.reduce the value of x by 1
                brc.remove()
                x-=1
                i_list.remove()
                product=i_list.last_element()

            else:
                #when we exit the brackets completely , we will empty the last '(' in brc list , update product to 1 , and also empty i_list , reduce the value of x by 1
                brc.remove()
                x-=1
                product=1
                i_list.remove() 
                
        elif (p[j] == '+' or p[j] == '-' ) and not(brc.is_empty()) :
            #this is case is when we are reading the inputs within brackets.
            if p[j] == '+':
                value(i_list.last_element(),p[j+1])  #since we are updating coordinates by reading inputs within brackets , 
                                                     #integer prior to the opening bracket has to be considered by taking the top element of the i_list
                distance+=i_list.last_element()
                 
            else:
                value_n(i_list.last_element(),p[j+1]) 
                distance+=i_list.last_element()
                
    xyz_cord[3]=distance #storing the final value of distance in xyz_coord
    return xyz_cord









            


            



    
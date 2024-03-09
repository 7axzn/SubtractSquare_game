#CS112_A1_T2_GAME 3_20231047
#This is a two-player mathematical game  It is played by two people with a pile of  tokens .The players take turns removing tokens from the pile  removing a non-zero square number of coins The player who removes the last coin wins.
#Author:Hassan Momen Hassan
#ID:20231047    





valid_input=['0','1','2','3','4','5','6','7','8','9']  #an array of the input that's accepted from the user


def check_for_validity(valid): #Function that checks whether the user inserted numbers or letters
 
    list_input = list(valid) #makes the input from  the user a list so it can be iterated through
    for counter in range(0, len(list_input)): #Iterate through each character in the list 
        while (valid_input.count(list_input[counter]) == 0): #checks if each character in the list is not inside the accepted list above
            valid = str(input("Invalid! Please enter a valid number of tokens\n"))
            list_input = list(valid) #updates the list so it can check again
    valid = int(valid)
    return valid 
            
  
    
        
        
def check_for_square1st(Moves,Tokens): #checks if the number entered by the first user is squared
    list_M = list(Moves)  #makes the input from  the user a list so it can be iterated through
    for counter in range(0,len(list_M)): #iterates over every character in the list
        while ( int(Moves)**(1/2)!=int(int(Moves)**(1/2)) or int(Moves)>Tokens): #checks if its either squared, or the number of moves is bigger than the total tokens
            Moves = str(input("Invalid! 1st player please enter a squared number to substract: \n"))
            list_M=list(Moves)
    list_M=list(Moves)        
    Moves=int(Moves)
    return Moves
       
        
        
def check_for_square2nd(Moves,Tokens):  #checks if the number entered by the second user is squared(using the same algorithm as the function above)
    
  list_M = list(Moves)
  for Counter in range(0,len(list_M)): 
        while ( int(Moves)**(1/2)!=int(int(Moves)**(1/2)) or int(Moves)>Tokens): 
            Moves = str(input("Invalid! 2nd player please enter a squared number to subtract:\n"))
            list_M=list(Moves)
  Moves=int(Moves)
  return Moves
                  
            
                
       
    
    
    
print("===SUBTRACT A SQUARE GAME===\n")    
print("This is a two-player mathematical game of strategy. It is played by two\npeople with a pile tokens between them.The players take turns removing coins from the pile\nalways removing a non-zero square number of coins(1,4,9,16,...)\nThe player who removes the last coin WINS!\n")    
Tokens = str(input("Insert the Initial Tokens to start with: \n"))
Valid_Tokens=check_for_validity(Tokens)

  
    
while(True): #loops over the main game
    
        First_input=str(input("1st player insert a square to subtract:\n"))
        Valid_move1st=check_for_validity(First_input) #updates the input done by the user to be valid
        Sqaured_Move1st=check_for_square1st(str(Valid_move1st),Valid_Tokens) #updates the valid input to be squared
        Valid_Tokens=Valid_Tokens-Sqaured_Move1st
        
        if(Valid_Tokens<=0):  #checks whether the tokens are empty to end the game
            print("1ST PLAYER WINS! \n")
            break
        
        
        print("number of coins is now ",Valid_Tokens)
        Second_input=str(input("2nd player insert a square to subtract:\n"))
        Valid_move2nd=check_for_validity(Second_input)  #updates the input done by the user to be valid
        Sqaured_Move2nd=check_for_square2nd(str(Valid_move2nd),Valid_Tokens)  #updates the valid input to be squared
        Valid_Tokens=Valid_Tokens-Sqaured_Move2nd 
        print("number of coins is now ",Valid_Tokens)
        if(Valid_Tokens<=0): #checks whether the tokens are empty to end the game
          print("2ND PLAYER WINS \n")
          break
        
      
        
            
            
            
                
        


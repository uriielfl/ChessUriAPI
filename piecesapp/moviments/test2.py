import numpy as np
#horizontal_position = ["a", "b", "c", "d", "e", "f", "g", "h"]
#vertical_position = ["1", "2", "3", "4", "5", "6", "7", "8"]
#position2 = str(input("Sua posição, por favor:\n"))
#classe2 = str(input("cavalo, peão, torre, bispo, rei e rainha\nDigite o nome da classe, por favor:\n"))
#color2= str(input("Sua cor, por favor:\n"))


chess_board = np.array([['a1','a2','a3','a4','a5','a6','a7','a8'],
                       ['b1','b2','b3','b4','b5','b6','b7','b8'],
                       ['c1','c2','c3','c4','c5','c6','c7','c8'],
                       ['d1','d2','d3','d4','d5','d6','d7','d8'],
                       ['e1','e2','e3','e4','e5','e6','e7','e8'],
                       ['f1','f2','f3','f4','f5','f6','f7','f8'],
                       ['g1','g2','g3','g4','g5','g6','g7','g8'],
                       ['h1','h2','h3','h4','h5','h6','h7','h8']])

result = np.where(chess_board==position2)


#################
#####CAVALO######
#################

def knight_moviment(classe, color, position):
    print("oi")
  
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
        indexes.append(int(i)) 

    try:     
        possibilidade = chess_board[int(indexes[0])+2][int(indexes[1])+1]
        possible_to_do.append(possibilidade)     
    except:
        pass
    try:
        if int(indexes[1]) - 1 > -1:          
            possibilidade = chess_board[int(indexes[0])+2][int(indexes[1])-1]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:    
        if int(indexes[0]-2)>-1:        
            possibilidade = chess_board[int(indexes[0])-2][int(indexes[1])+1]
            possible_to_do.append(possibilidade)         
    except:
        pass
    try:
        if int(indexes[1])-1 > -1 and int(indexes[0])-2>-1:            
            possibilidade = chess_board[int(indexes[0])-2][int(indexes[1])-1]
            possible_to_do.append(possibilidade)              
    except:
        pass
    try:        
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])+2]
        possible_to_do.append(possibilidade)       
    except:
        pass   
    try:
        if int(indexes[1]-2)>-1:          
            possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])-2]
            possible_to_do.append(possibilidade)            
    except:
        pass    
    try:
        if int(indexes[1]+2) > -1 and int(indexes[0] -1) > -1:       
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])+2]
            possible_to_do.append(possibilidade)
    except:
        pass   
    try:
        if int(indexes[1])-2 > -1 and int(indexes[0]-1) > -1:
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])-2]
            possible_to_do.append(possibilidade) 
    except:
        pass        
    print(possible_to_do) 
    

##################
#######PEÃO#######
##################
def black_pawn_moviment():
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
      indexes.append(int(i))
    for i in range (0,3):
        try:
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])]
            possible_to_do.append(possibilidade)          
            if int(indexes[0])+i > 7:
                break
        except:
            pass
 
def white_pawn_moviment():
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
      indexes.append(int(i))
    for i in range (0,3):
        try:           
            if int(indexes[0])-i < 0:
                break                 
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])]
            possible_to_do.append(possibilidade)
        except:
            pass
 

   

##################
###### REI #######
##################
def king_moviment():
   
    possible_to_do = []
    indexes = []
    count = 0
    for i in result:
      indexes.append(int(i)) 
    print("foi")
    try: 
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])]
        possible_to_do.append(possibilidade)    
    except:
        pass 
    try:   
        possibilidade = chess_board[int(indexes[0])][int(indexes[1])+1]
        possible_to_do.append(possibilidade)     
    except:
        pass
    try:       
        if int(indexes[0])-1>-1:
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])]
            possible_to_do.append(possibilidade)         
    except:
        pass 
    try:
        if int(indexes[1])-1>-1:
            possibilidade = chess_board[int(indexes[0])][int(indexes[1])-1]
            possible_to_do.append(possibilidade)      
    except:
        pass 
    try:      
        if int(indexes[1])-1 > -1:
            possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])-1]
            possible_to_do.append(possibilidade)     
    except:
        pass 
    try:       
        if int(indexes[0])-1>-1:
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])+1]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:    
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])+1]
        possible_to_do.append(possibilidade)
       
    except:
        pass 
    try:    
        if int(indexes[0])-1>-1 and int(indexes[1])-1 > -1:
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])-1]
            possible_to_do.append(possibilidade)         
    except:
        pass 
    print(possible_to_do)




##########
##RAINHA##
##########
def queen_moviment():
    possible_to_do = []
    indexes = []
    count = 0
    for i in result:
      indexes.append(int(i)) 

    try:       
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:   
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:        
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try: 
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
            if int(indexes[0])-i < 0 or int(indexes[1])-i < 0:
                break
    except:
        pass 
    try:  
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:        
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:
        for i in range(0,7):            
            possibilidade = chess_board[int(indexes[0])][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
    except:
        pass    



##########
##BISPO##
##########
def bishop_moviment():
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
        indexes.append(int(i))  
  
    try: 
        possible_to_do.append("1:") 
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:    
        possible_to_do.append("2:")     
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:
        possible_to_do.append("3:") 
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:
        possible_to_do.append("4:") 
        for i in range(0,7):        
            if int(indexes[0])-i < 0 or int(indexes[1])-i < 0:
                break
            if int(indexes[0])-i >7 or int(indexes[1])-i > 7:
                break           
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])-i]
            possible_to_do.append(possibilidade)         
    except:
        pass       

##########
##TORRE##
##########
def rook_moviment():
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
        indexes.append(int(i))       
    try:  
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])+i][int(indexes[1])]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:        
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])]
            possible_to_do.append(possibilidade)
    except:
        pass
    try:
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])][int(indexes[1])+i]
            possible_to_do.append(possibilidade)
    except:
        pass 
    try:
        for i in range(0,7):
            possibilidade = chess_board[int(indexes[0])][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
    except:
        pass    
   

if classe2=="cavalo":
    knight_moviment(classe2,color2,position2)
if classe2 == "peão" and color2 == "preto":
    black_pawn_moviment()
elif classe2 == "peão" and color2 == "branco":
    white_pawn_moviment()
elif classe2 == "torre":
    rook_moviment()
elif classe2 == "bispo":
    bishop_moviment()
elif classe2 == "rei":
    king_moviment()
elif classe2 == "rainha":
    queen_moviment()
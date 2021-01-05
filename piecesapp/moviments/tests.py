import numpy as np
horizontal_position = ["a", "b", "c", "d", "e", "f", "g", "h"]
vertical_position = ["1", "2", "3", "4", "5", "6", "7", "8"]
position = str(input("Sua posição, por favor:\n"))
classe = str(input("cavalo, peão, torre, bispo, rei e rainha\nDigite o nome da classe, por favor:\n"))

color= str(input("Sua cor, por favor:\n"))

chess_board = np.array([['a1','a2','a3','a4','a5','a6','a7','a8'],
                       ['b1','b2','b3','b4','b5','b6','b7','b8'],
                       ['c1','c2','c3','c4','c5','c6','c7','c8'],
                       ['d1','d2','d3','d4','d5','d6','d7','d8'],
                       ['e1','e2','e3','e4','e5','e6','e7','e8'],
                       ['f1','f2','f3','f4','f5','f6','f7','f8'],
                       ['g1','g2','g3','g4','g5','g6','g7','g8'],
                       ['h1','h2','h3','h4','h5','h6','h7','h8']])
result = np.where(chess_board==position)
#################
#####CAVALO######
#################

def knight_moviment():
    possible_to_do = []          
    indexes = []
    count = 0
    moviment = ""
    first_turn = []
    second_turn = []
    for i in result:
        indexes.append(int(i))  
    print(indexes)    
    try:
        possibilidade = chess_board[int(indexes[0])+2][int(indexes[1])+1]
        possible_to_do.append(possibilidade)
        print("1")
    except:
        pass
    try:
        if int(indexes[1])-1 < 7:            
            possibilidade = chess_board[int(indexes[0])+2][int(indexes[1])-1]
            possible_to_do.append(possibilidade)
            print("2")
    except:
        pass
    try:
        possibilidade = chess_board[int(indexes[0])-2][int(indexes[1])+1]
        possible_to_do.append(possibilidade)
        print("3")
    except:
        pass
    try:
        if int(indexes[0])+1 < 0:
            possibilidade = chess_board[int(indexes[0])-2][int(indexes[1])-1]
            possible_to_do.append(possibilidade)
            print("4")
        
    except:
        pass
    try:
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])+2]
        possible_to_do.append(possibilidade)
        print("5")
    except:
        pass
    try:
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])-2]
        possible_to_do.append(possibilidade)
        print("6")
    except:
        pass
    try:
        possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])+2]
        possible_to_do.append(possibilidade)
        print("7")
    except:
        pass
    try:    
        if int(indexes[0]-1) > 0:
            possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])-2]
            possible_to_do.append(possibilidade)
            print("8")
    
    except:
        pass
    

    print("Sua posição:"+str(position))
    print("Você pode ir em:")
    print(possible_to_do)
    print(moviment)


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
    print("Sua posição:"+str(position))
    print("Você pode ir em:")
    print(possible_to_do)
    print(moviment)    
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
    print("Sua posição:"+str(position))
    print("Você pode ir em:")
    print(possible_to_do)
    print(moviment)    

   

##################
###### REI #######
##################
def king_moviment():
    possible_to_do = []
    indexes = []
    count = 0
    for i in result:
      indexes.append(int(i))
    print(indexes)  
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
        
    
        possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])]
        possible_to_do.append(possibilidade)
    except:
        pass 
    try:
 
   
        possibilidade = chess_board[int(indexes[0])][int(indexes[1])-1]
        possible_to_do.append(possibilidade)
       
    except:
        pass 
    try:  
    
        possibilidade = chess_board[int(indexes[0])+1][int(indexes[1])-1]
        possible_to_do.append(possibilidade)
    except:
        pass 
    try:        
    
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
        possibilidade = chess_board[int(indexes[0])-1][int(indexes[1])-1]
        possible_to_do.append(possibilidade)
        
       
    except:
        pass 
 
    print("Sua posição:"+str(position))
    print("Você pode ir em:")
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
    print(indexes)
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
    print("Sua posição:"+str(position))
    print("Você pode ir em:")
    print(possible_to_do)


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
    print(indexes)  
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
            print(int(indexes[0])-1)
            print(int(indexes[1])-1)
            possibilidade = chess_board[int(indexes[0])-i][int(indexes[1])-i]
            possible_to_do.append(possibilidade)
            print(chess_board[int(indexes[0])-i][int(indexes[1])-i])
    except:
        pass    
    print("Sua classe é:" +str(classe))
    print("Sua posição:"+str(position))
      
    print("Você pode ir em:")
    print(possible_to_do)
    print(moviment)
    

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
    print(indexes)  
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
    print("Sua posição:"+str(position))
    print("Você pode ir em:")
    print(possible_to_do)
    print(moviment)


if classe=="cavalo":
    knight_moviment()
if classe == "peão" and color == "preto":
    black_pawn_moviment()
elif classe == "peão" and color == "branco":
    white_pawn_moviment()
elif classe == "torre":
    rook_moviment()
elif classe == "bispo":
    bishop_moviment()
elif classe == "rei":
    king_moviment()
elif classe == "rainha":
    queen_moviment()
from rest_framework import viewsets 
from piecesapp.api import serializers
from piecesapp import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from django.http import Http404
import numpy as np
import sqlite3 
from datetime import datetime

# Note: In some positions, i'm using a for loop
# just to go to see the position like in pawns movements,
# but sometimes I needed to just predifine what would be the next position to go,
# like in knight movements, for exemple. 
# I think the biggest problem is that there's a lot of trys, excepts and ifs in knight
# while in pawns we have just 1. These was made because, while some pieces could 
# simply just follow the for loop and pass through the conditions, other pieces needed to make a curve.

c = sqlite3.connect('db.sqlite3', check_same_thread=False)
cur = c.cursor()
#Creating our logs in db (pieces_logs, board_logs)
cur.execute("CREATE TABLE IF NOT EXISTS pieces_logs (pieceid INT UNIQUE, piecename TEXT, piececolor TEXT, createddate TEXT)") 
c.commit()
cur.execute("CREATE TABLE IF NOT EXISTS board_logs (movementid INT UNIQUE, piecename TEXT, piececolor TEXT, movementdate TEXT, possiblepositions TEXT, FOREIGN KEY (movementid) REFERENCES pieces_logs (pieceid))")
c.commit
chess_board = np.array([['a1','a2','a3','a4','a5','a6','a7','a8'], #our board is an numpy array that uses algebric notation
                       ['b1','b2','b3','b4','b5','b6','b7','b8'],
                       ['c1','c2','c3','c4','c5','c6','c7','c8'],
                       ['d1','d2','d3','d4','d5','d6','d7','d8'],
                       ['e1','e2','e3','e4','e5','e6','e7','e8'],
                       ['f1','f2','f3','f4','f5','f6','f7','f8'],
                       ['g1','g2','g3','g4','g5','g6','g7','g8'],
                       ['h1','h2','h3','h4','h5','h6','h7','h8']])


class PiecesAPIView(APIView):
    def get(self,request, *args, **kwargs):
        queryset = models.Pieces.objects.all()
        serializer = serializers.PiecesSerializer(queryset, many=True, context = {'request':request})
        data = serializer.data      
        if data:
            return Response({
                'sucess':'True',
                'message':'Data retrieved sucessfully',
                'data':data,
            }, status=200)
        else:
            return Response(data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer = serializers.PiecesSerializer(data=request.data)         
        if serializer.is_valid():
            serializer.save()  
            #Registering the insertion of a new piece into our logs:          
            cur.execute("INSERT INTO pieces_logs (pieceid, piecename, piececolor, createddate) VALUES(?,?,?,?)", (serializer.data['piece_id'], serializer.data['piece_name'], serializer.data['piece_color'], datetime.now()))  
            c.commit()            
            return Response({
                'sucess':'it was posted',               
                'log information':'piece log created', 
                'data':serializer.data,                    
            }, status = status.HTTP_201_CREATED)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BoardAPIView(APIView):
    def get(self,request, *args, **kwargs):
        queryset = models.Board.objects.all()
        serializer = serializers.BoardSerializer(queryset, many=True, context = {'request':request})
        data = serializer.data        
        if data:
            return Response({
                'sucess':'True',
                'board':'right',
                'data':data,
            }, status=200)
        else:
            return Response(data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer = serializers.BoardSerializer(data=request.data)
        queryset = models.Board.objects.all()        
        if serializer.is_valid():            
            serializer.save()      
            boardid = serializer.data['boardpiece_id'] #getting id from request      
            cur.execute("SELECT piece_name, piece_color FROM piecesapp_pieces WHERE piece_id = '%s'"%boardid)#getting name and color from database through id
            c.commit()
            for v in cur:
                piecedataname, piecedatacolor=v #name and color appended      
            position = serializer.data['position_x'] + serializer.data['position_y'] #position is equal to position_x and position_y from our requisition
            classe = piecedataname
            color = piecedatacolor
            result = np.where(chess_board==position)  #Here will save the indexes of chosen position

            ##movementS##
            #Knight:
            def knight_movement():
                possible_to_do = [] #This list will receive our positions     
                indexes = []            
                for i in result:
                    indexes.append(int(i)) 
                try:     
                    possible = chess_board[int(indexes[0])+2][int(indexes[1])+1]
                    possible_to_do.append(possible)     
                except:
                    pass
                #These 'try' and 'excepts' is just to prevent fails if the next position doesn't exist
                try:                     
                    if int(indexes[1]) - 1 > -1:     
                        #These "if's" along all the movements functions   
                        #is to prevent that the piece   
                        #goes from position a8 to h1, for exemple.                 
                        possible = chess_board[int(indexes[0])+2][int(indexes[1])-1]         
                        possible_to_do.append(possible)                                
                except:
                    pass
                try:    
                    if int(indexes[0]-2)>-1:        
                        possible = chess_board[int(indexes[0])-2][int(indexes[1])+1]
                        possible_to_do.append(possible)         
                except:
                    pass
                try:
                    if int(indexes[1])-1 > -1 and int(indexes[0])-2>-1:            
                        possible = chess_board[int(indexes[0])-2][int(indexes[1])-1]
                        possible_to_do.append(possible)              
                except:
                    pass
                try:        
                    possible = chess_board[int(indexes[0])+1][int(indexes[1])+2]
                    possible_to_do.append(possible)       
                except:
                    pass   
                try:
                    if int(indexes[1]-2)>-1:          
                        possible = chess_board[int(indexes[0])+1][int(indexes[1])-2]
                        possible_to_do.append(possible)            
                except:
                    pass    
                try:
                    if int(indexes[1]+2) > -1 and int(indexes[0] -1) > -1:       
                        possible = chess_board[int(indexes[0])-1][int(indexes[1])+2]
                        possible_to_do.append(possible)
                except:
                    pass   
                try:
                    if int(indexes[1])-2 > -1 and int(indexes[0]-1) > -1:
                        possible = chess_board[int(indexes[0])-1][int(indexes[1])-2]
                        possible_to_do.append(possible) 
                except:
                    pass 
                #Returning the positions
                return possible_to_do 
            #Pawn:
            ##black:
            def black_pawn_movement():
                possible_to_do = []          
                indexes = []
                for i in result:
                    indexes.append(int(i))
                for i in range (0,3):
                    try:
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])]
                        possible_to_do.append(possible)          
                        if int(indexes[0])+i > 7:
                            break
                    except:
                        pass   
            ##white:         
            def white_pawn_movement():
                possible_to_do = []          
                indexes = []              
                for i in result:
                    indexes.append(int(i))
                for i in range (0,3):
                    try:           
                        if int(indexes[0])-i < 0:
                            break                 
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])]
                        possible_to_do.append(possible)
                    except:
                        pass
            #King:
            def king_movement():   
                possible_to_do = []
                indexes = []                
                for i in result:
                    indexes.append(int(i))               
                try: 
                    possible = chess_board[int(indexes[0])+1][int(indexes[1])]
                    possible_to_do.append(possible)    
                except:
                    pass 
                try:   
                    possible = chess_board[int(indexes[0])][int(indexes[1])+1]
                    possible_to_do.append(possible)     
                except:
                    pass
                try:       
                    if int(indexes[0])-1>-1:
                        possible = chess_board[int(indexes[0])-1][int(indexes[1])]
                        possible_to_do.append(possible)         
                except:
                    pass 
                try:
                    if int(indexes[1])-1>-1:
                        possible = chess_board[int(indexes[0])][int(indexes[1])-1]
                        possible_to_do.append(possible)      
                except:
                    pass 
                try:      
                    if int(indexes[1])-1 > -1:
                        possible = chess_board[int(indexes[0])+1][int(indexes[1])-1]
                        possible_to_do.append(possible)     
                except:
                    pass 
                try:       
                    if int(indexes[0])-1>-1:
                        possible = chess_board[int(indexes[0])-1][int(indexes[1])+1]
                        possible_to_do.append(possible)
                except:
                    pass
                try:    
                    possible = chess_board[int(indexes[0])+1][int(indexes[1])+1]
                    possible_to_do.append(possible)                
                except:
                    pass 
                try:    
                    if int(indexes[0])-1>-1 and int(indexes[1])-1 > -1:
                        possible = chess_board[int(indexes[0])-1][int(indexes[1])-1]
                        possible_to_do.append(possible)         
                except:
                    pass 
                return possible_to_do          
            #Queen:
            def queen_movement():
                possible_to_do = []
                indexes = []                
                for i in result:
                    indexes.append(int(i)) 
                try:       
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])-i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:   
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass
                try:        
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try: 
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])-i]
                        possible_to_do.append(possible)
                        if int(indexes[0])-i < 0 or int(indexes[1])-i < 0:
                            break
                except:
                    pass 
                try:  
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:        
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])]
                        possible_to_do.append(possible)
                except:
                    pass
                try:
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:
                    for i in range(0,7):            
                        possible = chess_board[int(indexes[0])][int(indexes[1])-i]
                        possible_to_do.append(possible)
                except:
                    pass 
                return possible_to_do 
            #Bishop:
            def bishop_movement():
                possible_to_do = []          
                indexes = []               
                for i in result:
                    indexes.append(int(i))
                try: 
                    possible_to_do.append("1:") 
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])-i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:    
                    possible_to_do.append("2:")     
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass
                try:
                    possible_to_do.append("3:") 
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:
                    possible_to_do.append("4:") 
                    for i in range(0,7):        
                        if int(indexes[0])-i < 0 or int(indexes[1])-i < 0:
                            break
                        if int(indexes[0])-i >7 or int(indexes[1])-i > 7:
                            break           
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])-i]
                        possible_to_do.append(possible)         
                except:
                    pass
                return possible_to_do               
            #Rook
            def rook_movement():
                possible_to_do = []          
                indexes = []              
                for i in result:
                    indexes.append(int(i))       
                try:  
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])+i][int(indexes[1])]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:        
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])-i][int(indexes[1])]
                        possible_to_do.append(possible)
                except:
                    pass
                try:
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])][int(indexes[1])+i]
                        possible_to_do.append(possible)
                except:
                    pass 
                try:
                    for i in range(0,7):
                        possible = chess_board[int(indexes[0])][int(indexes[1])-i]
                        possible_to_do.append(possible)
                except:
                    pass   
                return possible_to_do
                
            if classe=="knight":                
                movements = knight_movement()
            if classe == "pawn" and color == "black":
                movements = black_pawn_movement()
            elif classe == "pawn" and color == "white":
                movements = white_pawn_movement()
            elif classe == "rook":
                movements = rook_movement()
            elif classe == "bishop":
                movements = bishop_movement()
            elif classe == "king":            
                movements = king_movement()                
            elif classe == "queen":
                movements = queen_movement() 
            #Creating our board log:         
            cur.execute("INSERT INTO board_logs (movementid, piecename, piececolor, movementdate, possiblepositions) VALUES(?,?,?,?,?)", (1, piecedataname, piecedatacolor, datetime.now(), str(movements)))  
            c.commit()
            #Returning the informations to user:
            return Response({
                'sucess':'it was posted',               
                'data':boardid,
                'piece':piecedataname,
                'position':position,
                'possible movements':movements
                       
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


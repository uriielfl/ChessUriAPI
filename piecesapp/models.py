from django.db import models
import uuid

# Create your models here.
COLOR_CHOICES = (
    ('white','WHITE'),
    ('black', 'BLACK'),    
)
PICES_NAMES = (
    ('king','KING'),
    ('queen','QUEEN'),
    ('rook','ROOK'),
    ('bishop','BISHOP'),
    ('knight','KNIGHT'),
    ('pawn','PAWN'),
)
WHITE_KING_POSITION = ['e1']
BLACK_KING_POSITION = ['e8'] 

WHITE_QUEEN_POSITION = ['d1']
BLACK_QUEEN_POSITION = ['d8']

WHITE_ROOK_POSITION = ['a1','h1']
BLACK_ROOK_POSITION = ['a8','h8']

WHITE_BISHOP_POSITION = ['c1','f1']
BLACK_BISHOP_POSITION = ['c8','f8']

WHITE_KNIGHT_POSITION = ['b1', 'g1']   
BLACK_KNIGHT_POSITION = ['b8', 'g8']   

WHITE_PAWN_POSITION = ['a2', 'b2','c2','d2','e2','f2','g2','h2'] 
BLACK_PAWN_POSITION = ['a7', 'b7','c7','d7','e7','f7','g7','h7'] 

PIECE_POSITION_HORIZONTAL = (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('e','E'),
    ('f','F'),
    ('g','G'),
    ('h','H'),
)
PIECE_POSITION_VERTICAL = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
)
BOARD_DEFAULT_ID = 1
class Pieces(models.Model):
    piece_id = models.AutoField(primary_key=True,editable= False) 
    piece_name = models.CharField(choices = PICES_NAMES, max_length=255)
    piece_color = models.CharField(choices = COLOR_CHOICES, max_length=5)  
    initial_position_h = models.CharField(default = "a", choices=PIECE_POSITION_HORIZONTAL, max_length=50)
    initial_position_v = models.IntegerField(default = 1, choices=PIECE_POSITION_VERTICAL)
        
    chess_board = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['1', '2', '3', '4', '5', '6', '7', '8']]
 
    def __int__(self):
        return self.piece_id
  
class Board(models.Model):
    boardpiece_id = models.ForeignKey(Pieces, on_delete=models.CASCADE)
    position_x = models.CharField(choices = PIECE_POSITION_HORIZONTAL, default="PIECE POSITION", max_length=50)
    position_y = models.CharField(choices = PIECE_POSITION_VERTICAL, default="PIECE POSITION",max_length = 50)
    def __str__(self):
        return str(self.boardpiece_id)
       
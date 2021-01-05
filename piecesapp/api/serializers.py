from rest_framework import serializers
from piecesapp import models 

class PiecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pieces         
        fields = ('piece_id', 'piece_name', 'piece_color')
        
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Board 
        fields = ['boardpiece_id', 'position_x', 'position_y']
        
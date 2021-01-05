# Chess Uri API

Chess Uri API is an API made to get possible next position on chess's board. 

ps: board on footer.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
### Register the piece
Through an post method requisition, create a new piece.

```bash
C:\Users\user>curl -X POST -d  "piece_name=king&piece_color=black" http://127.0.0.1:8000/pieces/
{"sucess":"it was posted","log information":"piece log created","data":{"piece_id":5,"piece_name":"king","piece_color":"black"}}
```
###### Pices name options:
- king
- queen
- pawn
- rook
- bishop
###### Pices color options:
- black
- white

### Register the position:
 Ok, now that we have our piece, we will need to use the piece ID to get our possible next possition relative to our choose. The piece_id:5 is a king of color black, knowing these, let's make a post on our board.


```bash
C:\Users\uriel>curl -X POST -d  "boardpiece_id=5&position_x=h&position_y=5" http://127.0.0.1:8000/board/

```
- boardpiece_id = ID of our piece that we have just registered.
- position_x = Horizontal Position.
- position_y = Vertical Position.  

### Result:

```bash
{"sucess":"it was posted","data":5,"piece":"king","position":"h5","possible moviments":["h6","g5","h4","g6","g4"]}
```
#### Understanding result:
We received a sucess message! After all, "it was posted". Then, we have our data. Our id was 5, so we have our king in position "h5" in algebric notation, then we get our possible moviments cosidering the piece's name(at /pieces/ = pieces_name), color and position.  

# Board:

```
                       
                       [a1] [a2] [a3] [a4] [a5] [a6] [a7][a8]
                       [b1] [b2] [b3] [b4] [b5] [b6] [b7][b8]
                       [c1] [c2] [c3] [c4] [c5] [c6] [c7][c8]
                       [d1] [d2] [d3] [d4] [d5] [d6] [d7][d8]
                       [e1] [e2] [e3] [e4] [e5] [e6] [e7][e8]
                       [f1] [f2] [f3] [f4] [f5] [f6] [f7][f8]
                       [g1] [g2] [g3] [g4] [g5] [g6] [g7][g8]
                       [h1] [h2] [h3] [h4] [h5] [h6] [h7][h8]
```

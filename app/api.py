from flask import Flask, request
from chess import Chess
from flask import request
from flask import Response
from db import *

app = Flask('web_app')
app.config["DEBUG"] = True
drop_database()
create_initial_structure_if_not_exists_db()

@app.route('/piece', methods=['POST'])
def registry_chess_piece():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        input = request.json
        validate_input(input, 'type')
        validate_input(input, 'name')
        validate_input(input, 'color')
        return insert_into_piece(input['name'], input['type'], input['color'])
    else:
        return 'Content-Type not supported!'

@app.route('/location/two-turns', methods=['GET'])
def possible_location_of_pience_two_turns_by_position():
    try:
        if request.args.get('pieceId') == None or request.args.get('position') == None:
            return Response("'result':'Not provided min required params pieceId and/or position'", status=400, mimetype='application/json')  
        piece_id = request.args.get('pieceId')
        position = request.args.get('position')
        ELEMENTS_IN_PIECE = 4        
        piece = select_piece_by(piece_id)
        if len(piece) == ELEMENTS_IN_PIECE:
            return retrive_possibilities_for_knight_piece(piece, position, piece_id)
        return Response("{'result':'Invalid piece provided'}", status=400, mimetype='application/json')      
    except Exception as e:    
        return Response(f"'result':'Invalid position provided: {e}'", status=400, mimetype='application/json')  

def retrive_possibilities_for_knight_piece(piece, position, piece_id):
    print(piece['type'])
    if(piece['type'] != 'knight'):
        return 'Not a knight'
    possibilities = Chess(position).find_knight_possibilities_in_two_tours()
    insert_into_possibilities(piece_id, str(possibilities))
    return {'piece': piece, 'tours': possibilities}    

def validate_input(input, input_field):
    if input_field not in input:
        raise ValueError(f'Input: {input_field} in the endpoint was expected but not received ')   
app.run()
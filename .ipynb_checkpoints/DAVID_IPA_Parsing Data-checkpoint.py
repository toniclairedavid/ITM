'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    member1 = social_graph.get(from_member)
    member2 = social_graph.get(to_member)
    
    following_member1 = member1.get('following')
    following_member2 = member2.get('following')
    
    if to_member in following_member1:
        if from_member in following_member2:
            return "friends"
        else:
            return "follower"
    else:
        if from_member in following_member2:
            return "followed by"
        else:
            return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # row win
    for row in range(len(board)):
        char = board[row][0]
        score = 0
        
        for col in range(len(board)):
            if char == board[row][col]:
                score += 1
            else:
                break
        
        if score == len(board) and char != '':
            return char
        
    # col win
    for col in range(len(board)):
        char = board[0][col]
        score = 0
        
        for row in range(len(board)):
            if char == board[row][col]:
                score += 1
            else:
                break
        
        if score == len(board) and char != '':
            return char
        
    # diagonal win (\)
    char = board[0][0]
    score = 0
    
    for row in range(len(board)):
        if char == board[row][row]:
            score += 1
        else:
            break
        
        if score == len(board) and char != '':
            return char
        
    # diagonal win (/)
    char = board[0][len(board)-1]
    score = 0
    
    for row in range(len(board)):
        if char == board[row][len(board)-1-row]:
            score += 1
        else:
            break
        
        if score == len(board) and char != '':
            return char
        else:
            return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    stop_list = list(route_map.keys())
    route_eta = 0
    
    for x in range(len(route_map)):
        if first_stop == stop_list[x][0]:
            stop_number_start = x
    
    for y in range(len(route_map)):
        if second_stop == stop_list[y][1]:
            stop_number_end = y
            
    if stop_number_start > stop_number_end:
        while stop_number_start < len(route_map):
            first_stop = stop_list[stop_number_start][0]
            stop_2 = stop_list[stop_number_start][1]
            route_eta += route_map.get((first_stop,stop_2)).get('travel_time_mins')
            stop_number_start = stop_number_start + 1
            
        stop_number_start = 0
        
    while stop_number_start <= stop_number_end:
        first_stop = stop_list[stop_number_start][0]
        stop_2 = stop_list[stop_number_start][1]
        route_eta += route_map.get((first_stop,stop_2)).get('travel_time_mins')
        stop_number_start = stop_number_start + 1
            
    return route_eta
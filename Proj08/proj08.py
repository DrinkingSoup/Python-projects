import cards

def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    my_deck = cards.Deck()
    my_deck.shuffle()

    foundation = [[], [], [], []]
    cell = [[], [], [], []]
    tableau = [[], [], [], [], [], [], [], []]

    for i in range(6):
        tableau[0].append(my_deck.deal())
        tableau[1].append(my_deck.deal())
        tableau[2].append(my_deck.deal())
        tableau[3].append(my_deck.deal())
        tableau[4].append(my_deck.deal())
        tableau[5].append(my_deck.deal())
        tableau[6].append(my_deck.deal())
        tableau[7].append(my_deck.deal())
    tableau[0].append(my_deck.deal())
    tableau[1].append(my_deck.deal())
    tableau[2].append(my_deck.deal())
    tableau[3].append(my_deck.deal())
    return foundation,tableau,cell


def move_to_foundation(tableau, foundation, cell=None, t_col=0, f_col=0, c_col=0):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    t_col = int(t_col)
    f_col = int(f_col)
    c_col = int(c_col)

    if not cell:
        if (t_col != 0 and f_col != 0) and (t_col <= 8 and f_col <= 4):
            tab_ind = t_col - 1
            fnd_ind = f_col - 1
            lst_place = len(tableau[tab_ind]) - 1

            rank_1 = tableau[tab_ind][lst_place].rank()

            if rank_1 == 1 and not foundation[fnd_ind]:
                foundation[fnd_ind].append(tableau[tab_ind].pop(lst_place))
                return True
            elif rank_1 == foundation[fnd_ind][-1].rank() + 1:
                print("work")
                if tableau[tab_ind][-1].suit() == foundation[fnd_ind][-1].suit():
                    foundation[fnd_ind].append(tableau[tab_ind].pop(lst_place))
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        if (c_col != 0 and f_col != 0) and (c_col <= 4 and f_col <= 4):
            cel_ind = c_col - 1
            fnd_ind = f_col - 1
            lst_place = len(cell[cel_ind]) - 1

            rank_1 = cell[cel_ind][lst_place].rank()

            if rank_1 == 1 and not foundation[fnd_ind]:
                foundation[fnd_ind].append(cell[cel_ind].pop(lst_place))
                return True
            elif rank_1 > foundation[fnd_ind][-1].rank():
                if cell[cel_ind][-1].suit() == foundation[fnd_ind][-1].suit():
                    foundation[fnd_ind].append(cell[cel_ind].pop(lst_place))
                    return True
                else:
                    return False
        else:
            return False



def move_to_cell(tableau,cell,t_col=0,c_col=0):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    t_col = int(t_col)
    c_col = int(c_col)
    if (t_col != 0 and c_col != 0) and (t_col <= 8 and c_col <= 4):
        tab_ind = t_col - 1
        col_ind = c_col - 1
        lst_place = len(tableau[tab_ind]) - 1

        if not cell[col_ind]:
            cell[col_ind].append(tableau[tab_ind].pop(lst_place))
            return True
        else:
            return False
    else:
        return False

def move_to_tableau(tableau,cell,t_col=0,c_col=0):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    t_col = int(t_col)
    c_col = int(c_col)

    if (t_col != 0 and c_col != 0) and (t_col <= 8 and c_col <= 4):
        tab_ind1 = c_col - 1
        tab_ind2 = t_col - 1

        lst_place1 = len(cell[tab_ind1]) - 1
        lst_place2 = len(tableau[tab_ind2]) - 1

        suit1 = int(cell[tab_ind1][lst_place1].suit())
        suit2 = int(tableau[tab_ind2][lst_place2].suit())
        rank1 = int(cell[tab_ind1][lst_place1].rank())
        rank2 = int(tableau[tab_ind2][lst_place2].rank())

        if suit1 == 1 or suit1 == 4:  
            if (rank1 == rank2 - 1) and (suit2 == 2 or suit2 == 3):
                tableau[tab_ind2].append(cell[tab_ind1].pop(lst_place1))
                return True
        elif suit1 == 2 or suit1 == 3:
            if (rank1 == rank2 - 1) and (suit2 == 1 or suit2 == 4):
                tableau[tab_ind2].append(cell[tab_ind1].pop(lst_place1))
                return True
        else:
            return False

    else:
        return False
        
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    suit1 = len(foundation[0])
    suit2 = len(foundation[1])
    suit3 = len(foundation[2])
    suit4 = len(foundation[3])

    if suit1 == 13 and suit2 == 13 and suit3 == 13 and suit4 == 13:
        return True
    else:
        return False


def move_in_tableau(tableau,t_col_source=0,t_col_dest=0):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    t_col_source = int(t_col_source)
    t_col_dest = int(t_col_dest)

    if (t_col_source != 0 and t_col_dest != 0) and (t_col_source <= 8 and t_col_dest <= 8):
        tab_ind1 = t_col_source - 1
        tab_ind2 = t_col_dest - 1

        lst_place1 = len(tableau[tab_ind1]) - 1
        lst_place2 = len(tableau[tab_ind2]) - 1

        suit1 = int(tableau[tab_ind1][lst_place1].suit())
        suit2 = int(tableau[tab_ind2][lst_place2].suit())
        rank1 = int(tableau[tab_ind1][lst_place1].rank())
        rank2 = int(tableau[tab_ind2][lst_place2].rank())

        if suit1 == 1 or suit1 == 4:  
            if (rank1 == rank2 - 1) and (suit2 == 2 or suit2 == 3):
                tableau[tab_ind2].append(tableau[tab_ind1].pop(lst_place1))
                return True
        elif suit1 == 2 or suit1 == 3:
            if (rank1 == rank2 - 1) and (suit2 == 1 or suit2 == 4):
                tableau[tab_ind2].append(tableau[tab_ind1].pop(lst_place1))
                return True
        else:
            return False

    else:
        return False
        

def print_game(foundation, tableau, cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line

    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(str(c[0])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            print('{:8s}'.format(str(stack[-1])), end = '')
        except IndexError:
            print('{:8s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                print('{:8s}'.format(str(stack[i])), end = '')
            except IndexError:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")
    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    while True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            if r == 't2f':
                if len(response_list) == 3:
                    move_to_foundation(tableau, foundation, None, response_list[1], response_list[2], 0)                    
            elif r == 't2t':
                if len(response_list) == 3:
                    move_in_tableau(tableau, response_list[1], response_list[2])                       
            elif r == 't2c':
                if len(response_list) == 3:
                    move_to_cell(tableau, cell, response_list[1], response_list[2])                     
            elif r == 'c2t':
                if len(response_list) == 3:
                    move_to_tableau(tableau, cell, response_list[2], response_list[1])                       
            elif r == 'c2f':
                if len(response_list) == 3:
                    move_to_foundation(tableau, foundation, cell, 0, response_list[2], response_list[1])                                             
            elif r == 'q':
                break
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    


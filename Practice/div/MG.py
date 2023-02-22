def check_win(state):
    win_states = [0b111000000, 0b000111000, 0b000000111, 
                  0b100100100, 0b010010010, 0b001001001,
                  0b100010001, 0b001010100]
    for win_state in win_states:
        if (state & win_state) == win_state:
            return True
    return False

t = int(input().strip())
for _ in range(t):
    state = int(input().strip(), 8)
    x_played = state & 0b111111111
    o_played = (state & 0b11111111100000000) >> 9
    x_turn = state & 0b10000000000000000
    if check_win(x_played):
        print("X wins")
    elif check_win(o_played):
        print("O wins")
    elif x_played | o_played == 0b111111111:
        print("Cat's")
    else:
        print("In progress")
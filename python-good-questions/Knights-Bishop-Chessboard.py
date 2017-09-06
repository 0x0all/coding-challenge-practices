# https://codereview.stackexchange.com/questions/107470/find-total-number-of-phone-numbers-formed-by-the-movement-of-knight-and-bishop-o

knight = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2]}

bishop = {1: [5, 9], 2: [4, 6], 3: [5, 7], 4: [2, 8], 5: [1, 3, 7, 9], 6: [2, 8], 7: [5, 0, 3], 8: [4, 6], 9: [5, 0, 1], 0: [7, 9]}


def count_chess_paths(dict, length, starting_digits):
    # Draw a grid of 0-9 x lengths, with possible starting digits = 1 else 0
    counts = [0] * 10
    for i in starting_digits: counts[i] = 1 or 0

    for row in range(1, length):
        prev_row = counts
        counts = [0] * 10
        
        for curr, moves in dict.items():
            for move in moves:
            	counts[move] += prev_row[curr]
    
    return sum(counts)





print count_chess_paths(knight, 7, [2,3,4,5,6,7,8,9])
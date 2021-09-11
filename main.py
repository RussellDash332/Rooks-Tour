def game():
  board = [[1, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 1]]

  visited = [[[1, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
              [[0, 0, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
              [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],
                [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]]]

  max_rounds = 15
  curr_round = 1

  teams = [[0,0],
          [1,2],
          [2,1],
          [3,3]]

  eligible = [True]*4
  temp = [[0,0],[0,0],[0,0],[0,0]]
  point = [0,0,0,0]
  move = [[],[],[],[]]

  while curr_round <= max_rounds:
    for team in range(1,5):
      while True:
        while True:
          temp_x = input(f"Team {team}: Where do you want to go (x)? ")
          if temp_x in list(map(str, range(4))):
            temp[team-1][0] = int(temp_x)
            break
          else:
            print("Not a valid x input! Try again :(")

        while True:
          temp_y = input(f"Team {team}: Where do you want to go (y)? ")
          if temp_y in list(map(str, range(4))):
            temp[team-1][1] = int(temp_y)
            break
          else:
            print("Not a valid y input! Try again :(")
          
        # Check for rook move
        if (int(temp_x) == teams[team-1][0]) ^ (int(temp_y) == teams[team-1][1]):
          break
        else:
          print("Not a rook move! Try again :(")

      if visited[team-1][temp[team-1][0]][temp[team-1][1]] == 1: # visited previous spot
        eligible[team-1] = False

      if temp[team-1][0] == teams[team-1][0]: # horizontal
        c = teams[team-1][0]
        d = teams[team-1][1]
        teams[team-1][1] = temp[team-1][1]
      elif temp[team-1][1] == teams[team-1][1]: # vertical
        c = teams[team-1][0]
        d = teams[team-1][1]
        teams[team-1][0] = temp[team-1][0]

      board[c][d] = 0 # Delete from Old
      board[teams[team-1][0]][teams[team-1][1]] = 1 # Move to New
      visited[team-1][teams[team-1][0]][teams[team-1][1]] = 1 # Mark visited

    for a in range(4):
        collision = 0
        for b in range(4):
          if b != a and temp[a] == temp[b]:
            collision = 1
            max_rounds -= 0.5 # will occur twice due to double counting
        if collision == 1:
          move[a].append(0)
        else:
          point[a] = point[a] + 1
          move[a].append(int(eligible[a]))

    # Only one eligible remaining
    game_ends = sum(eligible) <= 1
    
    # Check for row
    if not game_ends:
      for i in range(4):
        if sum(board[i]) >= 3:
          game_ends = True
    
    # Check for column
    if not game_ends:
      for i in range(4):
        result = 0
        for j in range(4):
          result += board[j][i]
        if result >= 3:
          game_ends = True
    
    # Check for diagonal
    if not game_ends:
      diag1 = 0
      diag2 = 0
      for i in range(4):
        diag1 += board[i][i]
        diag2 += board[i][3-i]
      if diag1 >= 3 or diag2 >= 3:
        game_ends = True

    max_rounds = int(max_rounds) # for prettifying float back to int
    print()
    print(f"STEP {curr_round} OF {max_rounds}")
    print("Current board state:")
    for row in board:
      print(row)
    print()

    print("Score: ")
    for i in range(4):
      print(f"Team {i+1}: {move[i]}\tScore: {sum(move[i])}")
    print()

    if game_ends:
      break

    curr_round += 1

    # boundary line
    print("-"*30)

  print("Game ended!")

"""
0 2 1 3 2 0 3 1
0 3 0 3 2 1 3 0 -> ends in 2 turns because Team 1 and Team 2 meet each other

0.0.1.2.2.1.3.3
0 2 1 3 2 0 3 1
0 3 2 3 2 1 3 2
0 2 0 3 2 2 3 3 -> Team 1 gets 0 points for travelling back

0.0.1.2.2.1.3.3
0 2 1 3 2 0 3 1
0 3 0 3 2 1 3 2
0 1 2 3 2 2 3 0
"""

game()

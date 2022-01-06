# Rook's Tour
# Russell Saerang and Darren Lionardo

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

  max_rounds = 8
  curr_round = 1
  check_three_collinear = False

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
          try:
            pos = int(input(f"Team {team}: Where do you want to go (1-16)? "))
            if pos in range(1, 17):
              temp[team-1][0], temp[team-1][1] = (pos - 1) // 4, (pos - 1) % 4
              break
            else:
              print(f"Team {team}: Input not in the correct range! Try again :(")
          except:
            print(f"Team {team}: Not a valid input! Try again :(")
        
        # Check for rook move
        if (temp[team-1][0] == teams[team-1][0]) ^ (temp[team-1][1] == teams[team-1][1]):
          print(f"Team {team} wants to go to {pos}")
          break
        else:
          print(f"Team {team}: Not a rook move! Try again :(")

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
    
    if check_three_collinear:
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

game()

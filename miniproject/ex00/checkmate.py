def checkmate(board_str):
    try:
        board = [list(row) for row in board_str.strip().split("\n")]
        n = len(board)

        # ตรวจสอบว่าเป็นบอร์ดสี่เหลี่ยมจัตุรัส
        if any(len(row) != n for row in board):
            print("Invalid board")
            return

        # หาตำแหน่งของ King
        king_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 'K']
        if len(king_positions) != 1:
            print("Invalid board: Must contain exactly one King")
            return

        ki, kj = king_positions[0]

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < n

        # ตรวจสอบการโจมตีจาก Pawn (เดินขึ้น)
        for dx, dy in [(-1, -1), (-1, 1)]:
            x, y = ki + dx, kj + dy
            if in_bounds(x, y) and board[x][y] == 'P':
                print("Success")
                return

        # ตรวจสอบการโจมตีจาก Rook และ Queen (แนวตรง)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = ki + dx, kj + dy
            while in_bounds(x, y):
                if board[x][y] != '.':
                    if board[x][y] in ('R', 'Q'):
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        # ตรวจสอบการโจมตีจาก Bishop และ Queen (แนวทแยง)
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = ki + dx, kj + dy
            while in_bounds(x, y):
                if board[x][y] != '.':
                    if board[x][y] in ('B', 'Q'):
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        # ตรวจสอบการโจมตีจาก Knight
        for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]:
            x, y = ki + dx, kj + dy
            if in_bounds(x, y) and board[x][y] == 'N':
                print("Success")
                return

        # ถ้าไม่มีตัวใดสามารถโจมตี King ได้
        print("Fail")

    except Exception:
        # ไม่พิมพ์อะไรเลยในกรณี error ตามข้อกำหนด
        pass
def checkmate(board_str):
    try:
        b = board_str.strip().split("\n")
        n = len(b)
        if any(len(r) != n for r in b):
            print("Invalid board"); return
        k = [(i,j) for i in range(n) for j in range(n) if b[i][j]=='K']
        if len(k)!=1:
            print("Invalid board: Must contain exactly one King"); return
        x,y = k[0]
        atk = [(-1,-1),(-1,1)];   # Pawn
        for dx,dy in atk:
            i,j = x+dx, y+dy
            if 0<=i<n and 0<=j<n:
                if (b[i][j]=='P' and dx==-1) :
                    print("Success"); return
        for dx,dy,d in [(-1,0,'RQ'),(1,0,'RQ'),(0,-1,'RQ'),(0,1,'RQ'),
                        (-1,-1,'BQ'),(-1,1,'BQ'),(1,-1,'BQ'),(1,1,'BQ')]:
            i,j = x+dx,y+dy
            while 0<=i<n and 0<=j<n:
                p = b[i][j]
                if p != '.':
                    if p in d:
                        print("Success"); return
                    break
                i+=dx; j+=dy
        print("Fail")
    except: pass

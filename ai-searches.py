from game import*


def segment(board):
    segments=[]
    #horizontal
    for linha in  range (6):
        for coluna in range(7):
            segment=board[linha][coluna:4]
            segments.append(segment)
    #diagonal
    for linha in range(6):
        for coluna in range(7):
            if (linha==coluna):
                segment=board[linha:4][coluna:4]
                segments.append(segment)
    #vertical
    for coluna in range (7):
        for linha in range(6):
            segment=board[linha:4][coluna]
            segments.append(segment)
    return segments

def count(p,seq):
    count=0
    for num in seq:
        if num==p:
            count+=1
    return count

def evaluation_segment(board):
    segments=segment(board)
    evaluation=0
    for seq in segments:
        qX=count(1,seq)
        qO=count(2,seq)
        if qO==2 and qX==0: evaluation-=10    
        if qO==3 and qX==0: evaluation-=50
        if qO==1 and qX==0: evaluation-=1
        if qO==0 and qX==1: evaluation+=1
        if qO==0 and qX==2: evaluation+=10
        if qO==0 and qX==3: evaluation+=50
    return evaluation    

a=evaluation_segment(board_inicial)
print(a)


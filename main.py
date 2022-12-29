def show():
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while True:
        cords = input("Ваш ход (Введите координаты клетки, которую хотите занять): ").split()
        
        if len(cords) != 2:
            print("Введите 2 координаты! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        
        x, y = int(x), int(y)
        
        if x < 0 or x > 2 or  y < 0 or  y > 2 :
            print("Координаты вне диапазона!")
            continue
        
        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        
        return x, y
            
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ставим крестик!")
    else:
        print("Ставим нолик!")
    
    x, y = ask()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print("Ничья!")
        break
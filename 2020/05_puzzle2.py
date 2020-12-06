seats_original = open('05_input.txt', 'r').read().splitlines()

seats = []
for seat in seats_original:
    row = int(seat[:7].replace('F','0').replace('B', '1').replace('L','0').replace('R', '1'), 2)
    column = int(seat[-3:].replace('L','0').replace('R', '1'), 2)
    seat_id = row * 8 + column
    seats.append(seat_id)


seats = sorted(seats)
my_seat = list(set(range(seats[0], seats[-1])) - set(seats))[0]

print("maximum seat id:", seats[-1])
print("my seat:", my_seat)

class Test:
    def __init__(self) -> None:
        super().__init__()
        

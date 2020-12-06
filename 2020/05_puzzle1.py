with open('05_input.txt', 'r') as file:
    seats_original = file.readlines()


heighst_seat_id = 0

for seat in seats_original:
    seat = seat.replace('\n', '')
    row = [0,127]
    for i in seat[0:7]:
        h = round((row[1] - row[0])/2 + 0.49)
        if i == 'F':
            row[1] -= h
        else:
            row[0] += h
    column = [0,7]
    for i in seat[7:]:
        h = round((column[1] - column[0])/2 + 0.49)
        if i == 'L':
            column[1] -= h
        else:
            column[0] += h
    seat_id = row[0] * 8 + column[0]
    if seat_id > heighst_seat_id:
        heighst_seat_id = seat_id

print(heighst_seat_id)
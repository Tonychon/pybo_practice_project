date_rows = ["20201123", "20201124", "20201125", "20201126", "20201127"]
time_rows = ["0900", "0930", "1000", "1030"]
min_rows = []

for item in date_rows:
    for item2 in time_rows:
        min_rows.append(item+item2)

print(min_rows)


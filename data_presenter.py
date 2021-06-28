data = open("CupcakeInvoices.csv")

# for line in data:
#     print(line)

# for line in data:
#     line = line.rstrip('/n').split(',')
#     print(line[2])

# for line in data:
#     line = line.rstrip('/n').split(',')
#     quantity = float(line[3])
#     price = float(line[4])
#     total = quantity*price
#     print(round(total, 2))

# all_total = 0
# for line in data:
#     line = line.rstrip('/n').split(',')
#     quantity = float(line[3])
#     price = float(line[4])
#     total = quantity*price
#     all_total += total

# print(round(all_total,2))

vanilla_total = 0
chocolate_total = 0
strawberry_total = 0

for line in data:
    line = line.rstrip('/n').split(',')
    quantity = int(line[3])
    price = float(line[4])
    total = quantity*price
    if line[2] == 'Vanilla':
        vanilla_total += total
    elif line[2] == 'Chocolate':
        chocolate_total += total
    else:
        strawberry_total += total

# for line in data:
#     print(line)

print("Vanilla: ", round(vanilla_total, 2))
print("Chocolate: ", round(chocolate_total, 2))
print("Strawberry: ", round(strawberry_total, 2))


data.close()
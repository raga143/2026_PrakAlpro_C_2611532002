n = int(input("Number of deposits: "))
totals = {}
for i in range(n):
    parts = input().split()
    name = parts[0]
    amount = int(parts[1])
    if name in totals:
        totals[name] = totals[name] + amount
    else:
        totals[name] = amount

grand = 0
top_name = ""
top_total = -1
for name, total in totals.items():
    print(f"{name}: {total}")
    grand = grand + total
    if total > top_total:
        top_name = name
        top_total = total

print("Total cash:", grand)
print(f"Top contributor: {top_name} ({top_total})")
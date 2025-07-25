colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print(f"colors: len is {len(colors)}; min is {min(colors)}; max is {max(colors)}")
print(f"months: len is {len(months)}; min is {min(months)}; max is {max(months)}")
print()

print("sorted:", end=' ')
for m in sorted(colors):   # sorted() returns a sorted list
    print(m, end=' ')
print()
print(f"{sorted(colors) = }")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

total = sum(nums)
print(f"{total = }")


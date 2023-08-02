new_list = [7, 9, 7, 9, 1, 8, 2]
dup_list = []
for item in new_list:
    if new_list.count(item) > 1 and item not in dup_list:
        dup_list.append(item)
print("Duplicate element:", dup_list)

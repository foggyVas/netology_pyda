"""Выведите на экран все уникальные гео-ID из списка координат ids.
Т. е. список вида [213, 15, 54, 119, 98, 35]
ids = [[‘user1’, [213, 213, 213, 15, 213]],
[‘user2’, [54, 54, 119, 119, 119]], [‘user3’, [213, 98, 98, 35]]]
"""

ids = [['user1', [213, 213, 213, 15, 213]],
       ['user2', [54, 54, 119, 119, 119]],
       ['user3', [213, 98, 98, 35]]
       ]

ids_sorted = list()


for user in range(len(ids)):
       for i in range(len(ids[user][1])):
              if str(ids[user][1][i]).isdigit():
                     if (ids[user][1][i]) in ids_sorted:
                            pass
                     else:
                            ids_sorted.append(ids[user][1][i])
print(ids_sorted)

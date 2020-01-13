import json

purchases = dict()
with open("purchase_log.txt", "r", encoding="UTF-8") as f:
    purchase_log = list(map(json.loads, map(str.strip, f.readlines())))

for user, category in(line.values() for line in purchase_log):
    purchases[user] = category

counter = 0
for key, value in purchases.items():
    if counter < 3:
        print(f"{key}: {value}")
    counter += 1

with open("visit_log.csv") as output_data:
    with open("funnel.csv", "w+") as input_data:
        for line in output_data:
            current_id = line.strip().split(",")[0]
            if purchases.get(current_id, None) != None:
                input_data.write(line.strip() + "," + purchases[current_id] + "\n")
            else:
                pass

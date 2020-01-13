import re

current_text = "edulluke-1905@yopmail.com izisseddudd-4472@yopmail.com " \
               "felalluke-5761@yopmail.com iffellommi-3738@yopmail.com " \
               "dmoh_nori@bethesetopcrossoversonthemarketsok.live " \
               "james27@jordan.com cherylorr@villarreal.org " \
               "bethgonzales@rivers-adams.biz sethscott@thomas-mcdaniel.info " \
               "bubae@rambler.ru"


look_for = r'[\w.-]+@[A-Za-z-]+\.[\w.]+'

results = re.findall(look_for, current_text)

print(len(results), '\n', results)

n = int(input("Сколько весит файл в байтах?: "))
mb = 1048576  # byte in megabytes
byte = mb / 1048576
mbs = (n / mb)   # Megabytes
print("Объем файла равен:", mbs, "Mb")

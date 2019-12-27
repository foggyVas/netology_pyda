stats = {"facebook": 55, "yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}

# Меняет местами ключ-значение
reverse_dict = {v: k for k, v in stats.items()}
print(reverse_dict[sorted(stats.values(), key=lambda x: x)[-1]])

print(sorted(stats.items(), key=lambda x: -x[1])[0][0])

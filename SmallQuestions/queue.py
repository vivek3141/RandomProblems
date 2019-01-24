queue = [1, 10, 8, 5, 12]
LIMIT = 10
d = 0
while True:
    value = queue[0]
    del queue[0]
    print(value)
    d = d + 1
    print(f"Dequeue: {d}")
    time = 0
    while True:
        value = value - 1
        time = time + 1
        if value != 0 and time >= LIMIT:
            break
    if value > 0:
        queue.append(value)
    if not queue:
        break

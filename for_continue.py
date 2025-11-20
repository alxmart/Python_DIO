
for num in range(100):
    if num % 2 == 0:
        #print(num, end=" ")
        if num == 12:
            continue
        print(f"Numero: {num} ")
    else:
        print(f"{num} é ímpar\n", end=" ")
print()

numbers = [12,75,150,180,145,525]
for x in numbers:
    if x % 5 == 0:
        if x > 150:
            continue
        if x > 500:
            break
        print(x);


  
num = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    if (a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66):
                                        num += 1
print(num)

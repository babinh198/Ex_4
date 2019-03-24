
months = [(31, "January"), (28, "February"), (31, "March"), (30, "April"), (31, "May"), (30, "June"),
          (31, "July"), (31, "August"), (30, "September"),(31, "October"), (30, "November"), (31, "December")]
while True:
    num = int(input("nhap vao thang: "))
    if num < 1 or num > 12:
        continue
    print(months[num - 1])  
    break
    
    """
 nhap vao thang: 1
(31, 'January')

    

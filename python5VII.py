# สร้างลิสต์ของหมายเลขจาก 21 ถึง 40
numbers = range(21, 41)

# หาหมายเลขที่เป็นจำนวนคี่
odd_numbers = [num for num in numbers if num % 2 != 0]

# หาหมายเลขที่เป็นจำนวนคู่
even_numbers = [num for num in numbers if num % 2 == 0]

print("จำนวนคี่:", odd_numbers)
print("จำนวนคู่:", even_numbers)

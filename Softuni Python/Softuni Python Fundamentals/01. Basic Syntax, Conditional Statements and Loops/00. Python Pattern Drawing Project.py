# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    for row in range(1, rows+1):
        print('*' * row)

elif choice == 2:  # Square with Hollow Center
    for row in range(size):
        if row in [0, size-1]:
            print('*' * size)
        else:
            print('*' + ' ' * (size-2) + '*')

elif choice == 3:  # Diamond
    #Upper triangle
    half_rows = rows // 2
    for row in range(half_rows):
        print(' ' * (half_rows - row) + '*' * (2 * row + 1))
    # And the lower triangle part
    for row in range(half_rows, -1, -1):
        print(' ' * (half_rows - row) + '*' * (2 * row + 1))

elif choice == 4:  # Left-angled Triangle
    for row in range(rows, 0, -1):
        print('*' * row)

elif choice == 5:  # Hollow Square
    # TODO: Similar to choice 2 but ensure perfect square logic
    pass

elif choice == 6:  # Pyramid
    # TODO: Center-align stars to form a pyramid
    pass

elif choice == 7:  # Reverse Pyramid
    # TODO: Create an upside-down pyramid
    pass

elif choice == 8:  # Rectangle with Hollow Center
    # TODO: Handle separate width and height inputs for rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    pass

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit
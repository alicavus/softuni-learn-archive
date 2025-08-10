number_of_electrons = int(input())

electron_configuration = []

cur_shell = 1

for idx in range(number_of_electrons):
    cur_shell = idx+1
    max_electrons = 2 * cur_shell ** 2

    electron_configuration += [max_electrons if number_of_electrons >= max_electrons else number_of_electrons]

    number_of_electrons -= electron_configuration[idx]

    if not number_of_electrons:
        break

print(electron_configuration)
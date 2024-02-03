def opening_file(name: str):
    file = open(name, encoding="UTF-8")
    file.readline()
    result = []
    for row in file.readlines():
        if row[-1] == "\n":
            row = row[:-1]
        znach = row.split("*")
        name_ship, num_ship = znach[0].split("-")
        home_planet = znach[1]
        x_coord, y_coord = znach[2].split()
        x_direction, y_direction = znach[3].split()
        result.append([name_ship, num_ship, home_planet, x_coord, y_coord, x_direction, y_direction])
    file.close()
    return result


def writing_file(name: str, data: list):
    file_w = open(name, "w", encoding="UTF-8")
    for row in data:
        file_w.write(row)
        file_w.write("\n")
    file_w.close()

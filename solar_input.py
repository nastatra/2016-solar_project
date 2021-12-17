# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)

            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)

            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    #   pass  # FIXME: not done yet

    r, color, m, x, y, Vx, Vy = float(line.split()[1]), str(line.split()[2]), float(line.split()[3]), \
                                float(line.split()[4]), float(line.split()[5]), float(line.split()[6]), float(
        line.split()[7])
    star.R = r
    star.color = color
    star.m = m
    star.x = x
    star.y = y
    star.Vx = Vx
    star.Vy = Vy


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    #    pass  # FIXME: not done yet...

    r, color, m, x, y, Vx, Vy = float(line.split()[1]), str(line.split()[2]), float(line.split()[3]), \
                                float(line.split()[4]), float(line.split()[5]), float(line.split()[6]), float(
        line.split()[7])
    planet.R = r
    planet.color = color
    planet.m = m
    planet.x = x
    planet.y = y
    planet.Vx = Vx
    planet.Vy = Vy


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            line = []
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

            if obj.type == "star":
                line.append("Star")
            elif obj.type == "planet":
                line.append("Planet")
            line.append(str(obj.R))
            line.append(obj.color)
            line.append(str(obj.m))
            line.append(str(obj.x))
            line.append(str(obj.y))
            line.append(str(obj.Vx))
            line.append(str(obj.Vy))
            out_file.write(line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " "
                           + line[4] + " " + line[4] + " " + line[5] + " " + line[6] + " " + line[7] + "\n")


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")


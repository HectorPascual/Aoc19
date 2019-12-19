def calc_fuel(mass):
    return int(mass/3)-2


if __name__ == "__main__":
    with open('ao.txt') as f:
        fuels = [calc_fuel(int(mass)) for mass in f]
        combined_fuels = sum(fuels)
    print(combined_fuels)

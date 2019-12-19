def calc_fuel(mass):
    return int(mass/3)-2


def calc_recursive_fuel(mass, total_fuel=0):
    mass_fuel = calc_fuel(mass)
    total_fuel += mass_fuel
    if calc_fuel(mass_fuel) > 0:
        return calc_recursive_fuel(mass_fuel, total_fuel)
    else:
        return total_fuel


if __name__ == "__main__":
    with open('ao.txt') as f:
        fuels = [calc_recursive_fuel(int(mass)) for mass in f]
        combined_fuels = sum(fuels)
    print(combined_fuels)

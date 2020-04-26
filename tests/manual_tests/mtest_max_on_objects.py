from protocol.problem_11_p_8_var3 import Building


if __name__ == "__main__":
    b1 = Building(1, 0)
    b2 = Building(3, 1)
    b3 = Building(2, 2)
    buildings = [b1, b2, b3]
    print(max(buildings).distance)

from vlad.problem_5_p_1_vlad import Problem5P1Vlad


if __name__ == "__main__":
    pivot = 3
    unpartitioned_list = [1, 2, 3, 3, 2, 1]
    Problem5P1Vlad().one_pass_dutch_flag_partition(pivot, unpartitioned_list)
    print(unpartitioned_list)
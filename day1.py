def per_elf_total(elf_cals: str) -> int:
    str_cals = elf_cals.split("\n")
    return sum(map(int, str_cals))


with open("input/day1input.txt") as file:
    cal_strings = file.read().split("\n\n")
    cal_totals = sorted(list(map(per_elf_total, cal_strings)), reverse=True)
    print(f"Top calorie elf: {cal_totals[0]}")
    top_3_elf_total = sum(cal_totals[:3])
    print(f"Top 3 elf total: {top_3_elf_total}")

example = {
    "defenestrate": "the act of throwing something or someone out of a window",
    4: "four",
    "four": 4,
    "Phoebe": ["Phoebe", 25, True],
    "Braden": ["Braden", 25, True]
}

example["Chase"] = ["Chase", 21, True]

print(example["Phoebe"][1])
print(example["Braden"][2])
print(example["Chase"][2])
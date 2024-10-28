import numpy as np


def medical_specialty_visited(facility_visited):
    medical_specialities = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
    all_nums = list(filter(lambda x: x.isdigit(), facility_visited))
    return medical_specialities[
        facility_visited[facility_visited.index(max(all_nums)) + 1]
    ]


print(medical_specialty_visited(["101", "P", "102", "O", "302", "P", "305", "P"]))
print(
    medical_specialty_visited(
        ["101", "O", "102", "O", "302", "P", "305", "E", "401", "O", "656", "O"]
    )
)
print(
    medical_specialty_visited(
        [
            "101",
            "O",
            "102",
            "E",
            "302",
            "P",
            "305",
            "P",
            "401",
            "E",
            "656",
            "O",
            "987",
            "E",
        ]
    )
)

# Test case 1: All specialties are Pediatrics
assert medical_specialty_visited(["101", "P", "102", "P", "302", "P", "305", "P"]) == "Pediatrics"

# Test case 2: All specialties are Orthopedics
assert medical_specialty_visited(["101", "O", "102", "O", "302", "O", "305", "O"]) == "Orthopedics"

# Test case 3: All specialties are ENT
assert medical_specialty_visited(["101", "E", "102", "E", "302", "E", "305", "E"]) == "ENT"

# Test case 4: Mixed specialties, Pediatrics has the highest number
assert medical_specialty_visited(["101", "P", "102", "O", "302", "P", "305", "P"]) == "Pediatrics"

# Test case 5: Mixed specialties, Orthopedics has the highest number
assert medical_specialty_visited(["101", "O", "102", "O", "302", "P", "305", "E", "401", "O", "656", "O"]) == "Orthopedics"

# Test case 6: Mixed specialties, ENT has the highest number
assert medical_specialty_visited(["101", "O", "102", "E", "302", "P", "305", "P", "401", "E", "656", "O", "987", "E"]) == "ENT"

print("All test cases passed!")

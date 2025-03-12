students[
    {"name" : "Tom", "house", "Grif"},
    {"name" : "Greg", "house", "Grif"},
    {"name" : "Janet", "house", "Grif"},
    {"name" : "Michael", "house", "Sly"}
]

def is_grif(s):
    return s["house"] == "Grif"


grifs = filter(is_grif, students)

for grif in sorted(grifs, key=lambda s: s["name"]):
    print(grif["name"]
          
          )
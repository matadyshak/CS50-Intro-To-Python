class Student:
    def _init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in  ["Grif", "Huff", "Raven"], "Sly"]
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    # student.house = "Number Four, Privit Drive"   #Prohibited by setter
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except Value:

@property
def house(self):
    return self._house

@house.setter
def house(self, house):
    if house not in ["Grif", "Huff", "Raven", "Sly"]
        raise ValueError("Invalid house")
    self._house = house


if __name__ == "__main__":
    main()

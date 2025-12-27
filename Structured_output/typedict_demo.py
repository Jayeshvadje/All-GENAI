from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int


new_person:Person = {"name" : "Jayesh", "age" :18}

print(new_person)




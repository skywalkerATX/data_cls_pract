# learning from arjan's video
import random
import string
import timeit
from dataclasses import dataclass, field
from functools import partial


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))


@dataclass(slots=False,match_args=False)   # match_args=True matches dunnder methods, for structured pattern matching (frozen=true) frozen=True means that the class is immutable can't be changed.. kw_only means that all arguments must be keyword arguments
class Person:
    name: str
    address: str
    email: str

@dataclass(slots=True,match_args=False) 
class PersonSlots:
    name: str
    address: str
    email: str


# class PersonEmployee(PersonSlots, EmployeeSlots):  --- example of multiple inheritance where SLOTS don't work

    # active: bool = True  # primitive type, this default works 
    # email_addresses: list[str] = field(default=list)  # list type, field ensures that the default value is variable not the same value for each
    # id: str = field(init=False,default_factory=generate_id)  # init=False means that this field is not included in the __init__ method
    # _search_string: str = field(init=False, repr=False)  # init=False means that this field is not included in the __init__ method. setting repr to false ensures that it's not printed

    # def __post_init__(self) -> None:
    #     self._search_string = f"{self.name} {self.address}"  # this is a computed field

def get_set_delete(person: Person | PersonSlots):  # new union type in 3.10
    person.address = "123 Main St" # this is a setter
    person.address # this is a getter
    del person.address # this is a deleter



def main() -> None:  
    person = Person("John", "123 Main St", "john@doe.com") # this is a constructor
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com") # this is a constructor
    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000)) # this is a constructor
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000)) # this is a constructor
    print(f"no slots: {no_slots}")
    print(f"slots: {slots}")
    print(f"% performance improvement: {no_slots - slots / no_slots:.2%}") # this calculates the performance improvement when using slots

    # person.name = "Luke" -- this won't work when frozen=True
    # print(person.__dict__["name"])  # example showing how dunders work and showing that objects are just dictionaries
    # print(person)

if __name__ == '__main__':
    main()

from data.data_person import Person
from faker import Faker

faker_en = Faker('En')

def generate():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        address=faker_en.address()
    )
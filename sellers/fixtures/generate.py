import json

from faker import Faker

fake = Faker()


def generate():
    return {
        "model": "sellers.seller",
        "pk": fake.uuid4(),
        "fields": {
            "name": fake.company(),
            "description": fake.paragraph(),
            "email": fake.email(),
            "address1": fake.address(),
            "address2": fake.address(),
            "zip_code": fake.zipcode(),
            "city": fake.city(),
            "country": "ar",
            "created_at": "2020-07-30T20:10:24.100Z",
            "is_mock": fake.boolean(),
            "is_active": fake.boolean(),
            "logo": fake.image_url(),
            "header_image": fake.image_url(),
            "owner": 1
        }
    }


data = [generate() for _ in range(50)]

with open('sellers/fixtures/sellers.json', 'w') as f:
    f.write(json.dumps(data))

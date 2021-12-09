import json

from faker import Faker

fake = Faker()


def generate():
    return {
        "model": "products.product",
        "pk": fake.uuid4(),
        "fields": {
            "title": fake.word(),
            "description": fake.paragraph(),
            "price": str(fake.random_int()),
            "active": fake.boolean(),
            "in_stock": fake.boolean(),
            "date_updated": "2020-07-30T21:08:20.119Z",
            "seller": "9db3c6f9-fd3e-4490-9529-b97c205ef866",
            "tags": [
            ]
        }
    }


data = [generate() for _ in range(50)]

with open('products/fixtures/products.json', 'w') as f:
    f.write(json.dumps(data))

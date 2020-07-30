import json

from faker import Faker

fake = Faker()


def generate():
    return {
        "model": "products.producttag",
        "fields": {
            "name": fake.word(),
            "slug": fake.slug(),
            "description": fake.paragraph(),
            "active": fake.boolean()
        }
    }


data = [generate() for i in range(50)]

with open('products/fixtures/producttags.json', 'w') as f:
    f.write(json.dumps(data))

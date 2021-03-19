import random

first_name = ["Apurba", "Apu", "Shuvra", "Partho", "Rothosri", "Nipa", "Puspa"]

last_name = ["Nath", "Debnath", "Saha", "Chakraborty", "Poddar", "Paul", "Sarkar" ]

street_name = ["Dhanmondi", "Kolabagan", "Adalatpara", "Najirpara", "Mohakhali", "Uttora"]

fake_cities = ["DFG", "KLJ", "CVB", "SER", "TYU", "GHU", "CVN","SWER"]

states = ["AK", "LL", "OL", "PO", "YU", "DF", "YUK", "JKL"]
print("Fake Address Generator for 100 persons /:----------------------------------->>>>>>>>>>.")
for num in range(100):
    first = random.choice(first_name)
    last = random.choice(last_name)
    phone = f"01-{random.randint(1,9)}-{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(10,99)}"
    street_num = random.randint(100,999)
    street = random.choices(street_name)
    city= random.choices(fake_cities)
    state = random.choices(states)
    zipcode = random.randint(1000,9999)
    address = f"{street_num}, {street}, ct-{city}, {state} ,zp-{zipcode}"
    email = first.lower() + last.lower() + "@gmail.com"
    print(f"{num}-Person: ")
    print(f"{first} {last}\n{phone}\n{address}\n{email}\n")

    

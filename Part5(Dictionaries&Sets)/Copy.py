animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals.copy()

animals["teddy"] = "toy"
print(things["teddy"])
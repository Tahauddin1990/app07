
greetings = "Hello Mr. "
greetings_copy = greetings
print(f"id of greetings :: {id(greetings)}")
print(f"id of greetings Copy Before changing :: {id(greetings_copy)}")
print(f"both the variables are pointing to the same value hence both are equal {id(greetings)} {id(greetings_copy)}")

greetings_copy = "Hello Miss. "
print(f"modifying the greetings copy value , to {greetings_copy}, this modifies only greeting copy but not greetings")
print(f"id of greetings :: {id(greetings)}")
print(f"id of greetings Copy After changing :: {id(greetings_copy)}")
print(f"both the variables are pointing to the different value hence both are not equal {id(greetings)} {id(greetings_copy)}")



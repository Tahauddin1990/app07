
string_sentence = "Three generations with six decades of life experience."
string_one = "Three"
string_two = "generations"
string_three = "with"
string_four = "six"
string_five = "decades"
string_six = "of"
string_seven = "life"
string_eight = "experience."

print(string_sentence)

string_joined_sentence = " ".join([string_one, string_two, string_three, string_four, string_five, string_six, string_seven, string_eight])
print(string_joined_sentence)

print(id(string_sentence))
print(id(string_joined_sentence))

print(string_sentence == string_joined_sentence)
print(hash(string_sentence) == hash(string_joined_sentence))
print(id(string_sentence) == id(string_joined_sentence))
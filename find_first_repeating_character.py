def find_first_repeating_character(s):
    char_count = {}

    for char in s:
        if char in char_count:
            print(f"The first repeating character is '{char}' with memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1

    print("No repeating character found.")
    return None
find_first_repeating_character("abcdaa")
data = input()
template = input()

searching_letters = set(template)
found_anagrams = 0

for start_search_index in range(len(data)):
    seen_letters = set()

    for current_search_index in range(start_search_index, len(data)):
        letter = data[current_search_index]

        if letter not in searching_letters:
            break

        seen_letters.add(letter)
        if seen_letters == searching_letters:
            found_anagrams += 1
            break

print(str(found_anagrams))

def uniq(input):
    have = set()
    for element in input:
        if not element in have:
            print(element, 'nicht vorhanden')
            yield element
            have.add(element)

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]

uniquified = uniq(input_list)
for element in uniquified:
    print(element)

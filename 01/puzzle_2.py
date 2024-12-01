from puzzle_1 import load_input_to_lists

if __name__ == "__main__":
    location_lists = load_input_to_lists()

    location_count = {}
    for location in location_lists[1]:
        location_count[location] = location_count.get(location, 0) + 1

    similarity_scores = [
        location * location_count.get(location, 0) for location in location_lists[0]
    ]
    print(sum(similarity_scores))

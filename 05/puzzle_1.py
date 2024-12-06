def load_input(
    filename: str = "05/input",
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = []
    pages = []
    with open(filename) as f:
        for line in f.readlines():
            if "|" in line:
                rules.append(tuple([int(n) for n in line.strip().split("|")]))
            if "," in line:
                pages.append([int(n) for n in line.strip().split(",")])

    return rules, pages


def filter_valid_pages(
    rules: list[tuple[int, int]], pages: list[list[int]], return_valid: bool = True
) -> list[list[int]]:
    filtered_pages = []
    for page in pages:
        valid = True
        for rule in rules:
            if (
                rule[0] in page
                and rule[1] in page
                and page.index(rule[0]) > page.index(rule[1])
            ):
                valid = False
                break

        if valid == return_valid:
            filtered_pages.append(page)

    return filtered_pages


def get_middle_page_numbers(pages: list[list[int]]) -> list[int]:
    return [page[len(page) // 2] for page in pages]


def main():
    test_rules, test_pages = load_input(filename="05/test_input")
    test_result = sum(
        get_middle_page_numbers(filter_valid_pages(test_rules, test_pages))
    )
    assert test_result == 143

    rules, pages = load_input()
    result = sum(get_middle_page_numbers(filter_valid_pages(rules, pages)))
    print(result)


if __name__ == "__main__":
    main()

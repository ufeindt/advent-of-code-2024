from copy import deepcopy
from puzzle_1 import load_input, get_middle_page_numbers, filter_valid_pages


def correct_invalid_pages(
    rules: list[tuple[int, int]], pages: list[list[int]], max_depth: int = 10
) -> list[list[int]]:
    if max_depth == 0:
        return pages
    pages = deepcopy(pages)
    corrected_pages = []
    corrected_any_pages = False
    for page in pages:
        for rule in rules:
            if (
                rule[0] in page
                and rule[1] in page
                and (index_0 := page.index(rule[0])) > (index_1 := page.index(rule[1]))
            ):
                corrected_page = []
                if index_1 > 0:
                    corrected_page.extend(page[:index_1])
                corrected_page.append(rule[0])
                corrected_page.extend(page[index_1:index_0])
                if index_0 < len(page) - 1:
                    corrected_page.extend(page[index_0 + 1 :])

                page = corrected_page
                corrected_any_pages = True

        corrected_pages.append(page)

    if corrected_any_pages:
        return correct_invalid_pages(rules, corrected_pages, max_depth=max_depth - 1)
    return corrected_pages


def main():
    test_rules, test_pages = load_input(filename="05/test_input.txt")
    test_result = sum(
        get_middle_page_numbers(
            correct_invalid_pages(
                test_rules,
                filter_valid_pages(test_rules, test_pages, return_valid=False),
            )
        )
    )
    assert test_result == 123

    rules, pages = load_input()

    result = sum(
        get_middle_page_numbers(
            correct_invalid_pages(
                rules,
                filter_valid_pages(rules, pages, return_valid=False),
            )
        )
    )
    print(result)


if __name__ == "__main__":
    main()

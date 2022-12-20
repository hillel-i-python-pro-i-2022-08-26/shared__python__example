import random
from queue import Queue


def _generate_data():
    return [random.randint(0, 1000) for _ in range(10)]


def make_action(number: int):
    return _generate_data()


def processing(items: list[int]) -> list[int]:
    all_links = set()
    links_by_order = []
    queue = Queue()
    for item in items:
        queue.put(item)
    # queue = [*items]

    # while not len(queue):
    #     item = queue.pop()

    counter = 0
    while not queue.empty():
        item = queue.get()

        results_items = make_action(item)

        for result_item in results_items:
            if result_item not in all_links:
                queue.put(result_item)
                # queue.append(result_item)
                all_links.add(result_item)
                links_by_order.append(result_item)

        counter += 1
    return list(all_links)


def main():
    items = _generate_data()

    processing(items=items)


if __name__ == "__main__":
    main()

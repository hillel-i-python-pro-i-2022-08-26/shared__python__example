class MyContextManager:
    def __enter__(self):
        print("Hi")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end")


def make():
    try:
        print("Hi")
    finally:
        print("end")


def main():
    with MyContextManager():
        print("Something")

    # with open('my_file.txt') as file:
    #     text = file.read()


if __name__ == "__main__":
    main()

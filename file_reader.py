def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    read_file("sample.txt")

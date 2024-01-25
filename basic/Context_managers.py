"""

This will provide the code details for context managers

"""


# custom context managers
class MyFileContextManager:
    def __init__(self, filename):
        self._filename = filename

    def __enter__(self):
        self._file = open(self._filename, "a+")
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


if __name__ == "__main__":
    with MyFileContextManager("TestContextManager.text") as file:
        file.write("Test_write")

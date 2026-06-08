from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

        print(f"Запись в файл: {message}")

file_logger = FileLogger('log.txt')

file_logger.log("Тест")
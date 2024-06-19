import configparser
import csv
import os


class ReadConfig:
    @staticmethod
    def get_config_path():
        return os.path.join(os.path.dirname(__file__), '../Configure/config.init')

    @staticmethod
    def get_logs_directory():
        config = configparser.ConfigParser()
        config.read(ReadConfig.get_config_path())
        return config['DEFAULT']['LogsDirectory']

    @staticmethod
    def get_csv_file_path():
        config = configparser.ConfigParser()
        config.read(ReadConfig.get_config_path())
        return config['DEFAULT']['CSVFilePath']

    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]
        return data


# Usage example
if __name__ == "__main__":
    logs_directory = ReadConfig.get_logs_directory()
    csv_file_path = ReadConfig.get_csv_file_path()
    csv_data = ReadConfig.read_csv(csv_file_path)
    print(f"Logs Directory: {logs_directory}")
    print(f"CSV Data: {csv_data}")

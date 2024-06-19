import configparser
import csv
import os


class ReadConfig:
    @staticmethod
    def get_config_path():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '../Configure/config.init'))

    @staticmethod
    def get_config():
        config_path = ReadConfig.get_config_path()
        print(f"Reading config file from: {config_path}")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r') as file:
            content = file.read()
            print(f"Config file content:\n{content}")

        config = configparser.ConfigParser()
        config.read_string(content)
        print(f"Config sections: {config.sections()}")
        if 'DEFAULT' in config:
            print(f"Config keys in DEFAULT: {list(config['DEFAULT'].keys())}")
            for key in config['DEFAULT']:
                print(f"{key}: {config['DEFAULT'][key]}")
        return config

    @staticmethod
    def get_logs_directory():
        config = ReadConfig.get_config()
        try:
            logs_directory = config['DEFAULT']['LogsDirectory']
            return os.path.abspath(os.path.join(os.path.dirname(ReadConfig.get_config_path()), logs_directory))
        except KeyError:
            raise KeyError("LogsDirectory key is missing in the configuration file")

    @staticmethod
    def get_csv_file_path():
        config = ReadConfig.get_config()
        try:
            csv_file_path = config['DEFAULT']['CSVFilePath']
            return os.path.abspath(os.path.join(os.path.dirname(ReadConfig.get_config_path()), csv_file_path))
        except KeyError:
            raise KeyError("CSVFilePath key is missing in the configuration file")

    @staticmethod
    def read_csv(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]
        return data


# Usage example
if __name__ == "__main__":
    try:
        logs_directory = ReadConfig.get_logs_directory()
        csv_file_path = ReadConfig.get_csv_file_path()
        csv_data = ReadConfig.read_csv(csv_file_path)
        print(f"Logs Directory: {logs_directory}")
        print(f"CSV Data: {csv_data}")
    except FileNotFoundError as e:
        print(e)
    except KeyError as e:
        print(e)

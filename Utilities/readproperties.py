import configparser
import csv


class ReadConfig:
    @staticmethod
    def get_logs_directory():
        config = configparser.ConfigParser()
        config.read('C:/Users/RAMESH SINGH/PycharmProjects/SoundBox_APP/Configure/config.init')
        return config['DEFAULT']['LogsDirectory']

    @staticmethod
    def get_csv_file_path():
        config = configparser.ConfigParser()
        config.read('C:/Users/RAMESH SINGH/PycharmProjects/SoundBox_APP/Configure/config.init')
        return config['DEFAULT']['CSVFilePath']

    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]
        return data

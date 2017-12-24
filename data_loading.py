import csv
import traceback


def load_csv_file(filename):
    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=';')
        data = {}
        for line in reader:
            try:
                date = line['Date']
                kwh = float(line['kWh'].replace(',', '.'))
                temp = float(line['Température moyenne (°C)'].replace(',', '.'))
            except Exception:
                print(f'Error reading file {filename}')
                traceback.print_exc()
                raise
            assert date not in data
            data[date] = {'kwh': kwh, 'temp': temp}
    return data


def load_csv_files(*filenames):
    data_all = {}
    for f in filenames:

        data = load_csv_file(f)

        # check if we have the same date twice
        all_dates = set(data_all).intersection(data)
        if len(all_dates) > 0:
            raise ValueError(f'File "{f}" adds redundate dates')

        data_all.update(data)
    return data_all

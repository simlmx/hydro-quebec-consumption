import csv
import traceback


def load_csv_file(filename):
    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=';')
        data = {}
        for line in reader:
            try:
                date = line['Date']
                kwh = line['kWh'].replace(',', '.')
                temp = line['Température moyenne (°C)'].replace(',', '.')

                if temp == '' or kwh == '':
                    continue

                kwh = float(kwh)
                temp = float(temp)
            except Exception:
                print('Error reading file {}'.format(f))
                print(line)
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
            raise ValueError('File "{}" adds redundate dates'.format(f))

        data_all.update(data)
    return data_all

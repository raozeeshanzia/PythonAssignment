import csv
def csv_writer(all_product):
    keys = []
    if len(keys) == 0:
        keys = all_product[0].keys()
    with open('../output/csv/city_list.csv', 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(all_product)

def open_csv_file():
    keys = ['city_name', 'program_name']
    my_file = open('../output/csv/city_list.csv', 'w')
    writer = csv.writer(my_file)
    writer.writerow(keys)
    return writer
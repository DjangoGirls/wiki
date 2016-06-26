import csv
import sys
import datetime


def read_statement(filename):
    source_data = []
    with open('source.csv', 'rb') as sourcefile:
        reader = csv.DictReader(sourcefile)
        for row in reader: 
            source_data.append(row)
    return source_data

def normalize_source(source_data):
    normalized_data = []

    # Remove transactions without reference ID -- we don't want currency conversion transactions
    for row in source_data:
        if row[' Reference Txn ID'] == '':
            normalized_data.append(row)

    transactions = {row[' Transaction ID']: row for row in normalized_data}
    
    # Replace USD values with GBP values if transaction currency was converted
    for row in source_data:
        if row[' Currency'] == 'USD' and row[' Reference Txn ID'] != '':
            id = row[' Reference Txn ID']
            if id in transactions:
                transactions[id][' Fee'] = row[' Fee']
                transactions[id][' Gross'] = row[' Gross']
                transactions[id][' Net'] = row[' Net']
                transactions[id][' Currency'] = row[' Currency']

    return transactions.values()

def write_csv(data):
    fieldnames = ['Description on bank statement', 'Item', 'Category', 'Date', 'Money in USD', 'Money in GBP', 'Money out USD', 'Money out GBP', 'Account', 'Is refunded?']
    output_filename = 'paypal_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d'))
    
    with open(output_filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for row in data:
            name = '{} / {}'.format(row[' Name'], row[' Transaction ID'])
            if row[' Currency'] == 'GBP' and '-' in row[' Net']:
                writer.writerow([name, '', '', row['Date'], '', '', '', row[' Net'].replace('-', ''), 'PayPal', '-'])
            elif row[' Currency'] == 'GBP' and not '-' in row[' Net']:
                writer.writerow([name, '', '', row['Date'], '', row[' Net'], '', '', 'PayPal', '-'])
            elif row[' Currency'] == 'USD' and '-' in row[' Net']:
                writer.writerow([name, '', '', row['Date'], '', row[' Net'].replace('-', ''), '', '', 'PayPal', '-'])
            elif row[' Currency'] == 'USD' and not '-' in row[' Net']:
                writer.writerow([name, '', '', row['Date'], row[' Net'], '', '', '', 'PayPal', '-'])
            print 'Transaction {} on {} processed'.format(name, row['Date'])
    
    print 'CSV saved to {}'.format(output_filename)


if __name__ == "__main__":
    source_data = read_statement(sys.argv[1])
    normalized_data = normalize_source(source_data)
    write_csv(normalized_data)

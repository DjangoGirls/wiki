import csv
import datetime
import sys

def read_statement(filename):
    source_data = []
    with open(filename, 'rb') as sourcefile:
        reader = csv.DictReader(sourcefile)
        for row in reader: 
            source_data.append(row)
    return source_data

def write_csv(source_data):
    fieldnames = ['Description on bank statement', 'Item', 'Category', 'Date', 'Money in USD', 'Money in GBP', 'Money out USD', 'Money out GBP', 'Account', 'Is refunded?']
    output_filename = 'cafbank_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d'))

    with open(output_filename, 'w') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(fieldnames)
        
        x = 8 # first row with actual data
        while len(source_data[x]) > 1:
            item = source_data[x][None]
            writer.writerow([item[1], '', '', item[0], '', item[3], '', item[2], 'CAF Bank', '-'])
            x += 1
            print 'Transaction {} on {} processed'.format(item[1], item[0])
    print 'CSV saved to {}'.format(output_filename)

if __name__ == "__main__":
    source_data = read_statement(sys.argv[1])
    write_csv(source_data)
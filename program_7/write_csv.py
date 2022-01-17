from csv import DictReader

salesorder_dictionary={}

file = open("practisecsv.csv","r",encoding="utf8")
csv_reader=DictReader(file)
for row in csv_reader:
    if row['Order No'] in salesorder_dictionary:
        salesorder_dictionary[row['Order No']]['Orderlines'].append({'SKU': row.get('SKU'),
                                                       'Price': row.get('Price'),
                                                       'Qty': row.get('Qty')})
    else:
        salesorder_dictionary.update({row.get('Order No'):
                                      {'Customer':
                                           {'Name': row.get('Customer'),
                                            'Address1': row.get('Address'),
                                            'Address2': row.get('Address2'),
                                            'City': row.get('City'),
                                            'Country': row.get('Country'),
                                            'ZipCode': row.get('Zipcode')
                                             },
                                       'Orderlines': [{'SKU': row.get('SKU'),
                                                       'Price': row.get('Price'),
                                                       'Qty': row.get('Qty')}]
                                       }
                                  })

file_for_write = open("sample.csv", "w")

import csv

field_names=['OrderNo','Customer','SKU','Qty','Price','Address1','Address2','Zipcode','City','Contry']

with open('OrderDetails.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for key, values in salesorder_dictionary.items():
        for val in values['Orderlines']:
            writer.writerow({'OrderNo':key,
                        'Customer':values['Customer']['Name'],
                        'SKU': val['SKU'],
                        'Qty': val['Qty'],
                        'Price': val['Price'],
                        'Address1': values['Customer']['Address1'],
                        'Address2': values['Customer']['Address2'],
                        'Zipcode': values['Customer']['ZipCode'],
                        'City': values['Customer']['City'],
                        'Contry': values['Customer']['Country'],
                        })
from csv import  DictReader

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

for key,values in salesorder_dictionary.items():
    print(key,values)
# file.close()


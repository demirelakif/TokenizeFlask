import csv
    

with open('test.csv',encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            if row[1] == "Yulaf İçeceği":
                
                print(f'\t{row[0]} ,  {row[1]} , {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


import pandas as pd
df = pd.DataFrame({'Id': [line_count],
                   'Key': [6],
                   'Tag': [15],
                   'Category': [15],
                   'Description': [''],
                   })


df.to_csv('test.csv', mode='a', index=False, header=False)
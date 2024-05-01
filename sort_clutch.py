import csv

input_file = 'clutch-04-2023-web-designers.csv'
output_file = 'result.csv'  # Новое имя файла или то же самое

with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as new_csv_file:
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames + ['Name', 'Sites']
    
    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        email = row['mail']
        name, site = email.split('@')
        
        row['Name'] = name
        row['Sites'] = site
        
        writer.writerow(row)

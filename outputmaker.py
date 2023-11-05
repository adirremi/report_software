import csv


def save_files(My_report,Company_report,duplicate_keys1,duplicate_keys2,mistake_list):
    output_csv_file1 = 'output/my_report.csv'
    output_csv_file2 = 'output/company_report.csv'
    output_csv_file3 = 'output/mistakes.csv'
    my_dict =[]

    #print("hey")
    dict_list = []
    for item in mistake_list:
        item_dict = {'address': item[0], 'comments': item[1]}
        dict_list.append(item_dict)


    # Convert dict_keys to a list and add the "Comment" field
    fieldnames1 = list(My_report[0].keys())
    fieldnames1.append('Comment')

    # Write the filtered data from My_report to the first CSV file
    with open(output_csv_file1, mode='w', newline='', encoding='utf-8') as file1:
        writer1 = csv.DictWriter(file1, fieldnames=fieldnames1)
        writer1.writeheader()
        for job in My_report:
            writer1.writerow(job)

        # Add a comment for the last row
        writer1.writerow({'Comment': duplicate_keys1})

    # Convert dict_keys to a list and add the "Comment" field
    fieldnames2 = list(Company_report[0].keys())
    fieldnames2.append('Comment')

    # Write the filtered data from Company_report to the second CSV file
    with open(output_csv_file2, mode='w', newline='', encoding='utf-8') as file2:
        writer2 = csv.DictWriter(file2, fieldnames=fieldnames2)
        writer2.writeheader()
        for job in Company_report:
            writer2.writerow(job)

        # Add a comment for the last row
        writer2.writerow({'Comment': duplicate_keys2})
    fieldnames3 = ['address','comments']
    #header_mistake = "mistake list parts and total rate"
    with open(output_csv_file3, mode="w", newline='') as file:
        writer3 = csv.DictWriter(file, fieldnames=fieldnames3)
       # writer3 = csv.writer(file)
        writer3.writeheader()
        for row in dict_list:
            writer3.writerow(row)

    # Specify the CSV file name




    print("CSV file created successfully.")


    print(f"{output_csv_file1} and {output_csv_file2} created successfully.")

    print("this mistake in the jobs in parts or total :")
    for job in mistake_list:
        print(job)
    return print("All Done")
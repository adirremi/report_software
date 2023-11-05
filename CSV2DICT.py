import csv
from clean import remove_non_letters_from_end,normalize_string
def csv_to_dict_list(csv_file):
    data = []

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader)
        for row in csv_reader:
            address = row.get('address', '').strip().lower().strip()
            job_type = row.get('job type', '').strip().lower().strip().replace("fix ignition","car key").replace("residential lock change","lock change").replace("new key fob","car key")
            last_five_chars = address[-5:]

            # Check if the last five characters are numeric
            if last_five_chars.isdigit():
                zip_code = last_five_chars
                address = address[:-5].replace("&","and").replace(",","").replace("avenue","ave").replace("road","rd").replace("street","st").replace("east","e").replace("west","w").replace("north","n").replace("south","s").replace("court","ct").replace("boulevard","blvd").replace("highway","hwy").replace("blv","blvd")
            else:
                zip_code = '00000'

            # Convert 'total' and 'parts' to integers
            total = float(row.get('total', '0'))
            parts = float(row.get('parts', '0'))
            job_type = remove_non_letters_from_end(job_type)
            address = remove_non_letters_from_end(address)
            address = normalize_string(address)
            job_type = normalize_string(job_type)
            if address[-1] == " ":
                address.replace(" ","")
            #total = int(row.get('total', '0'))
            #parts = int(row.get('parts', '0'))

            # Create a new dictionary with the modified fields
            processed_data = {
                'address': address,
                'total': int(total),
                'parts': int(parts),
                'job type': job_type,
                'zip code': int(zip_code)
            }

            data.append(processed_data)

    return data

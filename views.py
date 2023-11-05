from CSV2DICT import csv_to_dict_list
from HTML2CSV import html2csvUR,html2csvTHEY
from duplicate_checker import has_duplicate_keys
import compare
from zipcode_checker import zipcode_mistake
from parts_checker import parts_mistake
from total_checkr import total_rate_mistake
from outputmaker import save_files
import os
import csv
from flask import Flask, render_template, request, redirect, url_for,Blueprint
from web_print import print_web
from flask import Flask, render_template, request, redirect, url_for


   # os.makedirs(GENERATED_FILES_DIR, exist_ok=True)

#app.register_blueprint(app, url_prefix='/')
#app = Blueprint('app', __name__)
app = Flask(__name__)
GENERATED_FILES_DIR = "output"
data = "test"


def process_html_files(file1_path, file2_path):
    # Your existing code here
    # Return the result instead of printing it

    Company_report = csv_to_dict_list(html2csvTHEY(file1_path))
    My_report = csv_to_dict_list(html2csvUR(file2_path))
    print("company report jobs: ", len(Company_report))
    print("our report jobs: ", len(My_report))

    ####duplice checking
    duplicate_keys1 = has_duplicate_keys(My_report)
    duplicate_keys2 = has_duplicate_keys(Company_report)

    # Compare the reports

    compare.compare_reports(My_report, Company_report)

    zipcode_mistake(My_report, Company_report)

    rate_mistake = total_rate_mistake(My_report, Company_report)

    parts_mstk = parts_mistake(My_report, Company_report)

    compare.last_compare_jobs(My_report, Company_report)

    compare.addandzip_compare_jobs(My_report, Company_report)

    compare.need_verify(Company_report, My_report)

    compare.double_check_interactive(My_report, Company_report)

    print("my jobs:", len(My_report), " THey jobs: ", len(Company_report))

    for address_to_remove in duplicate_keys1:
        for report_dict in My_report:
            if report_dict.get('address') == address_to_remove:
                # Add the dictionary to the filtered_report list if the 'address' key doesn't match the specified value
                My_report.remove(report_dict)

    for address_to_remove in duplicate_keys2:
        for report_dict in Company_report:
            if report_dict.get('address') == address_to_remove:
                # Add the dictionary to the filtered_report list if the 'address' key doesn't match the specified value
                Company_report.remove(report_dict)

    mistake_list = []
    for jobs in rate_mistake:
        if jobs not in parts_mstk:
            parts_mstk.append(jobs)
    for job in parts_mstk:
        mistake_list.append([job[0].get("address"), job[-1]])

    print("my jobs:", len(My_report), " THey jobs: ", len(Company_report))

    print("\nSummary Statistics:")
    # Convert the list of dictionaries into a list of (key, value) tuples

    save_files(My_report, Company_report, duplicate_keys1, duplicate_keys2, mistake_list)
    #table1_data = print_web("output/my_report.csv")
    #table2_data = print_web("output/company_report.csv")

    return print("compare online") #table1_data,table2_data

def get_guess_from_user(secret_number):
    #global data
    data = secret_number
    print("#########")
    print(data)
    input_url = url_for('input_page')
    return redirect(input_url)

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'GET':
        return render_template('input.html',value=data)
    if request.method == 'POST':
        user_guess = request.form.get('user_guess')
        print(user_guess)
        if user_guess not in ['r', 'k']:  # Use 'and' instead of 'or'
            raise ValueError('Only "r" (remove) or "k" (keep) allowed')
        else:
            return user_guess
    return render_template('input.html', value=data, user="ohad")

@app.route('/result')
def result():
    data1 =[]
    data2 = []
    data3 = []
    with open('output/company_report.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate through the rows in the CSV and print each row
        for row in reader:
            data1.append(row)
        #print(data1)
    with open('output/my_report.csv', 'r', newline='') as csvfile1:
        reader = csv.DictReader(csvfile1)

        # Iterate through the rows in the CSV and print each row
        for row in reader:
          data2.append(row)
        #print(data2)
    with open('output/mistakes.csv', 'r', newline='') as csvfile2:
        reader = csv.DictReader(csvfile2)

        # Iterate through the rows in the CSV and print each row
        for row in reader:
         data3.append(row)
        print(data3)

    return render_template('result.html', data1=data1, data2=data2,data3=data3)

@app.route('/', methods=['GET', 'POST'])
def home():
    global data
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1 and file2:
            file1_path = os.path.join(GENERATED_FILES_DIR, file1.filename)
            file2_path = os.path.join(GENERATED_FILES_DIR, file2.filename)

            file1.save(file1_path)
            file2.save(file2_path)

            # Use your existing code to process the files and get the CSV file content
            csv_file_content = process_html_files(file1_path, file2_path)

            # Render the generated CSV file content
            return redirect(url_for('result', csv_content=csv_file_content))

    return render_template('home.html')



# Define the URL of your Flask application and the data to post






if __name__ == '__main__':
    os.makedirs(GENERATED_FILES_DIR, exist_ok=True)
    app.run(debug=True)

# Load data from HTML and CSV files
#print("Loading data from HTML and CSV files...")





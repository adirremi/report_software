import pandas as pd

def html2csvTHEY(path):
    try:
        # Read HTML tables using pandas
        df = pd.read_html(path)

        # Check if tables were found
        if len(df) > 0:
            # Save the first table as a CSV file
            df[0].to_csv("report_csv/CSV_File_THEY.csv", index=False)
            print("CSV file 'CSV_File_THEY.csv' saved successfully.")
            return "report_csv/CSV_File_THEY.csv"
        else:
            print("No tables found in the HTML file.")
            return "No tables found in the HTML file."

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

def html2csvUR(path):
    try:
        # Read HTML tables using pandas
        df = pd.read_html(path)

        # Check if tables were found
        if len(df) > 0:
            # Save the first table as a CSV file
            df[0].to_csv("report_csv/CSV_File_OUR.csv", index=False)
            return "report_csv/CSV_File_OUR.csv"
        else:
            return "No tables found in the HTML file."

    except Exception as e:
        return f"Error: {str(e)}"



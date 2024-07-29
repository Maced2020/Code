# I created this so that i could take the XML file you get from Exporting your apple music library and turn it into a readable list.
# completed 6/29/2024


import xml.etree.ElementTree as ET
import csv

def extract_data_from_xml(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    sort_data = []

    current_data = {}
    capture_next_string = None

    for elem in root.iter():
        if elem.tag == 'key' and elem.text in ['Sort Name', 'Sort Artist']:
            capture_next_string = elem.text
        elif capture_next_string and elem.tag == 'string':
            current_data[capture_next_string] = elem.text
            capture_next_string = None
            if 'Sort Name' in current_data and 'Sort Artist' in current_data:
                sort_data.append(current_data)
                current_data = {}

    # Write the extracted data to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sort Name", "Sort Artist"])
        for data in sort_data:
            writer.writerow([data.get('Sort Name', ''), data.get('Sort Artist', '')])
        print("file written")

# Replace 'input.xml' and 'output.csv' with your file names
extract_data_from_xml('Tims_Songs.xml', 'tims_songs.csv')
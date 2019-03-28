import csv
import geopy.geocoders
from geopy.geocoders import Bing
import time

def clean_locations():
     with open('dataset/location.csv') as csvDataFile:
        with open('dataset/location_clean.csv', 'w') as csv_out:
            writer = csv.writer(csv_out, delimiter=' ',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if row and row[0].lower().startswith("off "):
                    new_row = [row[0][4:]]
                elif row and row[0].lower().startswith("near "):
                    new_row = [row[0][5:]]
                else:
                    new_row = row
                writer.writerow(new_row)

def add_coordinates():
    geolocator = Bing(api_key="AjqWLHWVCEHcB9V7sO2ubMzKO7P1eARR-Zl6SBe0RmACT5RFMer3p6q6iJxiQ2Z9",
                      timeout=3)
    # todo: add delay, api requests timing out
    with open('dataset/location_clean.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        with open('dataset/location_coordinates.csv', 'w') as csv_out:
            writer = csv.writer(csv_out, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvReader = csv.reader(csvDataFile)
            row_count = 0
            for row in csvReader:
                if row_count % 100 == 0:
                    print(f"sleepy time {row_count}") #just to check progress while it's running
                time.sleep(1)
                row_count += 1
                if row:
                    location = geolocator.geocode(query=str(row[0]))

                    if location is not None:
                        new_row = [row[0], location.latitude, location.longitude]
                    else:
                        new_row = [row[0], "", ""]
                else:
                    new_row = ["", "", ""]
                writer.writerow(new_row)

if __name__ == "__main__":
    add_coordinates()
        
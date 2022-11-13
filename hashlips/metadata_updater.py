import json
import csv
import os
import shutil

#file paths for metadata, make sure old metadata is in old_metadata folder the new folder will be created automatically
json_directory_in = 'old_metadata'
json_directory_out = 'metadata'

#file containing update list (first value is old attribute being replaced, second is attribute replacing the first)
csv_path = 'update.csv'

#lists used to store the change data
old_strings = []
new_strings = []

#index for tracking what is being replaced
a = 0

#opens, reads, and assigns update values from update.csv
with open(csv_path, 'r') as changes:
    data = csv.reader(changes, delimiter = ',')
    for row in data:
        old_strings.append(row[0])
        new_strings.append(row[1])
    print(len(old_strings)," attributes are being checked for replacement") #comment to show user that things are happening

#checks if new metadata folder is present, if not it will be created
if not os.path.exists("metadata"):
    os.makedirs("metadata")

#starts metadata file iteration
for filename in os.listdir(json_directory_in):
    f = os.path.join(json_directory_in, filename)
    if os.path.isfile(f):
        filename_json_in = os.path.splitext(filename)[0] + ".json"
        filename_json_out = os.path.splitext(filename)[0] + ".json"
        print("checking file: ", filename)    # output to user that we're making progress, can be commented out

        #opens metadata file for checking
        with open(os.path.join(json_directory_in, filename_json_in), 'r') as mfile:
            json_data = json.load(mfile)
            for d in json_data['attributes']:
                print("original value: ", d['value'])
                a = 0
                while a < len(new_strings):
                    if(d['value'].lower().strip()) == old_strings[a].lower(): #added to ensure capital letters in the old values do not break script
                        d['value'] = new_strings[a] #updates old values to new values
                        print("new value: ", new_strings[a])
                    a = a + 1

        #writes new values to file
        with open(os.path.join(json_directory_out, filename_json_out), 'w') as file:
            json.dump(json_data, file, indent=2)

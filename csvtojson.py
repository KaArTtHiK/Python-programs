import json
json_list = []
file_csv = open("csv_file.txt", "r")
for line in file_csv.readlines():
    club, city, country = line.strip().split(",")
    json1 = {
        "club": club,
        "city": city,
        "country": country
    }
    json_list.append(json1)

file_csv.close()

json_file1 = open("json_file.txt", "w")
json.dump(json_list, json_file1)
json_file1.close()

#with open("json_file.txt", "w") as json_file1:
#    json.dump(json_list, json_file1)     we can also do it in this for opening the file and read or write in it.

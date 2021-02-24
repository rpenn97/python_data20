# import csv

#
# with open('example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#
#     dates = []
#     colours = []
#
#     for row in readCSV:
#         colour = row[3]
#         date = row[0]
#         dates.append(date)
#         colours.append(colour)
# print(dates)
# print(colours)
# print(row)
# print(row[0])
# print(row[0],row[1])
#
# whatColour = input("What colour do you wish to know the date of?")
# coldex = colours.index(whatColour)
# theDate = dates[coldex]
# print("The date of",whatColour,"is",theDate)

#My Simple Solution:

# import csv
#
# readcsv = csv.reader(open('user_details.csv','r'))
# outputcsv = open('name_and_email.csv','w')
# for column in readcsv:
#     new_details = (column[1].replace(',',','),column[2].replace(',',','),column[4].replace(',',','))
#     print(new_details)
#     outputcsv.write(str(new_details))

#Class Solution with Functions:

import csv

def transform_user_details(csv_file_name):
    new_user_data = []
    with open(csv_file_name) as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        #To skip the first line:
        # iterable_csv=iter(user_details_csv)
        # next(iterable_csv)

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[4])
            new_user_data.append(transformation)

    return new_user_data

print(transform_user_details("user_details.csv"))

def create_new_details(old_user_data_file="user_details.csv", new_file_name="new_user_details.csv"):
    new_user_data = transform_user_details(old_user_data_file)

    with open(new_file_name, "w") as new_file:
        csv_writer=csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_details()

# Adam's solution (list of lists):

# def opening_csv_files(filename):
#     with open(filename) as csvfile:
#         readcsv = csv.reader(csvfile,delimiter=',')
#         return list(readcsv)
#
# def transforming(csvfile):
#     firstname = []
#     lastname = []
#     email = []
#     for row in csvfile:
#         firstname.append(row[1])
#         lastname.append(row[2])
#         email.append(row[4])
#     return firstname,lastname,email
#
# def writingcsv(newfile,firstname,lastname,email):
#     with open(newfile,'w') as file:
#         for i in range(len(firstname)):
#             file.write(firstname[i]+","+lastname[i]+","+email[i]+"\n")
# def main(old_file_name, new_file_name):
#     a = opening_csv_files(old_file_name)
#     b = transforming(a)
#     writingcsv(new_file_name,b[0],b[1],b[2])



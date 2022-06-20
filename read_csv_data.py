import csv

from datetime import date, datetime


class PostalData():

    def __init__(self, row_data):
        self.id = int(row_data[0])  # ToDo error handling
        self.name = row_data[1]
        self.user_name = row_data[2]
        self.the_magic_number = int(row_data[3])
        self.expiry_date = datetime.fromisoformat(row_data[4])


    def user_is_expired(self, time_now=None):

        if time_now is None:
            time_now = datetime.now()

        if self.expiry_date <= time_now:
            return True
        else:
            return False


list_of_valid_users = [] # list()

with open('input_data_001.csv', newline='') as csvfile:

    my_reader = csv.reader(csvfile, delimiter=';')

    for rr in my_reader:
        pp = PostalData(rr)
        print(pp.id, pp.expiry_date, pp.user_is_expired())

        if not pp.user_is_expired():
            list_of_valid_users.append(pp)
            

for ii in list_of_valid_users:
    print(ii.id, ii.expiry_date, ii.user_is_expired())

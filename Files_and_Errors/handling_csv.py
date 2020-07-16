import csv

# scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     headers = list(map(str.lstrip, next(csvreader)))
#     for row in csvreader:
#         scores.append(int(row[-1]))
#
# print(headers)
# print(scores)
#
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader))  # List of lists

# data_to_write = [["David", 5], ["Paula", 6]]
#
# with open("new_data.csv", "w") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for row in data_to_write:
#         csv_writer.writerow(row)
#     csv_writer.writerows(data_to_write)

# def read_csv(filename):
#     try:
#         with open(filename, "r") as opened_file:
#             csv_reader = csv.reader(opened_file)
#
#     except FileNotFoundError:
#         print("File is not found. Check your spelling!")


def column_mean(filename):
    with open(filename, "r") as opened_file:
        csv_reader = list(csv.reader(opened_file))

        #headers = csv_reader[0]
        csv_reader = csv_reader[1:]
        means_of_columns = []
        for i in range(4):
            sum = 0
            for row in csv_reader:
                sum += float(row[i])
            mean = sum / (len(list(csv_reader)))
            means_of_columns.append(mean)
        return means_of_columns
# csv files act as buffers - as you go through the file the lines disappear
#print(column_mean("iris.csv"))

def column_mean_anyfile(filename):
    with open(filename, "r") as opened_file:
        csv_reader = list(csv.reader(opened_file))

        col = len(csv_reader[0])
        csv_reader_headers = csv_reader[0]
        csv_reader = csv_reader[1:]
        list_of_means = []
        list_of_headers = []
        for i in range(col):
            sum = 0
            try:
                for row in csv_reader:
                    row[i] = int(row[i])
                    sum += row[i]
                mean = sum / len(list(csv_reader))
                list_of_means.append(mean)
                list_of_headers.append(csv_reader_headers[i])
            except ValueError:
                print("This columns does not have arithmetic elements. Skip!")

        return f"{list_of_headers}\n{list_of_means}"

print(column_mean_anyfile("some_data.csv"))

class Iris:
    def __init__(self, filename):
        raw_data = self.load_data(filename) 
        self.header = raw_data[0]
        self.data = raw_data[1:]
        
    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)

    def find_mean(self, list_of_values):
        return column_mean()

iris = Iris("iris.csv")

iris.find_mean()




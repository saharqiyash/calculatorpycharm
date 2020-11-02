def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolute_path(filepath), "r") as f:
            csv_data = csv.DictReader(f, delimiter=',')
            for row in csv_data:
                self.data.append(row)


    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
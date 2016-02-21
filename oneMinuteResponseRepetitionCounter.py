import csv
import enchant
import collections
from collections import Counter
from collections import defaultdict
import operator
from collections import OrderedDict

class CounterClass:
    def __init__(self):
        self.single_word_count = 0
        self.double_word_count = 0
        self.double_double_word_count = 0
        self.triple_double_word_count = 0
        self.quadruple_double_word_count = 0
        self.quintuple_double_word_count = 0
        self.triple_word_count = 0
        self.quadruple_word_count = 0
        self.quintuple_word_count = 0
        self.sextuple_word_count = 0
        self.septuple_word_count = 0
        self.octuple_word_count = 0
        self.other = 0
        self.list_count = 0

    def count_repeat_words(self, sorted_string):
        repeat_list = []
        sorted_list = sorted_string.split("||")

        for each_word in sorted_list:
            if each_word == '':
                sorted_list.remove('')

        d = defaultdict(int)
        for each_word in sorted_list:
            d[each_word] += 1

        ds = collections.OrderedDict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

        items = list(ds.items())
        for key, value in items:
            self.list_count += 1

            if items[0][1] >= 8:
                self.octuple_word_count += 1
                repeat_list.append(key)
                return
            if items[0][1] == 7:
                self.septuple_word_count +=1
                repeat_list.append(key)
                return
            if items[0][1] == 6:
                self.sextuple_word_count +=1
                return
            if items[0][1] == 5:
                self.quintuple_word_count +=1
                return
            if items[0][1] == 4:
                self.quadruple_word_count += 1
                return
            if items[0][1] == 3:
                self.triple_word_count +=1
                return
            if items[0][1] == 2:
                self.double_word_count += 1
                if len(items) >= 2 and items[1][1] == 2:
                    self.double_double_word_count +=1
                    print(items)
                    if len(items) >= 3 and items[2][1] == 2:
                        self.triple_double_word_count +=1
                        if len(items) >= 4 and items[3][1] == 2:
                            self.quadruple_double_word_count += 1
                            if len(items) >= 5 and items[4][1] == 2:
                                self.quintuple_double_word_count += 1
                            return
                        return
                    return
                return
            if items[0][1] ==1:
                self.single_word_count +=1
                return



        repeat_string = ("||".join(repeat_list))
        return repeat_string

    def main(self):
        input_file = open("OutputData/One_Minute_Responses_Sorted.csv", "r")
        one_minute_data_sorted = csv.reader(input_file)

        output_file = open("OutputData/One_Minute_Responses_repeat_counter.csv", "w")
        one_minute_data_repeat_count = csv.writer(output_file)

        data_rows = []
        row_index = 0

        for each_row in one_minute_data_sorted:
            if row_index == 0 or row_index == 1:
                one_minute_data_repeat_count.writerow(each_row)
                row_index += 1
                continue

            cell_index = 0
            while cell_index < len(each_row):
                if cell_index == 21:
                    each_row[cell_index] = self.count_repeat_words(each_row[cell_index])
                    cell_index += 3
                elif cell_index >= 24:
                    each_row[cell_index] = self.count_repeat_words(each_row[cell_index])
                    cell_index += 2
                else:
                    cell_index += 1

            data_rows.append(each_row)

        for each_data_row in data_rows:
            one_minute_data_repeat_count.writerow(each_data_row)

        input_file.close()
        output_file.close()

        print("single word count: ", self.single_word_count)
        print("double word count: ", self.double_word_count)
        print("double double word count: ", self.double_double_word_count)
        print("triple double word count: ", self.triple_double_word_count)
        print("quadruple double word count: ", self.quadruple_double_word_count)
        print("quintuple double word count: ", self. quintuple_double_word_count)
        print("triple word count: ", self.triple_word_count)
        print("quadruple word count: ", self.quadruple_word_count)
        print("quintuple word count: ", self.quintuple_word_count)
        print("sextuple word count: ", self.sextuple_word_count)
        print("septuple word count: ", self.septuple_word_count)
        print("8 or more times word count: ", self.octuple_word_count)
        print("other count: ", self.other)
        print("total number of lists: ", self.list_count)
if __name__ == "__main__":
    CounterClass().main()
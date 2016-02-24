import sys

def readinparameter():
    prompt = '> '


    print 'Which group/language do you want? (case-sensitive)\n\t'
    group = raw_input(prompt)

    # print 'How many people do you want from that ?\n\t'
    # num = raw_input(prompt)
    print 'Do you want people who finished or not finished?\n\tOptions: "finished", "not finished", "both"'
    isfinished = raw_input(prompt)

    while isfinished not in ["finished", "not finished", "both"]:
        print '\nInvalid input!\n'
        print 'Do you want people who finished or not finished?\n\tOptions: "finished", "not finished", "both"'
        isfinished = raw_input(prompt)
    

    print 'Which VAC do you want? (case-sensitive)\n\t'
    vac = raw_input(prompt)

    

    # while group not in ["distance", "time", "both"]:
    #     print '\nInvalid matrix type!\n'
    #     print 'Which matrix do you want?\n\tOptions: "distance", "time", "both"'
    #     mode = raw_input(prompt)

    print 'Which matrix do you want?\n\tOptions: "distance", "time", "both"'
    mode = raw_input(prompt)

    while mode not in ["distance", "time", "both"]:
        print '\nInvalid matrix type!\n'
        print 'Which matrix do you want?\n\tOptions: "distance", "time", "both"'
        mode = raw_input(prompt)
    
    return group, mode, vac, isfinished
    

def main():
    group, mode, vac, isfinished = readinparameter()
    
    # print group, mode, vac, isfinished


    infile = open('OutputData/One_Minute_Responses_Network_Data.tsv', 'r')
    outfile1 = open('OutputData/distance_matrix.tsv', 'w')
    outfile2 = open('OutputData/time_matrix.tsv', 'w')

    line_num = 0

    subject = 0
    distances = []
    time_distances = []
    words = []
    for line in infile:
        line_num += 1

        row = line.split(" ")
        row[16] = row[16].strip()

        if isfinished == 'finished':
            if subject == 0:
                if row[2] == '0' or row[1] != group or row[16] != vac:
                    continue
                else:
                    subject = row[0]
                    words.append(row[9])
                    words.append(row[10])
                    distances.append(int(row[12]) - int(row[11]))
                    time_distances.append(row[15])

            else:
                if row[0] != subject or row[16] != vac:
                    break
                else:
                    distance = int(row[12]) - int(row[11])
                    distances.append(distance)
                    time_distances.append(row[15])
                    if int(row[11]) == 1:
                        words.append(row[10])


        elif isfinished == 'not finished':
            if subject == 0:
                if row[2] == '1' or row[1] != group or row[16] != vac:
                    continue
                else:
                    subject = row[0]
                    words.append(row[9])
                    words.append(row[10])
                    distances.append(int(row[12]) - int(row[11]))
                    time_distances.append(row[15])

            else:
                if row[0] != subject or row[16] != vac:
                    break
                else:
                    distance = int(row[12]) - int(row[11])
                    distances.append(distance)
                    time_distances.append(row[15])
                    if int(row[11]) == 1:
                        words.append(row[10])

        else:
            if subject == 0:
                if row[1] != group or row[16] != vac:
                    continue
                else:
                    subject = row[0]
                    words.append(row[9])
                    words.append(row[10])
                    distances.append(int(row[12]) - int(row[11]))
                    time_distances.append(row[15])

            else:
                if row[0] != subject or row[16] != vac:
                    break
                else:
                    distance = int(row[12]) - int(row[11])
                    distances.append(distance)
                    time_distances.append(row[15])
                    if int(row[11]) == 1:
                        words.append(row[10])




    print words
    # print distances
    # print time_distances
    print "The subject of the person is {}".format(subject)
    print "The last line of the vac is at line {} in the file".format(line_num)


    # output distance matrix data
    matrix = []
    for dis in distances:
        if dis == 1:
            matrix.append(['0', '1'])
        else:
            matrix[len(matrix)-1].append(str(dis))
    matrix.append(['0'])

    # print matrix


    # output time matrix data
    time_matrix = []
    start = 0
    for row_num in range(len(words)):
        
        time_matrix.append(['0'])
        for i in range(start, start + len(words) - row_num - 1):
            time_matrix[len(time_matrix)-1].append(time_distances[i])
        start = start + len(words) - row_num - 1

    time_matrix.append(['0'])

    # print time_matrix



    # output data to files

    outfile1.write("\t".join(words) + "\n")
    outfile2.write("\t".join(words) + "\n")

    for i in range(len(matrix)):
        lower_tri = []
        for j in range(i):
            lower_tri.append('0')
        if i > 0:
            outfile1.write("\t".join(lower_tri) + "\t" + "\t".join(matrix[i]) + "\n")
            outfile2.write("\t".join(lower_tri) + "\t" + "\t".join(time_matrix[i]) + "\n")
        else:
            outfile1.write("\t".join(matrix[i]) + "\n")
            outfile2.write("\t".join(time_matrix[i]) + "\n")

    infile.close()
    outfile1.close()
    outfile2.close()



if __name__ == "__main__":
    main()
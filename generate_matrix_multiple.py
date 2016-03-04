import sys

def findindex(mylist, myitem):
    for i in range(len(mylist)):
        if mylist[i] == myitem:
            return i
    return -1

def readinparameter():
    prompt = '> '

    print ('Which group/language do you want? (case-sensitive)\n\t')
    group = input(prompt)

    print ('Do you want people who finished or not finished?\n\tOptions: "finished", "not_finished", "both"')
    isfinished = input(prompt)

    while isfinished not in ["finished", "not_finished", "both"]:
        print ('\nInvalid input!\n')
        print ('Do you want people who finished or not finished?\n\tOptions: "finished", "not_finished", "both"')
        isfinished = input(prompt)
    

    print ('Which VAC do you want? (case-sensitive)\n\t')
    vac = input(prompt)


    # print 'Which matrix do you want?\n\tOptions: "distance", "time", "both"'
    # mode = input(prompt)

    # while mode not in ["distance", "time", "both"]:
    #     print '\nInvalid matrix type!\n'
    #     print 'Which matrix do you want?\n\tOptions: "distance", "time", "both"'
    #     mode = input(prompt)
    
    return group, vac, isfinished

def matrixOfOnePerson(line, infile):
    # line_num = 0

    distances = []
    time_distances = []
    words = []

    row = line.split(" ")
    row[16] = row[16].strip()
    subject_curr = row[0]
    group_curr = row[1]
    vac_curr = row[16]
    word1 = row[9]
    word2 = row[10]
    dis1 = row[11]
    dis2 = row[12]
    time_dis = row[15]

    subject = subject_curr
    vac = vac_curr

    words.append(word1)
    words.append(word2)
    
    distances.append(int(dis2) - int(dis1))
    time_distances.append(time_dis)

    for line in infile:
        # line_num += 1

        row = line.split(" ")
        row[16] = row[16].strip()
        subject_curr = row[0]
        group_curr = row[1]
        vac_curr = row[16]
        word1 = row[9]
        word2 = row[10]
        dis1 = row[11]
        dis2 = row[12]
        time_dis = row[15]
        
        if subject_curr == subject and vac_curr == vac:
            distance = int(dis2) - int(dis1)
            distances.append(distance)
            time_distances.append(time_dis)
            if int(dis1) == 1:
                words.append(word2)
        else:
            break

    matrix = []

    for dis in distances:

        if dis == 1:
            matrix.append(['0', '1'])

        else:
            matrix[-1].append(str(1.0/dis))

    matrix.append(['0'])


    time_matrix = []
    start = 0
    for row_num in range(len(words)):
        
        time_matrix.append(['0'])
        for i in range(start, start + len(words) - row_num - 1):
            time_matrix[-1].append(str(1.0/int(time_distances[i])))
        
        start = start + len(words) - row_num - 1

    # time_matrix.append(['0'])

    return words, matrix, time_matrix, line


def combineMatricesHelper(matrix_total, matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            matrix_total[i][i + j].append(matrix[i][j])
        for j in range(i):
            matrix_total[i][j].append("0")



def combineMatrices(dis_matrix_total, time_matrix_total, words_total, matrix, time_matrix, words):
    # if the words_total is still empty, treat differently
    if not words_total:
        for word in words:
            words_total.append(word)

        for i in range(len(words)):
            dis_matrix_total.append([])
            time_matrix_total.append([])
            for j in range(len(words)):
                dis_matrix_total[-1].append([])
                time_matrix_total[-1].append([])

        combineMatricesHelper(dis_matrix_total, matrix)
        combineMatricesHelper(time_matrix_total, time_matrix)
        return
    # end of the speical case


    for word in words:
        if word not in words_total:
            words_total.append(word)

            for i in range(len(dis_matrix_total)):
                dis_matrix_total[i].append([])
                time_matrix_total[i].append([])

                for j in range(len(dis_matrix_total[0][1])):
                    dis_matrix_total[i][-1].append("0")
                    time_matrix_total[i][-1].append("0")
            
            dis_matrix_total.append([])
            time_matrix_total.append([])
            
            for i in range(len(words_total)-1):
                dis_matrix_total[-1].append([])
                time_matrix_total[-1].append([])

                for j in range(len(dis_matrix_total[0][1])):
                    dis_matrix_total[-1][-1].append("0")
                    time_matrix_total[-1][-1].append("0")
            
            dis_matrix_total[-1].append(["0"])
            time_matrix_total[-1].append(["0"])


    
    # append 0 for each cell in the matrix at first
    for i in range(len(words_total)):
        for j in range(len(words_total)):
            if i == j:
                continue
            else:
                dis_matrix_total[i][j].append("0")
                time_matrix_total[i][j].append("0")


    # replace the 0 at the tail of each cell with actual value
    for i in range(len(words)):
        word1 = words[i]
        
        for j in range(i+1, len(words)):
            word2 = words[j]
            
            if word1 == word2:
                continue

            idx1 = findindex(words_total, word1)
            idx2 = findindex(words_total, word2)

            dis_matrix_total[idx1][idx2].pop()
            dis_matrix_total[idx1][idx2].append(matrix[i][j-i-1])

            time_matrix_total[idx1][idx2].pop()
            time_matrix_total[idx1][idx2].append(time_matrix[i][j-i-1])


def main():
    group, vac, isfinished = readinparameter()
    
    # print group, mode, vac, isfinished

    infile = open('OutputData/One_Minute_Responses_Network_Data.tsv', 'r')
    for line in infile:
        pass
    lastLine = line
    infile.close()


    infile = open('OutputData/One_Minute_Responses_Network_Data.tsv', 'r')
    outfile1 = open('OutputData/matrixData/' + group + '_'+ isfinished +'_' + vac + '_distance_matrix.tsv', 'w')
    outfile2 = open('OutputData/matrixData/' + group + '_'+ isfinished +'_' + vac + '_time_matrix.tsv', 'w')
    outfile3 = open('OutputData/matrixData/' + group + '_'+ isfinished +'_' + vac + '_distance_matrix_sum.tsv', 'w')
    outfile4 = open('OutputData/matrixData/' + group + '_'+ isfinished +'_' + vac + '_time_matrix_sum.tsv', 'w')

    time_matrix_total = []
    dis_matrix_total = []
    words_total = []


    count = 0
    for line in infile:
        count+=1
        
        row = line.split(" ")
        row[16] = row[16].strip()
        subject_curr = row[0]
        group_curr = row[1]
        vac_curr = row[16]
        finished_or_not = row[2]

        if isfinished == 'finished':
            if finished_or_not == '1' or group_curr != group or vac_curr != vac:
                continue
            else:
                words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)


                while True:
                    if line == lastLine:
                        break
                    row = line.split(" ")
                    row[16] = row[16].strip()
                    subject_curr = row[0]
                    group_curr = row[1]
                    vac_curr = row[16]
                    finished_or_not = row[2]
                    if finished_or_not == '1' or group_curr != group or vac_curr != vac:
                        break
                    else:
                        words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)


        elif isfinished == 'not_finished':
            if finished_or_not == '0' or group_curr != group or vac_curr != vac:
                continue
            else:
                words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)

                while True:
                    if line == lastLine:
                        break
                    row = line.split(" ")
                    row[16] = row[16].strip()
                    subject_curr = row[0]
                    group_curr = row[1]
                    vac_curr = row[16]
                    finished_or_not = row[2]
                    if finished_or_not == '0' or group_curr != group or vac_curr != vac:
                        break
                    else:
                        words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)


        else:
            if group_curr != group or vac_curr != vac:
                continue
            else:
                words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)

                while True:
                    if line == lastLine:
                        break
                    row = line.split(" ")
                    row[16] = row[16].strip()
                    subject_curr = row[0]
                    group_curr = row[1]
                    vac_curr = row[16]
                    finished_or_not = row[2]
                    if group_curr != group or vac_curr != vac:
                        break
                    else:
                        words, dis_matrix, time_matrix, line = matrixOfOnePerson(line, infile)


        combineMatrices(dis_matrix_total, time_matrix_total, words_total, \
            dis_matrix, time_matrix, words)
        
        # if count == 10000:
        #     break

    # remove error words

    error_idx = []
    for i in range(len(words_total)):
        if words_total[i][:5] == 'error':
            idx = i - len(error_idx)
            error_idx.append(idx)

    for idx in error_idx:
        words_total.pop(idx)

        dis_matrix_total.pop(idx)
        for row in dis_matrix_total:
            row.pop(idx)

        time_matrix_total.pop(idx)
        for row in time_matrix_total:
            row.pop(idx)



    # calculate sum
    dis_matrix_sum = []
    time_matrix_sum = []
    for i in range(len(words_total)):
        dis_matrix_sum.append([])
        time_matrix_sum.append([])
        for j in range(len(words_total)):
            sum1 = 0
            
            for number in dis_matrix_total[i][j]:
                sum1 += float(number)

            dis_matrix_sum[-1].append(str(sum1))
            

            sum1 = 0
            for number in time_matrix_total[i][j]:
                sum1 += float(number)

            time_matrix_sum[-1].append(str(sum1))
    

    # output data to files

    outfile1.write("" + "\t" + "\t".join(words_total) + "\n")
    outfile2.write("" + "\t" + "\t".join(words_total) + "\n")
    outfile3.write("" + "\t" + "\t".join(words_total) + "\n")
    outfile4.write("" + "\t" + "\t".join(words_total) + "\n")

    mylen = len(dis_matrix_total[0][1])
    for i in range(len(words_total)):
        for j in range(len(words_total)):

            # if the lengths of each cell are different, exit and print out error
            if i != j and len(dis_matrix_total[i][j]) != mylen:

                print ("diff length")
                print ("expected length: " + str(mylen))
                print ("obtained length: " + str(len(dis_matrix_total[i][j])))
                print ("position: " + str(i) + " "+str(j))
                print (dis_matrix_total[i][j])
                print ("Error: Different length of each cell")
                sys.exit(0)
            dis_matrix_total[i][j] = "[" + ", ".join(dis_matrix_total[i][j]) + "]"
            time_matrix_total[i][j] = "[" + ", ".join(time_matrix_total[i][j]) + "]"
            if dis_matrix_total[i][j] == "[]":
                dis_matrix_total[i][j] = "[0]"
            if time_matrix_total[i][j] == "[]":
                time_matrix_total[i][j] = "[0]"
        
        outfile1.write(words_total[i] + "\t" + "\t".join(dis_matrix_total[i]) + "\n")
        outfile2.write(words_total[i] + "\t" + "\t".join(time_matrix_total[i]) + "\n")
        outfile3.write(words_total[i] + "\t" + "\t".join(dis_matrix_sum[i]) + "\n")
        outfile4.write(words_total[i] + "\t" + "\t".join(time_matrix_sum[i]) + "\n")




    infile.close()
    outfile1.close()
    outfile2.close()
    outfile3.close()
    outfile4.close()


if __name__ == "__main__":
    main()
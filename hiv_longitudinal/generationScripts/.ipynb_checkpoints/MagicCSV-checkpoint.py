import os
import random
import csv
import itertools
from tempfile import NamedTemporaryFile
import shutil


# Used to generate frequency CSVs based on reference-based comparisons!!
# Used same reference for all studies -- may want to split by study for git file cap

def generate_frequencies(divisions, mod, patientmax):
    # -- = insert study reference
    study = "2031"
    referenceGenome = open('../AlignedSequences/1142_21423_13_10_1986_A_1986_0__None.txt', 'r')

    path = '../AlignedSequences/'
    

    # convert genome to single string
    referenceSequence = ""
    with referenceGenome as reference_file:
        for line in reference_file.readlines():
            referenceSequence += line.split("\n")[0]
    for iterations in range(0,divisions):
        print(divisions)
        print(iterations)
        outputFile = open("MutationDivision"+str(iterations+1)+"."+str(divisions)+".csv", "w")
        foundContexts = []

        firstPatient = True
        for (dirpath, dirnames, filenames) in os.walk(path):
            patientnum = 0
            mutations = {}
            mutations["T>A"] = {}
            mutations["T>C"] = {}
            mutations["T>G"] = {}
            mutations["C>A"] = {}
            mutations["C>T"] = {}
            mutations["C>G"] = {}
            for filename in filenames:
                if str(filename).endswith(".txt"): #and str(filename).startswith(study):
                    with open(path + filename, 'r') as test_file:
                        print("opening file", filename)
                            #if patientnum >= 40:
                            #return This is a limitation to the number of

                        
                        
                        
                        
                        if patientnum%mod==0:
                            populateContexts(mutations)

                        testSequence = ""
                        for line in test_file.readlines():
                            testSequence += line.split("\n")[0]
                        substr=testSequence[len(testSequence)*iterations/divisions:len(testSequence)*iterations/divisions+len(testSequence)/divisions]
                        startIndex = len(testSequence)*iterations/divisions
                        endIndex = len(testSequence)*(iterations+1)/divisions
                        if "-" in substr:
                            continue
                        patientnum += 1
                        if patientnum>=patientmax:
                            continue
                        for i in range(startIndex, endIndex):
                                # find mutations in line
                                if testSequence[i] != referenceSequence[i]:# and testSequence[i] != "-" and referenceSequence[i] != "-":
                                    test = randpicker(testSequence[i])
                                    ref = randpicker(referenceSequence[i])
                                    if test == "n" or ref == "n" or test == ref or not mutations.keys().__contains__(ref.upper() + ">" + test.upper()):
                                        continue
                                    # get context of test
                                    # print("Mutation at nucleotide " + str(i) + " between: " + ref + " and: " + test)
                                    context = ""
                                    if i - 1 < 0:
                                        context = "-" + ref + referenceSequence[i+1]
                                        # print("Found a starting mutation!")
                                    if i + 1 >= len(referenceSequence):
                                        context = referenceSequence[i-1] + ref + "-"
                                        # print("Found an ending mutation!")
                                    else:
                                        context = referenceSequence[i-1] + ref + referenceSequence[i+1]
                                    # print("Context " + context.upper() + "of mutation at i = " + str(i))
                                    mut = ref + ">" + test
                                    mut = mut.upper()
                                    context = context.upper()
                                    if not mutations[mut].__contains__(context):
                                        continue
                                    else:
                                        mutations[mut][context] = mutations[mut][context] + 1
        
                    #print("Mutations for file" + filename + " : " + str(mutations))
                    if (patientnum+1)%mod==0:
                        if firstPatient is True:
                            with open("MutationDivision"+str(iterations+1)+"."+str(divisions)+".csv", "w") as f:
                                w = csv.writer(f)
                                w.writerow(["Mutation Type"] + ["Trinucleotide"] + ["Sample" + str(patientnum)])
                                for key in sorted(mutations.keys()):
                                    for context in mutations[key].keys():
                                        w.writerow([key] + [context] + [mutations[key][context]])
                                        foundContexts.append([key, context])
                            firstPatient = False
                        else:  # move on to new column for next patient
                            filename = "MutationDivision"+str(iterations+1)+"."+str(divisions)+".csv"
                            #print("Looking at patient number " + str(patientnum))
                            # now populate data
                            with open(filename) as csvFile:
                                with open("dummyfile.csv", "w") as tempfile:
                                    # the following executes for every extracted mutation-context frequency
                                    # found from this patient
                                    csv_reader = csv.reader(csvFile, delimiter=',')
                                    csv_writer = csv.writer(tempfile)
                                    line_count = 0
                                    # Go over already found contexts
                                    for row in csv_reader:
                                        line_count += 1
                                        if line_count == 1:
                                            csv_writer.writerow(row + ["Sample" + str(patientnum)])
                                            continue
                                        if mutations[row[0]].__contains__(row[1]):
                                            csv_writer.writerow(row + [mutations[row[0]][row[1]]])
                                            foundContexts.append([row[0], row[1]])
                                        else:
                                            csv_writer.writerow(row + [0])

                                    for key in sorted(mutations.keys()):
                                        for context in mutations[key].keys():
                                            if not foundContexts.__contains__([key, context]):
                                                row = [key] + [context]
                                                for i in range(patientnum - 1):
                                                    row += [0]
                                                csv_writer.writerow(row + [mutations[key][context]])
                            shutil.move(tempfile.name, filename)

def randpicker(letter):
    randnum = random.randint(0, 12)
    if letter == "u":
        return "t"
    if letter == "t":
        return "t"
    if letter == "a":
        return "a"
    if letter == "g":
        return "g"
    if letter == "c":
        return "c"
    if letter == "n":
        return "n"
    if letter == "r":
        if randnum > 6:
            return "a"
        else:
            return "g"
    if letter == "y":
        if randnum > 6:
            return "c"
        else:
            return "t"
    if letter == "s":
        if randnum > 6:
            return "g"
        else:
            return "c"
    if letter == "w":
        if randnum > 6:
            return "a"
        else:
            return "t"
    if letter == "k":
        if randnum > 6:
            return "g"
        else:
            return "t"
    if letter == "m":
        if randnum > 6:
            return "a"
        else:
            return "c"
    if letter == "b":
        if randnum > 4:
            return "c"
        if randnum > 8:
            return "g"
        else:
            return "t"
    if letter == "d":
        if randnum > 4:
            return "a"
        if randnum > 8:
            return "g"
        else:
            return "t"
    if letter == "h":
        if randnum > 4:
            return "a"
        if randnum > 8:
            return "c"
        else:
            return "t"
    if letter == "v":
        if randnum > 4:
            return "a"
        if randnum > 8:
            return "c"
        else:
            return "g"

    else:
        return "illegal value exception"

def populateContexts(mutations):
    left = "A"
    right = "A"
    for key in mutations.keys():
        for i in range(4):
            if i % 4 == 0:
                left = "A"
            if i % 4 == 1:
                left = "C"
            if i % 4 == 2:
                left = "G"
            if i % 4 == 3:
                left = "T"
            for j in range(4):
                if j % 4 == 0:
                    right = "A"
                if j % 4 == 1:
                    right = "C"
                if j % 4 == 2:
                    right = "G"
                if j % 4 == 3:
                    right = "T"
                context = left + key[0] + right
                mutations[key][context] = 0

generate_frequencies(7,10,20)
# To do

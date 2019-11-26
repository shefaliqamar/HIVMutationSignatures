import os
import random
import csv
import itertools


# Used to generate frequency CSVs based on reference-based comparisons!

def generate_frequencies():
    # -- = insert study reference
    study = "968"
    referenceGenome = open('/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/AlignedSequences/1142_21423_13_10_1986_A_1986_0__None.txt', 'r')

    mutations = {}
    mutations["ag"] = {}
    mutations["ac"] = {}
    mutations["at"] = {}
    mutations["ta"] = {}
    mutations["tc"] = {}
    mutations["tg"] = {}
    mutations["ca"] = {}
    mutations["ct"] = {}
    mutations["cg"] = {}
    mutations["ga"] = {}
    mutations["gc"] = {}
    mutations["gt"] = {}

    path = '/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/AlignedSequences/'

    # convert genome to single string
    referenceSequence = ""
    with referenceGenome as reference_file:
        for line in reference_file.readlines():
            referenceSequence += line.split("\n")[0]

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if str(filename).endswith(".txt"):
                with open(path + filename, 'r') as test_file:
                    print("opening file", filename)
                    testSequence = ""
                    for line in test_file.readlines():
                        testSequence += line.split("\n")[0]
                    for i in range(len(testSequence)):
                            # find mutations in line
                            if testSequence[i] != referenceSequence[i] and testSequence[i] != "-" and referenceSequence[i] != "-":
                                test = randpicker(testSequence[i])
                                ref = randpicker(referenceSequence[i])
                                if test == "n" or ref == "n" or test == ref:
                                    continue
                                # get context of test
                                print("Mutation at nucleotide " + str(i) + " between: " + ref + " and: " + test)
                                context = ""
                                if i - 1 < 0:
                                    context = "-" + test + testSequence[i+1]
                                    print("Found a starting mutation!")
                                if i + 1 >= len(testSequence):
                                    context = testSequence[i-1] + test + "-"
                                    print("Found an ending mutation!")
                                else:
                                    context = testSequence[i-1] + test + testSequence[i+1]
                                print("Context " + context + "of mutation at i = " + str(i))
                                mut = ref + test
                                if not mutations.__contains__(mut):
                                    mutations[mut] = {}
                                if not mutations[mut].__contains__(context):
                                    mutations[mut][context] = 1
                                else:
                                    mutations[mut][context] = mutations[mut][context] + 1
                print("Mutations for file" + filename + " : " + str(mutations))
                with open(filename + "Frequencies.csv", "w") as f:
                    w = csv.writer(f)
                    for key in mutations.keys():
                        for context in mutations[key].keys():
                            w.writerow([key] + [context] + [mutations[key][context]])


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



generate_frequencies()
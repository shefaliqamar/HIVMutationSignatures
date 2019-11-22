import os

# -- = insert study reference
study = "968"
referenceGenome = open('/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/AlignedSequences/2031_101861_53ZA.0_C_2006_0__None.txt', 'r')

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

for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if str(filename).startswith(study):
            # compare
            with open(path + filename, 'r') as test_file:
                with referenceGenome as reference_file:
                    testlines = test_file.readlines()
                    referencelines = reference_file.readlines()
                    for i in range(len(testlines)):
                        testline = testlines[i]
                        refline = referencelines[i]
                        # find mutations in line
                        for j in range(len(testline)):
                            test = testline[j]
                            ref = refline[j]
                            if test != ref and test != "-" and ref != "-":
                                # get context of test
                                print("Mutation at line " + str(i) + " between: " + ref + " and: " + test)
                                startIndex = 0
                                if j - 1 < 0:
                                    startIndex = 0
                                else:
                                    startIndex = j - 1
                                endIndex = 0
                                if j + 1 > len(testline):
                                    endIndex = len(testline)
                                else:
                                    endIndex = j + 1
                                context = testline[startIndex:endIndex+1]
                                mut = ref + test
                                if not mutations[mut].__contains__(context):
                                    mutations[mut][context] = 1
                                else:
                                    mutations[mut][context] = mutations[mut][context] + 1
                                print(mutations)






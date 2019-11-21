import os

# print("Hi")
# Aligned data: all_time0_linsi.fasta

# Split by time

# were already in directory: HIVSigs.py		all_time0_linsi.fasta


outputfile = open('out.txt', 'w')
# for file in os.listdir("/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/nucleotide"):
#     with open('/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/nucleotide/' + file, 'r') as content_file:
#         content = content_file.read()
#         # outputfile.write(content + "\n\n\n")

with open('/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/AlignedSequences/all_time0_linsi.fasta', 'r') as content_file:
    for line in content_file.readlines():
        if line.__contains__(">") is True:
            # New genome here
            arr = line.split(">")
            filename = arr[1].split("\n")[0]
            # outputfile.write("Filename\t" + filename + "\n")
            outputfile = open(filename + '.txt', 'w')
        else:
            outputfile.write(line)


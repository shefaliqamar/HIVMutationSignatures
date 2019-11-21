import os

# print("Hi")
# Aligned data: all_time0_linsi.fasta

# Split by study

outputfile = open('out.txt', 'w')
for file in os.listdir("/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/nucleotide"):
    with open('/Users/macbook/Desktop/Proj6/HIVMutationSignatures/hiv_longitudinal/nucleotide/' + file, 'r') as content_file:
        content = content_file.read()
        outputfile.write(content + "\n\n\n")


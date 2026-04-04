import random

# create GTF with 100 genes
with open("big.gtf", "w") as gtf:
    start = 1000
    for i in range(1, 101):
        end = start + random.randint(500, 1500)
        gtf.write(f"chr1 source gene {start} {end} . + . gene_id \"Gene{i}\";\n")
        start = end + random.randint(100, 500)

# create SAM with many reads
with open("big.sam", "w") as sam:
    sam.write("@SQ SN:chr1 LN:1000000\n")

    for i in range(1, 5000):
        pos = random.randint(1000, 150000)
        sam.write(f"read{i} 0 chr1 {pos} 255 50M * 0 0 ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC *\n")

print("Generated big.sam and big.gtf")
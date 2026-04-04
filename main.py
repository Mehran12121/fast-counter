import sys
from parser import parse_gtf, parse_sam
from counter import count_reads

# check arguments
if len(sys.argv) != 4:
    print("Usage: python main.py <input.sam> <genes.gtf> <output.txt>")
    sys.exit(1)

sam_file = sys.argv[1]
gtf_file = sys.argv[2]
output_file = sys.argv[3]

# process
genes = parse_gtf(gtf_file)
reads = parse_sam(sam_file)
counts = count_reads(reads, genes)

# write output
with open(output_file, "w") as f:
    f.write("gene_id\tcount\n")
    for gene_id, count in counts.items():
        f.write(f"{gene_id}\t{count}\n")

print(f"Output written to {output_file}")
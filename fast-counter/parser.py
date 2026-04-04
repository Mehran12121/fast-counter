def parse_gtf(gtf_file):
    genes = {}

    with open(gtf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            parts = line.strip().split()

            if len(parts) < 9:
                continue

            chrom = parts[0]
            feature_type = parts[2]

            # robust check for gene feature
            if "gene" not in feature_type.lower():
                continue

            start = int(parts[3])
            end = int(parts[4])
            attributes = parts[8]

            gene_id = None
            for attr in attributes.split(';'):
                attr = attr.strip()
                if attr.startswith('gene_id'):
                    parts_attr = attr.split()
                    if len(parts_attr) >= 2:
                        gene_id = parts_attr[1].replace('"', '')
                    break

            if gene_id is None:
                continue

            if chrom not in genes:
                genes[chrom] = []

            genes[chrom].append((start, end, gene_id))

    return genes
def parse_sam(sam_file):
    reads = []

    with open(sam_file, 'r') as file:
        for line in file:
            # Skip header lines
            if line.startswith('@'):
                continue

            parts = line.strip().split()

            # SAM must have at least 4 columns
            if len(parts) < 4:
                continue

            chrom = parts[2]
            pos = int(parts[3])

            # Skip unmapped reads
            if chrom == '*':
                continue

            reads.append((chrom, pos))

    return reads
def parse_gtf(gtf_file):
    genes = {}

    with open(gtf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            parts = line.strip().split()

            if len(parts) < 5:
                continue

            chrom = parts[0]

            # check if this line represents a gene
            if "gene" not in line.lower():
                continue

            try:
                start = int(parts[3])
                end = int(parts[4])
            except:
                continue

            # extract gene_id from full line
            gene_id = None
            if 'gene_id' in line:
                try:
                    gene_id = line.split('gene_id')[1].split(';')[0].strip()
                    gene_id = gene_id.replace('"', '').replace("'", "")
                except:
                    continue

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
            if line.startswith('@'):
                continue

            parts = line.strip().split()

            if len(parts) < 4:
                continue

            chrom = parts[2]
            pos = int(parts[3])

            if chrom == '*':
                continue

            reads.append((chrom, pos))

    return reads
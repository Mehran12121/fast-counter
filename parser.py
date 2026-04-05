def parse_gtf(gtf_file):
    genes = {}

    with open(gtf_file) as file:
        for line in file:
            if line.startswith('#'):
                continue

            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue

            chrom = parts[0]
            feature = parts[2]

            if feature != "exon":
                continue

            try:
                start = int(parts[3])
                end = int(parts[4])
            except:
                continue

            attributes = parts[8]

            gene_id = None
            for attr in attributes.split(";"):
                attr = attr.strip()
                if attr.startswith("gene_id"):
                    try:
                        gene_id = attr.split('"')[1]
                    except:
                        pass
                    break

            if gene_id is None:
                continue

            if chrom not in genes:
                genes[chrom] = {}

            if gene_id not in genes[chrom]:
                genes[chrom][gene_id] = []

            genes[chrom][gene_id].append((start, end))

    # merge exons
    def merge_intervals(intervals):
        intervals.sort()
        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = curr

            if curr_start <= prev_end:
                merged[-1] = (prev_start, max(prev_end, curr_end))
            else:
                merged.append(curr)

        return merged

    for chrom in genes:
        for gene_id in genes[chrom]:
            genes[chrom][gene_id] = merge_intervals(genes[chrom][gene_id])

    return genes


def parse_sam(sam_file):
    reads = []

    with open(sam_file) as file:
        for line in file:
            if line.startswith('@'):
                continue

            parts = line.strip().split()

            if len(parts) < 6:
                continue

            chrom = parts[2]

            if chrom == '*':
                continue

            try:
                pos = int(parts[3])
            except:
                continue

            cigar = parts[5]

            if cigar == '*':
                continue

            segments = []
            current_pos = pos
            num = ""

            for char in cigar:
                if char.isdigit():
                    num += char
                else:
                    if num == "":
                        continue

                    length = int(num)

                    if char == 'M':
                        start = current_pos
                        end = current_pos + length - 1
                        segments.append((start, end))
                        current_pos += length

                    elif char == 'N':
                        # skip intron
                        current_pos += length

                    elif char in ['D', 'I', 'S', 'H']:
                        current_pos += length

                    num = ""

            if segments:
                reads.append((chrom, segments))

    return reads
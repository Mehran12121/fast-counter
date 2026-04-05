def overlaps(a_start, a_end, b_start, b_end):
    return a_start <= b_end and b_start <= a_end


def count_reads(reads, genes):
    counts = {}

    # initialize
    for chrom in genes:
        for gene_id in genes[chrom]:
            counts[gene_id] = 0

    # count
    for chrom, segments in reads:
        if chrom not in genes:
            continue

        for gene_id, exons in genes[chrom].items():
            counted = False

            for seg_start, seg_end in segments:
                for exon_start, exon_end in exons:
                    if overlaps(seg_start, seg_end, exon_start, exon_end):
                        counts[gene_id] += 1
                        counted = True
                        break

                if counted:
                    break

    return counts
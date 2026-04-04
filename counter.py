import bisect

def count_reads(reads, genes):
    counts = {}

    gene_starts = {}
    gene_data = {}

    # prepare sorted data
    for chrom in genes:
        sorted_genes = sorted(genes[chrom], key=lambda x: x[0])

        gene_starts[chrom] = [g[0] for g in sorted_genes]
        gene_data[chrom] = sorted_genes

        for _, _, gene_id in sorted_genes:
            counts[gene_id] = 0

    # binary search counting
    for chrom, pos in reads:
        if chrom not in gene_data:
            continue

        starts = gene_starts[chrom]
        genes_list = gene_data[chrom]

        # find index using binary search
        idx = bisect.bisect_right(starts, pos) - 1

        if idx >= 0:
            start, end, gene_id = genes_list[idx]

            if start <= pos <= end:
                counts[gene_id] += 1

    return counts
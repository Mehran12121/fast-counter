# 🧬 FastCounter: A Lightweight RNA-seq Read Counter

FastCounter is a Python-based tool for counting sequencing reads mapped to genes using **exon-aware and splice-aware logic**.

This project implements core ideas behind tools like featureCounts and HTSeq in a simplified, educational, and extendable way.

---

## 🔥 Features

- ✅ Exon-based read counting (introns ignored)
- ✅ Merged exon intervals per gene
- ✅ Splice-aware parsing (supports CIGAR `M` and `N`)
- ✅ Works with SAM files from STAR, HISAT2, Bowtie, Bowtie2
- ✅ Modular design (parser, counter, main)
- ✅ Simple and easy to understand

---

## 🧠 How It Works

### 1. GTF Parsing
- Extracts only `exon` features
- Groups exons by `gene_id`
- Merges overlapping exon intervals

### 2. SAM Parsing
- Reads alignment positions
- Parses CIGAR strings
- Converts reads into exon segments:
  - `50M` → single segment
  - `50M100N50M` → two exon segments (spliced read)

### 3. Read Counting
- Checks overlap between read segments and gene exons
- Counts a read **once per gene**
- Avoids double counting within the same gene

---

## 📂 Project Structure


Fast-counter/
│── main.py
│── parser.py
│── counter.py
│── test_data/
│ ├── test.gtf
│ └── test.sam
│── output.txt


---

## ▶️ Usage

Run from terminal:

```bash
python main.py test_data/test.sam test_data/test.gtf output.txt
📊 Example Output
gene_id	count
GeneA	1
GeneB	1
🧪 Example Input
GTF (exons)
chr1	test	exon	1000	1200	.	+	.	gene_id "GeneA";
chr1	test	exon	1500	1700	.	+	.	gene_id "GeneA";
SAM (spliced read)
50M100N50M
⚠️ Current Limitations
❌ No strand-specific counting
❌ No paired-end support
❌ Limited CIGAR handling (M, N only)
❌ Not optimized for very large datasets
🚀 Future Improvements
Add strand-specific mode
Support paired-end reads
Handle more CIGAR operations
Optimize using interval trees
Benchmark against featureCounts
📚 Inspiration

This project is inspired by widely used RNA-seq tools:

featureCounts
HTSeq
👨‍💻 Author

Mehran Khan
Bioinformatics Student


This is a learning-oriented implementation aimed at understanding the core logic of RNA-seq read counting, not a replacement for production tools.


---

#

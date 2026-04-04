# ⚡ FastCounter: Lightweight RNA-seq Read Counting Tool

A fast and memory-efficient RNA-seq read counting tool designed for small to medium datasets.  
FastCounter processes aligned reads (SAM format) and gene annotations (GTF format) to generate gene-level counts using an optimized binary search algorithm.

---

## 🧠 Motivation

Existing tools like featureCounts are highly optimized but complex and resource-heavy.  
FastCounter is built as a lightweight alternative to:

- Understand core bioinformatics workflows  
- Demonstrate algorithmic optimization  
- Work efficiently on low-resource systems  

---

## ⚙️ Workflow

---

## 🚀 Features

- ✅ Parses SAM (aligned reads) and GTF (gene annotations)
- ⚡ Fast lookup using binary search (O(n log k))
- 💻 Low memory usage
- 🧩 Simple command-line interface
- 🧪 Works on simulated and real-like datasets

---

## 📦 Installation

Clone the repository:


git clone https://github.com/Mehran12121/fast-counter.git
cd fast-counterpython main.py <input.sam> <genes.gtf> <output.txt>
python main.py example.sam example.gtf result.txt
input format
read1 0 chr1 1000 ...
read2 0 chr1 5000 ...
chr1 source gene 900 2000 . + . gene_id "GeneA";
chr1 source gene 4000 6000 . + . gene_id "GeneB";
gene_id    count
GeneA      2
GeneB      1
⚡ Algorithm & Optimization
🔹 Naive Approach
Checks every gene for each read
Time Complexity: O(n × k)
🔹 FastCounter Approach
Sorts gene intervals
Uses binary search (bisect)
Time Complexity: O(n log k)

👉 This significantly improves performance for large datasets.

🧪 Performance Benchmark

Tested on simulated dataset:

📊 Reads: 5,000
🧬 Genes: 100
⏱ Runtime: ~0.01–0.05 seconds
🏗 Project Structure
fast-counter/
│
├── main.py        # CLI entry point
├── parser.py      # SAM & GTF parsing
├── counter.py     # Counting logic (binary search)
├── test_data/     # Sample data
└── README.md
🔬 Real-world Usage

FastCounter can be used after alignment tools such as:

Bowtie2
HISAT2

Example pipeline:

FASTQ → Bowtie2 → SAM → FastCounter → counts.txt
🚧 Limitations
No BAM support (SAM only)
No multi-threading
Simplified overlap logic
Not strand-specific
🚀 Future Improvements
BAM file support (pysam)
Multi-threading for speed
Strand-specific counting
Advanced gene overlap handling
Integration with full RNA-seq pipelines
👨‍💻 Author

Mehran Khan
Bioinformatics Student



This project focuses on understanding core bioinformatics concepts and optimizing them using efficient algorithms.
It is designed as a learning + demonstration tool rather than a production-grade alternative.



Input:
- SAM file with aligned reads
- GTF file with gene annotations

Command:
python main.py example.sam example.gtf output.txt

Output:
gene_id    count
GeneA      2
GeneB      1
## Performance

Tested on:
- 5000 reads
- 100 genes

Runtime:
~0.01 seconds

Optimization:
Binary search reduces complexity from O(n × k) → O(n log k)
## Architecture

- parser.py → parses SAM and GTF files
- counter.py → counts reads using binary search
- main.py → CLI interface
- ## Future Improvements
- BAM support
- Multi-threading
- Strand-specific counting
- Integration with real RNA-seq pipelines

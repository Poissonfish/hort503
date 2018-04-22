params.base_dir = "/data/hort503_01_s18/example-data/Day26";
params.fastq_pairs = Channel
  .fromFilePairs("${params.base_dir}/SRR*/SRR*_{1,2}.fastq")

process trimPaired{
  module "trimmomatic/0.36"
  executor "slurm"
  input:
    set SRR, file(fastq_files) from fastq_pairs
  output:
    set SRR, file("*.trim.fastq") into trimmed_reads
  """
  java -Xmx512m org.usadellab.trimmomatic.Trimmomatic PE \
          -threads 1 -phred33 \
          ${SRR}_1.fastq \
          ${SRR}_2.fastq \
          ${SRR}_1.trim.fastq \
          ${SRR}_1s.trim.fastq \
          ${SRR}_2.trim.fastq \
          ${SRR}_2s.trim.fastq \
          ILLUMINACLIP:${ILLUMINACLIP_PATH}/fasta_adapter.txt:2:40:15 \
          LEADING:3 TRAILING:6 SLIDINGWIDOW:4:15 MINLEN:50
  """
}

















params.base_dir = "/data/hort503_01_s18/example-data/Day26";
params.reads = "${params.base_dir}/SRR*/*_{1,2}.fastq"
pairs4trim = Channel
    .fromFilePairs(params.reads)
    .ifEmpty { error "Cannot find any reads matching: ${params.reads}" }
process trimmomatic {
  module "trimmomatic/0.36"
  stageInMode "copy"
  publishDir "$SRR", mode: "copy"
  input:
    set SRR, file(fastq) from pairs4trim
  output:
    set SRR, file("*.trim.fastq") into trimmed_reads
  """
      java -Xmx512m org.usadellab.trimmomatic.Trimmomatic PE \
        -threads 1 -phred33 \
        ${SRR}_1.fastq \
        ${SRR}_2.fastq \
        ${SRR}_1.trim.fastq \
        ${SRR}_1s.trim.fastq \
        ${SRR}_2.trim.fastq \
        ${SRR}_2s.trim.fastq \
        ILLUMINACLIP:\${ILLUMINACLIP_PATH}/fasta_adapter.txt:2:40:15 \
        LEADING:3 TRAILING:6 SLIDINGWINDOW:4:15 MINLEN:50
  """
}

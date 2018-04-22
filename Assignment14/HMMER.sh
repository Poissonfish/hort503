# Set up environment
  cd /data/hort503_01_s18/james.chen
  mkdir src
  mkdir bin
  PATH=$PATH:/data/hort503_01_s18/james.chen/bin
  export PATH
# Download files and unzip it
  wget 'http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz' -O hmmer-3.1b1.tar.gz
  gzip -d hmmer-3.1b1.tar.gz
  tar -xf hmmer-3.1b1.tar
  wget 'https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz' -O muscle.tar.gz
  gzip -d muscle.tar.gz
  tar -xf muscle.tar
# Inspect the file
  cd hmmer-3.1b2
  less INSTALL
# Installation
  ./configure --prefix=/data/hort503_01_s18/james.chen/
  make
  make install
  mv muscle3.8.31_i86linux64 /data/hort503_01_s18/james.chen/bin/muscle
# Exercise
  mkdir c_elegans
  wget 'ftp://ftp.wormbase.org/pub/wormbase//species/c_elegans/sequence/genomic/c_elegans.PRJNA13758.WS237.genomic.fa.gz' -O WS237.fa.gz
  gzip -d c_elegans/WS237.fa.gz
  muscle -in target.fa -out target.fa.aln
  hmmbuild target.fa.aln.hmm target.fa.aln
  hmmsearch target.fa.aln.hmm WS237.fa > result.txt

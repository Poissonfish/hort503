# Get arguments
  echo "Getting arguments ..."
  fileName=$1
  dbName=$2
  wd=$(pwd)
# For split files
  if [ -d SplitFSA ]
  then
    rm -r SplitFSA
  fi
  if [ -d BlastResult ]
  then
    rm -r BlastResult
  fi
  mkdir SplitFSA
  mkdir BlastResult
# Split given file into pieces
  echo "Splitting files... "
  awk 'BEGIN{RS=">"}
  {
    print ">" $0 >> "SplitFSA/seq_" (int(NR/5000) + 1) ".fasta"
  }' $fileName
  echo "$(tail -n +2 SplitFSA/seq_1.fasta)" > SplitFSA/seq_1.fasta
# Do blast on these files
  echo "Submitting BLAST tasks ..."
  nFiles=$(ls -1q SplitFSA | wc -l)
  sbatch --array="1-${nFiles}" DoBlast.srun ${dbName}

echo "============================================"
echo "Please use 'ls split*' to check the progress"
echo "After the tasks done, use 'sh SummarizeBlast.sh ${wd}' to summarize the results"
echo "============================================"

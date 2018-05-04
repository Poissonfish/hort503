# Get arguments
  echo "Getting arguments ..."
  wd=$1
# Combine reulsts of files into one
  echo "Combining results..."
  if [ $wd/Blast.out ]
  then
    rm $wd/Blast.out
  fi
  cat $wd/BlastResult/seq_*.out >> $wd/Blast.out
# Summarize result
  echo "Summarizing results..."
  awk 'BEGIN{FS="\t"}
  {
    array[$3]++
  }
  END{for(i in array) print i,"\t",array[i]}' $wd/Blast.out | \
  sort -t$'\t' -nrk2 > $wd/Summary.out

echo "Done"

#
sh DoBatchBlast.sh short.fasta /data/hort503_01_s18/example-data/swissprot

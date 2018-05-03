# Get arguments
  echo "Getting arguments ..."
  wd=$1
# Combine reulsts of files into one
  echo "Combining results..."
  rm $wd/blast.out
  cat $wd/splitOut/seq_*.out >> $wd/blast.out
# Summarize result
  echo "Summarizing results..."
  awk 'BEGIN{FS="\t"}
  {
    array[$3]++
  }
  END{for(i in array) print i,"\t",array[i]}' $wd/blast.out | \
  sort -t$'\t' -nrk2 > $wd/summary.out

echo "Done"

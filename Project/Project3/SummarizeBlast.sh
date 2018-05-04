# Get arguments
  echo "Getting arguments ..."
  wd=$1
# Combine reulsts of files into one
  echo "Combining results..."
  if [ -e $wd/seq_all.out ]
  then
    rm $wd/seq_all.out
  fi
  cat $wd/seq_*.out >> $wd/seq_all.out
# Summarize result
  echo "Summarizing results..."
  awk 'BEGIN{FS="\t"}
  {
    array[$3]++
  }
  END{for(i in array) print i,"\t",array[i]}' $wd/seq_all.out | \
  sort -t$'\t' -nrk2 > $wd/Summary.out

echo "Done"

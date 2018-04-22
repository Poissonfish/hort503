#!/bin/bash

export query = $1
export db = $2
export output = $3

muscle -in $query -out $query.aln
hmmbuild $query.aln.hmm $query.aln
hmmsearch $query.aln.hmm $db > $output

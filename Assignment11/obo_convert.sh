egrep "\[Typedef\]|\[Term\]|^id:|^name:|^def:|^namespace" goslim_plant.obo |
awk '/^\[Term\]/ {for (i = 1; i < 5; i ++) {getline; print}}' |
sed 's/^id: //g' | sed 's/^name: //g' | sed 's/^def: //g' | sed 's/^namespace: //g' |
awk 'BEGIN {FS = "\t"}; {printf "%s" (NR % 4 == 0 ? RS : FS), $1}' > goslim_plant.out

#!/bin/env sh

lines=$(tput lines)
cols=$(tput cols)

awkscript='
  {
    letters="･ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝमॶळओΔβλφψωρμΞΨδאש"
    lines=$1
    random_col=$3
    c=$4
    letter=substr(letters,c,1)
    cols[random_col]=0;
    for (col in cols) {
      line=cols[col];
      cols[col]=cols[col]+1;
      printf "\033[%s;%sH\033[2;32m%s", line, col, letter;
      printf "\033[%s;%sH\033[1;37m%s\033[0;0H", cols[col], col, letter;
      if (cols[col] >= lines) {
        cols[col]=0;
      }
    }
  }
'
awkscript2='
  {
    letters="                                                                            "
    lines=$1
    random_col=$3
    c=$4
    letter=substr(letters,c,1)
    cols[random_col]=0;
    for (col in cols) {
      line=cols[col];
      cols[col]=cols[col]+1;
      printf "\033[%s;%sH\033[2;32m%s", line, col, letter;
      printf "\033[%s;%sH\033[1;37m%s\033[0;0H", cols[col], col, letter;
      if (cols[col] >= lines) {
        cols[col]=0;
      }
    }
  }
'

while true;do
echo -e "\e[1;40m"
clear
i=0
while [ $i -lt 200 ] ;do
  echo $lines $cols $(( $RANDOM % $cols)) $(( $RANDOM % 72 ))
  sleep 0.08
  i=$(($i + 1 ))
#  echo "$i" > /tmp/i.tmp
done | awk "$awkscript"

while [ $i -lt 200 ] ;do
  echo $lines $cols $(( $RANDOM % $cols)) $(( $RANDOM % 72 ))
  sleep 0.08
  i=$(($i + 1 ))
#  echo "$i" > /tmp/i.tmp
done | awk "$awkscript2"
done

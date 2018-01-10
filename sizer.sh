#!/bin/bash

i=1
e=1
while [ $e -ne 0 ] 
do 
 curl -G https://images-api.nasa.gov/search --data-urlencode "q=ramon" --data-urlencode "page=$i" --data-urlencode "media_type=image" > ramon$i.json
 l=`jq .collection.metadata.total_hits ramon$i.json`
 echo "total hits $l"
 if [ $l -gt 100 ];
  echo "more than 1 page"
  then
  (( mod = $l % 100 ));((( times = $l - $mod) ));((times = times/100));
  echo "additional $times pages to get"
  for j in `seq 1 $times`
  do 
   (( page = $j +1 ))
   echo "getting page $page"
   curl -G https://images-api.nasa.gov/search --data-urlencode "q=ramon" --data-urlencode "page=$page" --data-urlencode "media_type=image" > ramon$page.json
  done
 fi
  e=0 
echo "done collection"
done

cat access.log | wc -l

echo ~~~~

awk '{print $6}' access.log | sort | uniq -c | sort -n

echo ~~~~

cat  access.log | awk '{print $7}' | sort | uniq -c | sort -nk1 | tail -10

echo ~~~~

awk '$9~ /^4/ {print $7,$9,$10,$1}' access.log | sort -nk3 | tail -5

echo ~~~~

cat  access.log | awk '$9~/^5/ {print $1}' | uniq -c | sort -n | tail -5


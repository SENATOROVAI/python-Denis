import operator
from collections import Counter
from shlex import split
from subprocess import Popen, PIPE


# cat access.log | wc -l
def readlines_counter(upload_file_path):
    p1 = Popen(split(f"cat {upload_file_path}"), stdout=PIPE)
    p2 = Popen(split("wc -l"), stdin=p1.stdout, stdout=PIPE)
    print(int(p2.communicate()[0]))


# cat access.log | awk '{print $6}' | sort | uniq -c | sort -n
def test_get_requests_type(upload_file_path):
    p1 = Popen(split(f"cat {upload_file_path}"), stdout=PIPE)
    p2 = Popen(split("awk '{print $6}'"), stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(split("sort"), stdin=p2.stdout, stdout=PIPE)
    p4 = Popen(split("uniq -c"), stdin=p3.stdout, stdout=PIPE)
    p5 = Popen(split("sort -n"), stdin=p4.stdout, stdout=PIPE)
    asn = p5.communicate()[0]
    print(asn)


# cat  access.log | awk '{print $7}' | sort | uniq -c | sort -nk1 | tail -10
def top_ten_frequent_requests(upload_file_path):
    p1 = Popen(split(f"cat {upload_file_path}"), stdout=PIPE)
    p2 = Popen(split("""awk '{print $7}'"""), stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(split("sort"), stdin=p2.stdout, stdout=PIPE)
    p4 = Popen(split("uniq -c"), stdin=p3.stdout, stdout=PIPE)
    p5 = Popen(split("sort -nk1"), stdin=p4.stdout, stdout=PIPE)
    p6 = Popen(split("tail -10"), stdin=p5.stdout, stdout=PIPE)
    print(p6.communicate())


# cat access.log | awk '$9~ /^4/ {print $7,$9,$10,$1}' | sort -nk3 | tail -5
def five_heaviest_requests_with_4xx(upload_file_path):
    p1 = Popen(split(f"cat {upload_file_path}"), stdout=PIPE)
    p2 = Popen(split("""awk '$9~ /^4/ {print $7,$9,$10,$1}'"""), stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(split("sort -nk3"), stdin=p2.stdout, stdout=PIPE)
    p4 = Popen(split("tail -5"), stdin=p3.stdout, stdout=PIPE)
    print(p4.communicate())


# cat  access.log | awk '$9~/^5/ {print $1}' | uniq -c | sort -n | tail -5
def top_five_frequent_requests_with_5xx(upload_file_path):
    p1 = Popen(split(f"cat {upload_file_path}"), stdout=PIPE)
    p2 = Popen(split("""awk '$9~/^5/ {print $1}'"""), stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(split("uniq -c"), stdin=p2.stdout, stdout=PIPE)
    p4 = Popen(split("sort -n"), stdin=p3.stdout, stdout=PIPE)
    p5 = Popen(split("tail -5"), stdin=p4.stdout, stdout=PIPE)
    print(p5.communicate())

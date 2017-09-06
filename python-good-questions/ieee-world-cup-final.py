# ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team

n, m = [int(x) for x in raw_input().split()]

max_topics = 0
count = 0

people = [raw_input() for j in range(n)]

for i in range(n):
    for j in range(i+1, n):
        topics = bin(int(inp[i], 2) | (int(inp[j], 2))).count('1')
        if topics > max_topics:
            max_topics = topics
            count = 1
        elif topics == max_topics:
            count += 1

print max_topics
print count
a = int(input())
k = int(input())
digit = 0
n_line_len = pow(2, a - 1)
while n_line_len != 1:
  line_middle = n_line_len // 2
  if k > line_middle:
    digit = 0 if digit == 1 else 1
    k -= line_middle
  n_line_len = line_middle

print(digit)

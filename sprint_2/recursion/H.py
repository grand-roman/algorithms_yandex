def generate_parenthesis(n, current='', opened=0, closed=0, collected=None):
    if collected is None:
        collected = []

    if closed == n:
        collected.append(current)

    if opened < n:
        generate_parenthesis(n, current=current + '(', opened=opened + 1, closed=closed, collected=collected)

    if closed < opened:
        generate_parenthesis(n, current=current + ')', opened=opened, closed=closed + 1, collected=collected)

    return collected


a = int(input())
for i in generate_parenthesis(a):
  print(i)

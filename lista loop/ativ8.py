def primo(num):
  if num <= 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
    return True

for num in range(1, 51):
  if primo(num):
    print(num)
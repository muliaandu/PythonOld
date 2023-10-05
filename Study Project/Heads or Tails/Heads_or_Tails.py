import random

# 1 means Heads
# 0 means Tails

coin = random.randint(0, 1)
if coin == 0:
    print(f"{coin} means Tails")
else:
    print(f"{coin} means Heads")
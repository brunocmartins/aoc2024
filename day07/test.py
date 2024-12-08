from itertools import product

with open("day07/sample.txt") as f:
    lines = f.read().strip().split("\n")

ans = 0
for line in lines:
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    def test(combo):
        ans = nums[0]
        for i in range(1, len(nums)):
            if combo[i - 1] == "+":
                ans += nums[i]
            else:
                ans *= nums[i]
        return ans
    
    for combo in product("+*", repeat=len(nums) - 1):
        if test(combo) == value:
            ans += value
            print(combo)
            break

print(ans)
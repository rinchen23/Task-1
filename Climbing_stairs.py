class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize the base cases
        prev2 = 1  # f(1)
        prev1 = 2  # f(2)

        # Compute the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            # Update the previous two values
            prev2 = prev1
            prev1 = current

        return prev1

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
print(solution.climbStairs(5))  # Output: 8
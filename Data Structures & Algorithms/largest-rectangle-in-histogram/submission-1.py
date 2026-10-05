class Solution:
    """
    Compute largest rectangle area in a histogram using a monotonic increasing stack.
    
    Algorithm:
    - Use sentinel zeros appended to both ends of the heights array to simplify boundary handling.
    - Maintain a stack of indices whose corresponding heights are in strictly increasing order.
    - When we see a height that is less than the height at the top of the stack, we pop
      the stack and compute the maximal rectangle that uses the popped height as the
      limiting height. Width is computed from the current index and the new stack top.
    
    Complexity: O(n) time, O(n) space.
    Design patterns: monotonic stack, sentinel technique to simplify boundary logic.
    """
    # Each comment line below explains the subsequent code line(s) clearly.
    
    # Define the required method matching LeetCode signature.
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Create a local variable to hold a new array with sentinel zeros at both ends
        # This avoids additional boundary checks when computing widths.
        extended = [0] + heights + [0]
        # Initialize a stack of indices starting with the index of the left sentinel (0)
        # Stack will maintain indices of increasing heights.
        stack = [0]
        # Variable to track the maximum area seen so far.
        max_area = 0
        # Iterate through each index in the extended heights array starting from 1.
        # We will process up to the last sentinel index.
        for i in range(1, len(extended)):
            # While current height is less than the height at the top index of the stack,
            # we have found the right boundary for the bar at stack top.
            while extended[i] < extended[stack[-1]]:
                # Pop the index of the bar that we will compute area for.
                height_index = stack.pop()
                # The height for the popped bar.
                height = extended[height_index]
                # Width is the distance between the current index and the new stack top minus one.
                # This computes the maximal width where the popped height is the limiting height.
                width = i - stack[-1] - 1
                # Update the max_area if this area is larger.
                if height * width > max_area:
                    max_area = height * width
            # After processing pops, push the current index onto the stack to maintain increasing heights.
            stack.append(i)
        # Return the maximum area found.
        return max_area
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Determine if s2 contains a substring that is a permutation of s1.
        
        Algorithm:
        - Use a sliding window of fixed size len(s1) across s2.
        - Maintain two frequency arrays (size 26) for s1 (target) and current window.
        - Maintain 'matches' count of positions where target[i] == window[i].
        - When matches == 26, the current window is a permutation -> return True.
        
        Design patterns:
        - Sliding window for substring search with O(1) incremental updates.
        - Frequency-count arrays leverage fixed small alphabet (constant space).
        
        Time complexity: O(len(s2) + len(s1))
        Space complexity: O(1) (26-size arrays)
        """
        # If target string is longer than source string, no permutation can fit.
        if len(s1) > len(s2):
            # Immediately return False for this infeasible case.
            return False

        # Prepare frequency arrays of size 26 for lowercase letters.
        target = [0] * 26
        # Prepare frequency array for the current sliding window in s2.
        window = [0] * 26

        # Populate the target counts for s1.
        for ch in s1:
            # Increment the count for the letter in target.
            target[ord(ch) - ord('a')] += 1

        # Populate the initial window counts for the first len(s1) characters of s2.
        window_size = len(s1)
        for i in range(window_size):
            # Increment the count for the letter in the initial window.
            window[ord(s2[i]) - ord('a')] += 1

        # Initialize matches to count how many indices have equal counts.
        matches = 0
        # Compute initial matches by comparing each letter index.
        for i in range(26):
            # If counts are equal at this index, it's a match.
            if target[i] == window[i]:
                matches += 1

        # If all 26 character counts match, we found a permutation.
        if matches == 26:
            # Return early with True.
            return True

        # Slide the window over s2 from index window_size to end.
        for right in range(window_size, len(s2)):
            # Index of the incoming character to the window.
            in_idx = ord(s2[right]) - ord('a')
            # Index of the outgoing character from the window.
            out_idx = ord(s2[right - window_size]) - ord('a')

            # If window count for outgoing char equals target before change, decrement matches.
            if window[out_idx] == target[out_idx]:
                matches -= 1
            # Remove outgoing char from window counts.
            window[out_idx] -= 1
            # If window count for outgoing char equals target after change, increment matches.
            if window[out_idx] == target[out_idx]:
                matches += 1

            # If window count for incoming char equals target before change, decrement matches.
            if window[in_idx] == target[in_idx]:
                matches -= 1
            # Add incoming char to window counts.
            window[in_idx] += 1
            # If window count for incoming char equals target after change, increment matches.
            if window[in_idx] == target[in_idx]:
                matches += 1

            # If all 26 characters match, current window is a permutation.
            if matches == 26:
                # Return immediately True.
                return True

        # If no window matched, return False.
        return False
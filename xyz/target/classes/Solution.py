class Solution:
    def calculate_z_array(self, s: str) -> list[int]:
        length = len(s)
        z = [0] * length
        left, right = 0, 0

        for i in range(1, length):
            if i < right:
                z[i] = min(right - i, z[i - left])
            while i + z[i] < length and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > right:
                left = i
                right = i + z[i]

        return z

    def minStartingIndex(self, text: str, pattern: str) -> int:
        # Create a combined string of pattern + text
        combined = pattern + text
        forward_z = self.calculate_z_array(combined)

        # Prepare reversed pattern and text
        reversed_pattern = pattern[::-1]
        reversed_text = text[::-1]
        combined_reversed = reversed_pattern + reversed_text
        backward_z = self.calculate_z_array(combined_reversed)

        total_length = len(forward_z)
        pattern_length = len(pattern)
        index = 2 * pattern_length

        # Adjust index for backward comparison
        index = total_length - index
        index = pattern_length + index

        for i in range(pattern_length, total_length):
            if index >= total_length or index < pattern_length:
                break

            forward_value = forward_z[i]
            backward_value = backward_z[index]

            if forward_value + backward_value >= pattern_length - 1:
                return i - pattern_length

            index -= 1

        return -1
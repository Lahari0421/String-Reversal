def reverse_string(s):
    # Strip leading/trailing whitespace and reverse the string
    return s.strip()[::-1]

# Example usage:
input_str = "hello,"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: 'olleh'

import re
class StringCalculator:
    def add(self, numbers: str) -> int:
        """Adds numbers provided in a string format."""
        if not numbers:
            return 0  # Step 1: Handle empty string

        delimiter = r"[,\n]"  # Default delimiters: comma or newline

        # Step 4: Support custom delimiter
        if numbers.startswith("//"):
            delimiter_end_index = numbers.index("\n")
            custom_delimiter = numbers[2:delimiter_end_index]
            delimiter = re.escape(custom_delimiter)  # Escape special characters for regex
            numbers = numbers[delimiter_end_index + 1:]
        
        # Split numbers using the determined delimiter
        number_list = re.split(delimiter, numbers)
        number_list = [int(num) for num in number_list if num]

        # Step 5: Handle negative numbers
        negative_numbers = [num for num in number_list if num < 0]
        if negative_numbers:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
        
        # Sum all valid numbers
        return sum(number_list)

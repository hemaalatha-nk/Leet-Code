class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # position to write compressed output
        read = 0   # position to read input
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count occurrences of current char
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write

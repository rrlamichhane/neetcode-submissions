class Solution:
    ascii_length = 6
    ascii_floor = 99999

    def encode(self, strs: List[str]) -> str:
        """
        Store the first "char" of the string, then add the numerical difference in ord
        for each consecutive character from the last character.
        """
        encoded_string = ""
        if not strs:
            return "0"
        for word in strs:
            if not word:
                encoded_string += "0_"
                continue
            first_char = word[0]
            encoded_word, last_ascii = first_char, ord(first_char)
            # Encode each word
            for c in word[1:]:
                cur_ascii = ord(c)
                ascii_diff = str(cur_ascii - last_ascii + self.ascii_floor)
                ascii_padding = self.ascii_length - len(ascii_diff)
                ascii_diff_str = "0" * ascii_padding + ascii_diff
                encoded_word += ascii_diff_str
                last_ascii = cur_ascii
            encoded_string += str(len(word)) + "_" + encoded_word
        return str(len(strs)) + "_" + encoded_string

    def find_encoded_length(self, s:str) -> str:
        count = ""
        for c in s:
            if c.isnumeric():
                count += c
            else:
                break
        return count

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 1:
            return []
        if len(s) == 3:
            return [""]
        count = self.find_encoded_length(s)
        no_of_words = int(count)
        words = []
        i = len(count) + 1
        for _ in range(no_of_words):
            len_word = self.find_encoded_length(s[i:])
            i += (len(len_word)+1)
            if int(len_word) == 0:
                cur_word = ""
            elif int(len_word) == 1:
                cur_word = s[i]
                i += 1
            else:
                cur_word = s[i]
                i += 1
                for j in range(int(len_word)-1):
                    ascii_ord = s[i:i+self.ascii_length]
                    ascii_ord_norm = int(ascii_ord) + ord(cur_word[-1]) - self.ascii_floor
                    decoded_char = chr(ascii_ord_norm)
                    cur_word += decoded_char
                    i += self.ascii_length
            words.append(cur_word)
        return words

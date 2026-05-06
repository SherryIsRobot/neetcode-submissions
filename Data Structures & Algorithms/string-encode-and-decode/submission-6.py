class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:

            return ""

        encode_str = ''.join(strs)

        len_str = []

        for s in strs:

            len_str.append(str(len(s)))

        length_str = ','.join(len_str)

        return length_str + '#' + encode_str

    def decode(self, s: str) -> List[str]:

        if not s:

            return []

        length_str, encode_str = s.split('#', 1)

        lengths = [int(x) for x in length_str.split(',')]

        res = []

        i = 0

        for length in lengths:

            res.append(encode_str[i:i + length])

            i += length

        return res
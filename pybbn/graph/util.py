class IdUtil:
    @staticmethod
    def hash_string(s):
        hash_value = 0

        if len(s) == 0:
            return hash_value

        for c in s:
            hash_value = ((hash_value << 5) - hash_value) + ord(c)
            hash_value |= 0

        return hash_value
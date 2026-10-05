class TimeMap:

    def __init__(self):
        self.key_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_map:
            self.key_map[key] = []
        self.key_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_map:
            return ""
        key_values = self.key_map[key]
        if key_values[-1][1] <= timestamp:
            return key_values[-1][0]
        l, r = 0, len(key_values)
        min_time = ("", timestamp)
        while l <= r:
            if count == 9:
                return ""
            m = (l + r)// 2
            m_val = key_values[m][0]
            m_time = key_values[m][1]
            if m_time > timestamp:
                r = m - 1
            elif m_time < timestamp:
                min_time = (m_val, m_time)
                l = m + 1
            else:
                return m_val
        if min_time[1] < timestamp:
            return min_time[0]
        return ""

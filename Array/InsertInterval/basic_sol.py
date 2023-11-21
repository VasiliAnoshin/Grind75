def insert(intervals, newInterval):
    start, end, output = 0, 1, []
    for i, inter in enumerate(intervals):
        if inter[start] > newInterval[end]:
            output.append(newInterval)
            output.extend(intervals[i:])
            return output
        elif inter[end] < newInterval[start]:
            output.append(inter)
        else:
            newInterval[start] = min(newInterval[start], inter[start])
            newInterval[end] = max(newInterval[end], inter[end])
    output.append(newInterval)
    return output

if __name__ == "__main__":
    res = insert([[1,3], [6,9]], [2,5])
    print(res)
    res = insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    print(res)
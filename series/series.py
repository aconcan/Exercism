def slices(series, length):
    if length <= 0 or len(series) < length:
        raise ValueError('.+')
    
    # Ensuring all values are int digits
    series = list(map(int, series))
    return [series[i:length+i] for i in range(0, len(series)-length+1, 1)]

    

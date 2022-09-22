#Copyright 2022-present, Author: 5MysterySD

def convertBytes(sz) -> str:
    if not sz: return ""
    sz = int(sz)
    ind = 0
    Units = {0: 'Bytes', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB', 5: 'PB', 6: 'EB'}
    while sz > 2**10:
        sz /= 2**10
        ind += 1
    return f"{round(sz, 2)} {Units[ind]}"


def convertTime(mss: int) -> str:
    s, ms = divmod(mss, 1000)
    m, s = divmod(s, 60)
    hr, m = divmod(m, 60)
    days, hr = divmod(hr, 24)
    convertedTime = (f"{days}d, " if days else "") + \
          (f"{hr}h, " if hr else "") + \
          (f"{m}m, " if m else "") + \
          (f"{s}s, " if s else "") + \
          (f"{ms}ms, " if ms else "")
    return convertedTime[:-2]

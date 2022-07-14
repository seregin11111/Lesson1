from Levenshtein import distance
primer = [
    ('смеситель', 'лейка'),
    ('кранбукса', 'кран'),
    ('раковина', 'рак'),
    ('квадрат', 'квадратура'),]
if __name__ == '__main__':
    for sourse, dest in primer:
        dist = distance(sourse, dest)
        print('sourse:', sourse, ', dest:', dest, '; distance =', dist)
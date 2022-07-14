import difflib

spisok = """Сега
Серый
Серёжа
Сергуня
Серёгин
Сергеич
""".split('\n')

dest = 'Сергей'

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

if __name__ == '__main__':
    for i in spisok:
        print(i, dest, similarity(i, dest))
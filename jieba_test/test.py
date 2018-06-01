from jieba.analyse import extract_tags
with open('十九大.txt', errors='ignore') as f:
    data = f.read()
res = extract_tags(data)
print(res)
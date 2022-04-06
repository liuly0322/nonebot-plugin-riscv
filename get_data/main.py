import io
import json
from utils import word_diff

f = open("test.txt")               # 返回一个文件对象
line = f.readline()               # 调用文件的 readline()方法
curr_block = [line]
total_blocks = []
while line:
    if line == '\n':
        # 处理当前块
        command = curr_block[0].split()[0]
        total_blocks.append(
            {'name': command, 'content': ''.join(curr_block[:-1]), 'relevant': []})
        curr_block = []
    # 新的块
    line = f.readline()
    curr_block.append(line)
f.close()

# 预先处理，对每个 total_blocks 中的 name 比较编辑距离，生成 relevant 信息
# 允许编辑距离差为 1
for _start in total_blocks:
    for _goal in total_blocks:
        start, goal = _start.get('name'), _goal.get('name')
        if start == goal:
            continue
        diff = word_diff(start, goal)
        if diff == 1:
            _start['relevant'].append(goal)

detail_file = io.open('data.json', 'w', encoding='utf8')
detail_file.write(json.dumps(total_blocks, default=str, ensure_ascii=False))
detail_file.close()

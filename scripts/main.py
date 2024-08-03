from pathlib import Path
from recorder import Recorder

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

plt.rcParams['font.sans-serif'] = ['SimHei']

db = Recorder()


def get_word_list_set(fp):
    with open(fp, mode='r', encoding='utf-8') as f:
        lines = [s.strip() for s in f.readlines()]

    return set([l for l in lines if l])

def show_venn2(s1, s2, s1_name, s2_name):
    intersection = s1.intersection(s2)
    only_s1 = s1 - intersection
    only_s2 = s2 - intersection
    venn2(subsets=(len(only_s1), len(only_s2), len(intersection)), set_labels=(s1_name, s2_name))
    plt.show()


def show_analysis(wn, cn, wl, cl, cn2=None):
    assets_path = Path.cwd() / 'assets'
    a = get_word_list_set(assets_path / f'{wn}.txt')
    b = set(e['word'] for e in db.getCEFR(cn, cn2))

    show_venn2(a, b, wl, cl)

def main():
    # show_analysis('小学', 'A1', '小学词汇', 'CEFR_A1')
    # show_analysis('初中', 'A2', '初中词汇', 'CEFR_A2')
    # show_analysis('高中', 'B1', '高中词汇', 'CEFR_B1')
    # show_analysis('四级', 'B1', '四级词汇', 'CEFR_B1')
    # show_analysis('六级', 'B2', '六级词汇', 'CEFR_B2')
    # show_analysis('小学', 'B2', '小学词汇', 'CEFR_B2')
    show_analysis('专四专八', 'B2', '专四专八词汇', 'CEFR_C1_C2', 'C2')

    pass



if __name__ == '__main__':
    db.start()
    main()
    db.close()
from pathlib import Path

assets_path = Path.cwd().parent / 'assets'


def get_word_list_set(name):
    with open(assets_path / (name + '.txt'), mode='r', encoding='utf-8') as f:
        lines = [s.strip().lower() for s in f.readlines()]

    return set([l for l in lines if l])


def main():

    sources = [(name, get_word_list_set(name)) for name in ['小学', '初中', '高中', '四级', '六级', '专四专八']]

    targets = [(name, get_word_list_set(name)) for name in ['CEFR_A1', 'CEFR_A2', 'CEFR_B1', 'CEFR_B2', 'CEFR_C1', 'CEFR_C2', 'COCA_20000']]

    # targets.append(('ULTRA', set()))

    nodes = [{"name": name, "count": len(wl)} for name, wl in [*sources, *targets]]

    links = []
    for src, swl in sources:
        for tgt, twl in targets:
            intersection = swl.intersection(twl) if tgt != 'ULTRA' else swl
            if intersection:
                links.append({ "source": src, "target": tgt, "value": len(intersection)})
                # links.append({ "source": src, "target": tgt, "value": len(intersection), "i": intersection if tgt == 'ULTRA' else None})
                # swl = swl - intersection

    # ultra = []
    # for l in links:
    #     if l["i"]:
    #         ultra.extend(list(l["i"]))
    # ultra.sort()
    # with open(assets_path / ('ULTRA' + '.txt'), encoding='utf-8', mode='w') as f:
    #     f.writelines([(w + '\n') for w in ultra])

    graph = {
        "nodes": nodes,
        "links": links
    }
    pass



if __name__ == '__main__':
    main()

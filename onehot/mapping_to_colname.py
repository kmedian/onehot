

def mapping_to_colname(mapping_, typ=None, prefix="col", sep="_",
                       nastate=False):

    def tostr(s):
        return ''.join(str(s).split()).lower()

    mapping = mapping_.copy()
    if nastate:
        mapping["na"] = "na"

    if sep is None:
        sep = ""

    if prefix is None:
        prefix = ""

    if typ in (1, 'encoding', 'enc'):  # 0, 1, 2, etc.
        return list(mapping.keys())
    elif typ in (2, 'label'):  # labela, babelc, etc.
        return list(mapping.values())
    elif typ in (3, 'prefixlabel'):  # col_labela, col_labelc
        return [prefix + sep + tostr(v) for v in mapping.values()]
    elif typ in (4, 'withlabel'):  # col_1_labela, col_2_labelc
        return [
            prefix + sep + tostr(k) + sep + tostr(v)
            for k, v in mapping.items()]
    else:  # (None, 0, 'numbered'): col_1, col_2, etc.
        return [prefix + sep + tostr(k) for k in mapping.keys()]

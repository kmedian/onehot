
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd  # pd.isnull
import scipy.sparse
from grouplabelencode import grouplabelencode
from .onehotencode import onehotencode
from .mapping_to_colname import mapping_to_colname
from collections import Counter


class OneHotDummy(BaseEstimator, TransformerMixin):
    """One-Hot encoder with sklearn-ish API interface that process
    mixed string and numeric labels directly.

    Parameters
    ----------
    mapping : dict, list

    nastate : bool
        - Ignore missing values or unmapped labels
            (Default: False)
        - True to append a column to indicate missing values
            or resp. not mapped labels

    droprule : str
        - drop no label (Default: None)
        - 'least' drop the least frequent label
        - 'most' drop the most frequent label

    spare : bool
        (Default: True)

    nametyp : str
        The way how the columns are named
        - numbered (Default: None)
        - 'prefixlabel'
        - 'withlabel'
        - 'label'
        - 'encoding'

    prefix : str
        Prefix for all column names (Default: "col")

    sep : str
        Seperator used in column names (Default: "_")
    """
    def __init__(self, mapping=None, nastate=False, droprule=None,
                 sparse=True, nametyp=None, prefix="col", sep='_'):
        self.mapping = mapping   # fit or given
        self.nastate = nastate   # see pandas.get_dummies(dummy_na)
        self.droprule = droprule
        self.sparse = sparse
        # column names
        self.nametyp = nametyp
        self.prefix = prefix
        self.sep = sep

    def fit(self, X, y=None):
        """Use fit to create or overwrite the mapping"""
        # drop a column
        drop_label = None
        if self.droprule:
            cnt = dict(Counter(X))
            if self.droprule in ('least'):
                drop_label = min(cnt, key=cnt.get)
            else:  # self.droprule in ('most'):
                drop_label = max(cnt, key=cnt.get)

        # map all strings and numbers
        self.mapping = dict(enumerate(
            [e for e in set(X) if pd.notnull(e) and e not in [drop_label]]))

        return self

    def transform(self, X):
        """Convert a nominal variable to an one-hot encoded matrix"""
        # encode labels according to the mapping (without NaN)
        xlabelenc = grouplabelencode(X, self.mapping, nastate=False)
        # encoded labels to one-hot encoding matrix
        xonehot = onehotencode(xlabelenc, self.mapping)
        # add a NaN column (optional)
        if self.nastate:
            xonehot = scipy.sparse.hstack([xonehot, xonehot.sum(axis=1) == 0])
        # done
        return xonehot

    def get_feature_names(self):
        return mapping_to_colname(
            self.mapping, typ=self.nametyp, prefix=self.prefix,
            sep=self.sep, nastate=self.nastate)

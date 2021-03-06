#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print s

dates = pd.date_range('20130101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df


df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print df2
print df2.dtypes

print df.head()
print df.tail(3)

print df.index
print df.columns
print df.values
print df.describe()
print df.T
df.sort_index(ascending=False)
print df
df.sort_index(axis=1, ascending=False)
print df




print df["A"]
print df.A
print df[0:3]
print df["20130101":"20130103"]
print df.loc[dates[0]]
print df.loc[:,['A','B']]
print df.loc['20130102':'20130104',['A','B']]
print df.loc['20130102',['A','B']]
print df.iloc[3]
print df.iloc[3:5,0:2]
print df.iloc[[1,2,4],[0,2]]
print df.iloc[1:3,:]
print df.iloc[:,1:3]
print df.iloc[1,1]
print df[df.A > 0]
print df[df > 0]
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print s1

df2 = df.copy()
df2[df2 > 0] = -df2
print df2

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print df1

print df.mean()
print df.mean(1)

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print s

df.sub(s, axis='index')
print df

print df.apply(np.cumsum)
print df.apply(lambda x: x.max() - x.min())
s = pd.Series(np.random.randint(0, 7, size=10))
print s
print s.value_counts()

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print s.str.lower()

df = pd.DataFrame(np.random.randn(10, 4))
print df
pieces = [df[:2],df[4:5],df[7:]]
print pd.concat(pieces)

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
print df

s = df.iloc[3]
print df.append(s, ignore_index=True)


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print df

df.groupby('A').sum()
print df

print df.groupby(['A','B']).sum()

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print df

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print ts

ts_utc = ts.tz_localize('UTC')
print ts_utc

df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
print df

df["grade"] = df["raw_grade"].astype("category")
print df["grade"]


df["grade"].cat.categories = ["very good", "good", "very bad"]
print df["grade"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print df["grade"]
print df.groupby("grade").size()

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
p = ts.cumsum().plot()


s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print s
print s.index

d = {'a' : 0., 'b' : 1., 'c' : 2.}
pd.Series(d)

pd.Series(d, index=['b', 'd', 'a'])
print pd


pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print pd
print s[0]
print s[:3]

print s[s > s.median()]
print s[[4, 3, 1]]
print np.exp(s)

print s["a"]
print s["e"]
print "e" in s
print "f" in s































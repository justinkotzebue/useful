import statsmodels.formula.api as smf
import pandas as pd
from pylab import arange, randn
x = arange(20)
y = x * 0.3 + randn(20)
data = pd.DataFrame({'x':x, 'y':y})

# create the data for Rpy
import rpy2.robjects as robjects
import pandas.rpy.common as com
r = robjects.r
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
stats = importr('stats')
base = importr('base')
robjects.globalenv["x"] = FloatVector(x)
robjects.globalenv["y"] = FloatVector(y)

# model without intercept
lm0 = stats.lm("y ~ x + 0")
s = base.summary(lm0)
print s.rx2("r.squared")[0], smf.ols('y ~ x + 0', data).fit().rsquared
print s.rx2("adj.r.squared")[0], smf.ols('y ~ x + 0', data).fit().rsquared_adj

# model with intercept
lm0 = stats.lm("y ~ x + 1")
s = base.summary(lm0)
print s.rx2("r.squared")[0], smf.ols('y ~ x + 1', data).fit().rsquared
print s.rx2("adj.r.squared")[0], smf.ols('y ~ x + 1', data).fit().rsquared_adj

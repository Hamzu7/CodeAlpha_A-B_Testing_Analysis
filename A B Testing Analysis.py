#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy.stats as stats


data = {
    'group': ['control', 'control', 'control', 'test', 'test', 'test'],
    'conversion': [0, 1, 0, 1, 1, 0]
}


df = pd.DataFrame(data)


control_group = df[df['group'] == 'control']['conversion']
test_group = df[df['group'] == 'test']['conversion']


control_conversion_rate = control_group.mean()
test_conversion_rate = test_group.mean()


t_stat, p_value = stats.ttest_ind(control_group, test_group)


print(f"Control group conversion rate: {control_conversion_rate}")
print(f"Test group conversion rate: {test_conversion_rate}")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")


alpha = 0.05
if p_value < alpha:
    print("The result is statistically significant. Reject the null hypothesis.")
else:
    print("The result is not statistically significant. Fail to reject the null hypothesis.")
    
    
    


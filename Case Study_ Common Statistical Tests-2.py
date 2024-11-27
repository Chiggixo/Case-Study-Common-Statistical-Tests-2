#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency, pearsonr, shapiro
from statsmodels.stats.anova import AnovaRM


# In[2]:


data = pd.read_csv('Marketing-campaign-dataset.csv') 


# In[3]:


data.head()


# In[4]:


facebook_impressions = data[data['ext_service_name'] == 'Facebook Ads']['impressions']
google_impressions = data[data['ext_service_name'] == 'Google Ads']['impressions']


# In[5]:


t_stat, p_value_ttest = ttest_ind(facebook_impressions, google_impressions, nan_policy='omit')
print("T-Test Results")
print(f"T-Statistic: {t_stat}, P-Value: {p_value_ttest}\n")


# In[6]:


contingency_table = pd.crosstab(data['weekday_cat'], data['channel_name'])
chi2_stat, p_value_chi2, _, _ = chi2_contingency(contingency_table)
print("Chi-Square Test Results")
print(f"Chi-Square Statistic: {chi2_stat}, P-Value: {p_value_chi2}\n")


# In[7]:


impressions = data['impressions']
clicks = data['clicks']


# In[8]:


corr_coeff, p_value_corr = pearsonr(impressions, clicks)
print("Pearson Correlation Results")
print(f"Correlation Coefficient: {corr_coeff}, P-Value: {p_value_corr}\n")


# In[11]:


shapiro_stat, p_value_shapiro = shapiro(impressions)
print("Shapiro-Wilk Test Results")
print(f"Shapiro Statistic: {shapiro_stat}, P-Value: {p_value_shapiro}\n")


# In[ ]:





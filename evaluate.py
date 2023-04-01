import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import r2_score







def plot_residuals(y, yhat):
    residuals = y - yhat
    
    plt.scatter(residuals, y)
    plt.xlabel('Residuals')
    plt.ylabel("tax_value")
    plt.title("prediction Model")
    plt.show()
    
    

def regression_errors(y, yhat):
    residuals = y - yhat
    baseline = round(y.mean(), 2)
    baseline_residuals = y - baseline
    values = {
        'SSE' : (residuals**2).sum(),
        'TSS' : (baseline_residuals**2).sum(),
        'ESS' : TSS - SSE,
        'MSE' : SSE/len(y),
        'RMSE' : MSE**.5   
        }
    return values
    
 
    
def baseline_mean_errors(y):
    baseline = round(y.mean(), 2)
    residuals = y - baseline
    values = {
        'SSE' : (residuals**2).sum(),
        'MSE' : SSE/len(y),
        'RMSE' : MSE**.5   
        }
    
    return values



def better_than_baseline(y, yhat):
    model_score = r2_score(y, yhat)
    baseline = round(y.mean(), 2)
    baseline_arr = np.full(y.shape , baseline)
    baseline_score = r2_score(y, baseline_arr)
    if model_score > baseline_score:
        return True
    else: 
        return False
    
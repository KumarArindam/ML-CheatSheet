def pred_confidance(model, x_val, percentile = 95, n_pnt):   
    
    """
    x_val = validation input
    percentile = required confidence level
    model = random forest model
    """

    allTree_preds = np.stack([t.predict(x_val) for t in model.estimators_], axis = 0)
    
    err_down = np.percentile(allTree_preds, (100 - percentile) / 2.0  ,axis=0)
    err_up = np.percentile(allTree_preds, 100- (100 - percentile) / 2.0  ,axis=0)
    
    ci = err_up - err_down
yhat = model.predict(x_val)
    y = y_val
    
    df = pd.DataFrame()
    df['down'] = err_down 
    df['up'] = err_up
    df['y'] = y
    df['yhat'] = yhat
    df['deviation'] = (df['up'] - df['down'])/df['yhat']
    df.reset_index(inplace=True)
    df_sorted = df.iloc[np.argsort(df['deviation'])[::-1]]
    return df_sorted
def score(x1,x2):
	metrics.mean_squared_error(x1,x2)

def feat_imp(m,x,y,small_good=True):
"""
m: random forest model
x: matrix of independent variables
y: output variable
small_good: True if smaller prediction score is better
""" 

	score_list={}
	score_list['originals']=score(m.predict(x.values),y)     ##x.values converts it to array
	imp={}
	for i in range(len(x.columns)):
		rand_idx=np.random.permutation(len(x))
		new_col=x.values[rand_idx,i]
		new_x=x.copy()
		new_x[x.columns[i]]=new_col
		score_list[x.columns[i]]=score(m.predict(new_x.values),y)
		imp[x.columns[i]]=score_list['originals']-score_list[x.columns[i]]

	if small_good:
		return sorted(imp.items(),key:lambda x:x[1])
	else: return sorted(imp.items(), key=lambda x: x[1], reverse=True)

#importance = feat_imp(ens, X_train[cols], y_train); importance
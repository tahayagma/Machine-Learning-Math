def confusion_Matrix(y_test,y_pred):
    y_pred = y_pred.reshape(254,1) # reshape y_predict values
    data_sum  = pd.DataFrame(np.array(y_test)-y_pred,columns =['result'])
    data_extraction = pd.DataFrame(np.array(y_test)+y_pred,columns =['result'])
    total_sample = len(c) # total number of samples
    
    totaL_true =data_sum.query("result == 0").count() # number of correctly classified samples (all correctly classified 0 and 1)
    
    true_positive = data_extraction.query("result == 2").count()
    
    true_negative = data_extraction.query("result == 0").count()
    
    false_positive = data_sum.query("result == -1").count()
    
    false_negative = data_sum.query("result == 1").count()
    
    accuracy_score  = (true_positive+true_negative)/total_sample
    
    precision = true_positive/(true_positive+false_positive)
    
    recall = true_positive/(true_positive+false_negative)
    
    f1_score = 2*((precision*recall)/(precision+recall))
    
    print(f"accuracy:{round(accuracy_score[0],2)}\nprecision:{round(precision[0],2)}\nrecall:{round(recall[0],2)}\nf1_score:{round(f1_score[0],2)}")
    
    return np.array([true_negative,false_positive,false_negative,true_positive]).reshape(2,2)

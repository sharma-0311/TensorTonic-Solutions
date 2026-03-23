def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    TP = 0
    FP = 0
    FN = 0
    if len(y_true) == len(y_pred):
        for i in range(len(y_true)):
                if y_true[i] == y_pred[i]:
                    TP += 1
                else:
                    FP +=1
                    FN +=1

        f1_score = 2*TP/(2*TP+FP+FN)
        return f1_score
        
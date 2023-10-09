import numpy as np

def calculate_metrics(tp, tn, fp, fn):
  """Calculates recall, precision, specificity, and F1 score from a confusion matrix.

  Args:
    confusion_matrix: A 3x3 confusion matrix.

  Returns:
    A tuple containing the recall, precision, specificity, and F1 score.
  """


  # tp = confusion_matrix[1, 1]
  # tn = confusion_matrix[0, 0]
  # fp = confusion_matrix[0, 1]
  # fn = confusion_matrix[1, 0]

  recall = tp / (tp + fn)
  precision = tp / (tp + fp)
  specificity = tn / (tn + fp)
  f1_score = 2 * (precision * recall) / (precision + recall)

  return recall, precision, specificity, f1_score


def matrix_conversion(confusion_matrix, pos):
  if pos == 0:
    tp = confusion_matrix[0, 0]
    tn = confusion_matrix[1, 1] + confusion_matrix[1, 2] + confusion_matrix[2, 1] + confusion_matrix[2, 2]
    fp = confusion_matrix[1, 0] + confusion_matrix[2, 0]
    fn = confusion_matrix[0, 1] + confusion_matrix[0, 2]

  elif pos == 1:
    tp = confusion_matrix[1, 1]
    tn = confusion_matrix[0, 0] + confusion_matrix[0, 2] + confusion_matrix[2, 0] + confusion_matrix[2, 2]
    fp = confusion_matrix[0, 1] + confusion_matrix[2, 1]
    fn = confusion_matrix[1, 0] + confusion_matrix[1, 2]


  else:
    tp = confusion_matrix[2, 2]
    tn = confusion_matrix[0, 0] + confusion_matrix[0, 1] + confusion_matrix[1, 1] + confusion_matrix[1, 2]
    fp = confusion_matrix[0, 2] + confusion_matrix[1, 2]
    fn = confusion_matrix[2, 0] + confusion_matrix[2, 1]

  # if pos == 0 :
  #   tp = confusion_matrix[0, 0]
  #   tn = confusion_matrix[1, 1] + confusion_matrix[1, 2] + confusion_matrix[2, 1] + confusion_matrix[2, 2]
  #   fp = confusion_matrix[0, 1] + confusion_matrix[0, 2]
  #   fn = confusion_matrix[1, 0]  + confusion_matrix[2, 0]
  #
  # elif pos == 1:
  #   tp = confusion_matrix[1, 1]
  #   tn = confusion_matrix[0, 0] + confusion_matrix[0, 2] + confusion_matrix[2, 0] + confusion_matrix[2, 2]
  #   fp = confusion_matrix[1, 0] + confusion_matrix[1, 2]
  #   fn = confusion_matrix[0, 1] + confusion_matrix[2, 1]
  #
  #
  # else:
  #   tp = confusion_matrix[2, 2]
  #   tn = confusion_matrix[0, 0] + confusion_matrix[0, 1] +  confusion_matrix[1, 1] + confusion_matrix[1, 2]
  #   fp = confusion_matrix[2, 0] + confusion_matrix[2, 1]
  #   fn = confusion_matrix[0, 2] + confusion_matrix[1, 0]


  return tp, tn, fp, fn

def weighted_calculation(confusion_matrix):
  btp, btn, bfp, bfn = matrix_conversion(confusion_matrix, 0)
  rtp, rtn, rfp, rfn = matrix_conversion(confusion_matrix, 1)
  bltp, bltn, blfp, blfn = matrix_conversion(confusion_matrix, 2)

  print(btp, btn, bfp, bfn)
  print(rtp, rtn, rfp, rfn)
  print(bltp, bltn, blfp, blfn)

  b_recall, b_precision, b_specificity, b_f1_score = calculate_metrics (btp, btn, bfp, bfn)
  r_recall, r_precision, r_specificity, r_f1_score = calculate_metrics(rtp, rtn, rfp, rfn)
  bl_recall, bl_precision, bl_specificity, bl_f1_score = calculate_metrics(bltp, bltn, blfp, blfn)
  print("b", b_recall, b_precision, b_specificity, b_f1_score)
  print("r", r_recall, r_precision, r_specificity, r_f1_score)
  print("bl", bl_recall, bl_precision, bl_specificity, bl_f1_score)

  b_overall = btp + bfn
  r_overall = rtp + rfn
  bl_overall = bltp + blfn

  precision = (b_precision * b_overall + r_precision * r_overall + bl_precision * bl_overall) / (b_overall + r_overall + bl_overall)
  recall =  (b_recall * b_overall  +  r_recall * r_overall  +  bl_recall * bl_overall) / (b_overall + r_overall + bl_overall)
  specificity = (b_specificity * b_overall + r_specificity * r_overall + bl_specificity * bl_overall) / (b_overall + r_overall + bl_overall)
  f1_score = (b_f1_score * b_overall + r_f1_score * r_overall + bl_f1_score * bl_overall) / (b_overall + r_overall + bl_overall)

  return precision, recall, specificity, f1_score


  # Example usage:

confusion_matrix = np.array([[39, 27, 4],
                              [2, 100, 4],
                              [8, 27, 71]])




precision, recall, specificity, f1_score = weighted_calculation(confusion_matrix)

print("Precision:", precision)
print("Recall:", recall)
print("Specificity:", specificity)
print("F1 score:", f1_score)

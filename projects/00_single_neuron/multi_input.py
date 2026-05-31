x = [(1,10),(2,20),(3,30),(4,40),(5,50)]
w = 1
bias = 0
lr = 0.1
for epoch in range(100):
  for input,y_true in x:
    y_pred = input * w + bias
    loss = abs(y_pred-y_true)
    if loss < 0.01:
      break
    print(f"epoch:{epoch},loss:{loss},y_pred:{y_pred},weight:{w}")
    if y_true>y_pred:
      w += lr
    else:
      w -+ lr
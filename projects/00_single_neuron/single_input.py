x = 10
y_true = 100
weight = 1
bias = 0
lr = 0.1

for epoch in range(100):
  y_pred = x*weight + bias
  loss = abs(y_true-y_pred)
  print(f"epoch:{epoch},loss:{loss},y_pred:{y_pred},weight:{weight}")
  if loss < 0.01:
    break
  if y_true > y_pred:
    weight = weight + lr
  else:
    weight = weight - lr
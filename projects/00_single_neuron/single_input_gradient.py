dataset = [
    (1,10),
    (2,20),
    (3,30),
    (4,40),
    (5,50)
]

w = 1
b = 0
lr = 0.001

for epoch in range(500):
    total_loss = 0

    for x, y_true in dataset:

        y_pred = x * w

        error = y_pred - y_true

        loss = abs(error)

        total_loss += loss

        w = w - (lr*error*x)

        b = b - (lr * error)

    print(epoch, total_loss, w, b)
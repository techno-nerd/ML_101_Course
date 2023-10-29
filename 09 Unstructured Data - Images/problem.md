# Digit Identification

Try the problem presented by the MNIST Dataset, which contains 60,000 images of handwritten digits between 0 and 9. 

To load the data into your local environment, use the code below:

```python
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

Use a Convolutional Neural Network to solve the problem, and try comparing it to an Artificial Neural Network. Make sure you apply the softmax activation as it is a multi-class classification problem.

You can use the Fashion_Classification.ipynb file as a template.

If needed, refer to the MNIST_Classification.ipynb file for my approach to the problem
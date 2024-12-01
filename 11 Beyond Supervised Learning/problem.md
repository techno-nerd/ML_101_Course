# Image Generation

So far, we have looked at traditional predictive machine learning and some sequence-to-sequence models for text generation. However, what happens when it comes to images?

Two of the most popular architectures are Diffusion and Generative Adverserial Networks (GANs). Due to the complex nature of the task, both these models take very long to train. To learn more, check out this [video](https://www.youtube.com/watch?v=Av6k8JeifQw)

For diffusion, we will use a pre-trained model. The code on using the OpenAI API is in `diffusion.py`.

For GANs, `mnist-gan.ipynb` details the training process, and `mnist-generator.keras` is the model produced after training.

Using `app.py`, you can experiment with both these models. Follow the steps below to set it up:
1. Ensure that you are using python 3.12
2. `pip install -r requirements.txt`
3. `streamlit run app.py`
Fine-Grained Chip Brand Classifier

A custom Convolutional Neural Network (CNN) built from scratch in TensorFlow, designed to classify 29 specific brands of chips based on packaging features.

The Origin Story

As a university student, I make sure to leverage all the resources my school provides—which heavily includes the free snacks distributed around campus. During this time, I was also taking a "Machine Learning for Data Analysis" course where we were introduced to Convolutional Neural Networks (CNNs).

Looking at a table full of assorted chips one afternoon, the two concepts collided. I wondered if I could build a model from scratch to identify what I was eating. What started as a broad idea to build a "universal snack identifier" eventually evolved into a much more focused, complex computer vision problem: distinguishing between the 29 most common chip brands based on highly similar, shiny foil packaging.

Project Timeline

Phase 1: Brainstorming & Ideation

The project began with the goal of identifying any general snack (chocolates, gummies, chips). However, after evaluating the complexity of the computer vision space, I realized that narrowing the scope created a more impressive engineering challenge.

Phase 2: Defining Project Requirements

I narrowed the project from a broad classifier to a Fine-Grained Image Classification problem. Because bags of Lay's, Ruffles, and Utz share nearly identical physical shapes (crinkly foil bags), the neural network cannot rely on the shape of the object. It must be designed to learn specific typography, logos, and brand color palettes. I finalized a target list of 29 specific chip brands.

Phase 3: Data Gathering & Structuring (How Labeling Works)

To train the model effectively, I needed 50 to 100 images for each of the 29 brands. (Note: I am currently compiling this custom dataset and plan to publish it to Kaggle soon!)

How do you label images for this? Unlike Object Detection (where you manually draw boxes around objects in an image and save coordinates in an XML file), this project uses Image Classification. In TensorFlow, the labeling process is entirely structure-based. You simply name a folder doritos and put 100 images of Doritos inside it. When TensorFlow loads the data, it automatically uses the folder name as the mathematical label for those images.

Phase 4: CNN Creation with TensorFlow

Using tf.keras, I built a deep Convolutional Neural Network from scratch. The architecture uses four sequential convolutional blocks. The early layers detect basic edges and distinct brand colors (like Doritos red vs. Lay's yellow), while deeper layers extract complex shapes like the Chester Cheetah mascot or specific font styles.

Phase 5: Refinement, Tuning, and Deployment

Foil bags have high specular highlights (glare) which confuses neural networks. During this phase, I introduced heavy Data Augmentation (random contrast adjustments, rotations, and flips) during the training loop to force the model to ignore glare. Finally, the model was wrapped in a Streamlit web application and containerized using Docker for easy deployment.
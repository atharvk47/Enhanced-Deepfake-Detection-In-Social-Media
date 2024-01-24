# Enhanced Deepfake Detection In Social Media
Contributors:

1.  Atharv Kurlapkar
2.  Akhand Verma
3.  Aditya Nagulpelli
4.  Prathamesh Gadekar

## Importance:

Detecting deepfakes in social media is crucial for safeguarding trust and integrity online. As the sophistication of deepfake technology grows, the potential for misinformation, manipulation, and identity theft escalates. Effective detection mechanisms are essential to prevent the spread of fake content, protect individuals from malicious intent, and preserve the authenticity of digital interactions, thereby maintaining the credibility of social media platforms and fostering a safer online environment for users.

## Technologies Used:

1. MongoDB for database
2. Express and Node for backend server
3. React for the frontend
4. MUI for enhancing the frontend
5. Flask(ngrok) for public API endpoint for ML model on Colab 
6. Kaggle and Python Notebook for implementing existing research paper, training etc

## Dataset

The DFDC dataset encompasses a combination of real and deepfake video content, from which we extract individual frames to be utilized as still images.
The real images are sourced from CelebA image dataset. Each of these datasets comprises a collection of 5000 images. For this experiment, we consider 1000 randomly picked images from this dataset. The deepfake images, on the other hand, are gleaned from StyleGAN, encompassing a curated selection of 1000 images from each dataset. 

## Literature Review

![Screenshot 2024-01-24 211410](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/96378794/cb7404e9-9df4-4779-b161-f953c3dd3085)


## Snapshots:

1. Login Page
   
   ![Login Page](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/122916032/4d3fdf99-3348-4ef3-a21c-2b5b2a9e61fe)

2. Home Page
   
   ![Home Page](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/122916032/84241da1-092a-4749-ab98-58411fcff340)

3. Putting a post
   
   ![Posting](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/122916032/e6f168a2-2ef3-4b07-882a-0285da6cbad9)

4. Dark Mode

   ![dark mode](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/122916032/195aadea-4766-47aa-8ce0-e0e7cebec5d2)

5. Displaying post

   ![Deepfake post](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/122916032/1b2f5702-1015-425e-8bcd-a63fc12bbe27)

6. Displaying deepfake in backend

![Screenshot 2024-01-24 211801](https://github.com/atharvk47/Enhanced-Deepfake-Detection-In-Social-Media/assets/96378794/d0e90f05-6450-49e5-9307-9de75df5e0de)



## Future Scope:

This rendering of the result can be updated back onto the frontend using jsonify function so that now other users can validate the genuinety of the image.Moreover, we can work on applying deepfake detection on videos, stickers, etc.
 

   

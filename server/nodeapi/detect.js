const express = require('express');
const request = require('request');
const multer = require('multer');
const app = express();
const PORT = 3000;

// Configure multer for handling file uploads
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post('/home', upload.single('image'), function (req, res) {
    const imageBuffer = req.file.buffer; // Access the uploaded image as a buffer

    if (!imageBuffer) {
        return res.status(400).json({ error: 'No image provided' });
    }

    const options = {
        url: 'http://ceab-35-245-40-114.ngrok.io/predict', // Change the URL to match your Flask endpoint
        method: 'POST',
        formData: {
            image: {
                value: imageBuffer,
                options: {
                    filename: 'image.jpg', // Set the filename as needed
                    contentType: 'image/jpeg' // Change to the appropriate content type
                }
            }
        }
    };

    request(options, function (error, response, body) {
        if (error) {
            console.error('error:', error);
            return res.status(500).send('Internal Server Error');
        }
        console.log('statusCode:', response && response.statusCode);
        console.log('body:', body);
        res.send(body);
    });
});

app.listen(PORT, function () {
    console.log(`Server running on port ${PORT}`);
});
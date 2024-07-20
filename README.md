# FastAPI Image Management

This FastAPI application provides endpoints for uploading, retrieving, and deleting images. It supports basic CRUD operations on images stored in MongoDB.

## Features

- **Upload Image**: Upload images with metadata.
- **Retrieve Images**: List all images with base64 encoded data.
- **Retrieve Image by ID**: Fetch a single image by its ID.
- **Delete Image**: Remove an image by its ID.
- **Static Files**: Serve HTML pages for uploading and viewing images.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- PyMongo
- Python-dotenv (for loading environment variables)
- MongoDB

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/javid-guluzada/upload-images.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```
4.  Activate the virtual environment:
    For Linux and macOS:
    ```bash
    source venv/bin/activate  
    ```
    For Windows:
    ```bash
    venv\Scripts\activate
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and add your MongoDB connection string:

    ```
    MONGO_DETAILS=mongodb://username:password@host:port/dbname
    ```

## Configuration

- **`config.json`**: Modify this file to set allowed file types 

    ```json
    {
        "allowed_file_types": ["png", "jpg", "jpeg"]
    }
    ```
    or leave it empty to allow all file types.
    ```json
    {
        "allowed_file_types": []
    }
    ```

## Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```
    or
    ```bash
    python run.py
    ```
2. Open your browser and navigate to `http://localhost:8000` to access the application.

## Endpoints

- **POST `/upload/`**: Upload an image with metadata.
  - Form data: `name` (string), `file` (file)
  
- **GET `/images/`**: Retrieve a list of all images with their id, name,type and base64 encoded data.
    Example
    ```json
    [{
        "id": "60f4b3b3b3b3b3b3b3b3b3b3",
        "name": "image1",
        "mime_type": "image/png",
        "data": "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABjElEQVR42mNkAAYy...=="
    }]
    ```
- **GET `/images/{id}`**: Retrieve a specific image by its ID.

- **DELETE `/delete/{id}`**: Delete a specific image by its ID.

- **GET `/`**: Serve the upload form HTML page.

- **GET `/gallery/`**: Serve the gallery HTML page.

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

## Acknowledgements

- FastAPI documentation and community
- PyMongo for MongoDB interactions

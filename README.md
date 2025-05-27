# Moondream FastAPI Application

## Setup

1. Install dependencies using Composer:
   ```
   composer install
   ```
   (Or, if using pip, install from composer.yaml dependencies manually.)

2. Make sure you have your GCP service account file as `service-account-file.json` in the root directory.

3. Set your bucket name in `app/services/gcs_service.py` if you want to change it.

4. Run the FastAPI app:
   ```
   uvicorn app.main:app --reload
   ```

## Endpoints

### 1. Upload Image
- **POST** `/upload`
- Form Data: `file` (image)
- Saves image to GCS and returns public URL.

### 2. Get Images
- **GET** `/get_images`
- Returns list of public URLs of images in GCS.

### 3. Generate Caption
- **POST** `/caption`
- Body:
  ```json
  { "image_url": "<url>", "length": "normal" }
  ```
- Returns caption for the image.

### 4. Answer Query
- **POST** `/query`
- Body:
  ```json
  { "image_url": "<url>", "query": "What is in the image?" }
  ```
- Returns answer to the query about the image.

### 5. Detect Object
- **POST** `/detect`
- Body:
  ```json
  { "image_url": "<url>", "object_to_detect": "letters" }
  ```
- Returns detected boxes and annotated image URL.

### 6. Point Object
- **POST** `/point`
- Body:
  ```json
  { "image_url": "<url>", "object_to_point": "letters" }
  ```
- Returns detected points and annotated image URL.

## Notes
- All detected/annotated images are also saved to GCS and will appear in `/get_images`.
- The logic for image processing is based on your original `test.py` code. 
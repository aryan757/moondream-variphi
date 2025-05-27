# Moondream FastAPI Application

## Setup

### Local Development

1. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Make sure you have your GCP service account file as `service-account-file.json` in the root directory.

4. Set your bucket name in `app/services/gcs_service.py` if you want to change it.

5. Run the FastAPI app:
   ```sh
   uvicorn app.main:app --reload
   ```

### Docker

1. Build the Docker image:
   ```sh
   docker build -t moondream-app .
   ```

2. Run the Docker container:
   ```sh
   docker run -p 8000:8000 moondream-app
   ```

3. Visit [http://localhost:8000](http://localhost:8000) to check if the API is running.

### Git Workflow

1. Initialize git and add your remote (if not already done):
   ```sh
   git init
   git remote add origin https://github.com/aryan757/moondream-variphi.git
   ```

2. Add all files (except those ignored by .gitignore):
   ```sh
   git add .
   ```

3. Commit your changes:
   ```sh
   git commit -m "project files and Docker setup"
   ```

4. Push to the main branch:
   ```sh
   git push -u origin main
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
# pdf_utils_api

## Overview

This project, `pdf_utils_api`, is a Django-powered API designed to streamline PDF manipulation. It currently offers two core services:

1. **Split:** Splits a PDF file into individual PDFs, one per page.
2. **Merge:** Combines multiple PDF files into a single consolidated PDF, maintaining the order of attachment.

## Environment Variables

* `IP_CLIENT_CORS=localhost`
* `PORT_CLIENT_CORS=3001`

These environment variables configure Cross-Origin Resource Sharing (CORS) to permit requests from your frontend application (presumably running on `localhost:3001`).

## Endpoints

### Split

* **URL:** `/split/`
* **Method:** `POST`
* **Request:** 
    * `pdf_file` (in form-data) - The PDF file to be split.
* **Response:** A `.zip` file containing the split PDFs.

### Merge

* **URL:** `/merge/`
* **Method:** `POST`
* **Request:** 
    * `pdf_files` (multiple files in form-data) - The PDF files to be merged.
* **Response:** A single merged PDF file.

## Running the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/peluza/pdf_utils_api.git
   cd pdf_utils_api
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set environment variables:**
    ```bash
    export IP_CLIENT_CORS=localhost
    export PORT_CLIENT_CORS=3001
    ```
    Our .env file
    ```env
    IP_CLIENT_CORS=localhost
    PORT_CLIENT_CORS=3001
    ```
4. **Start the development server:** 
    ```bash
    python manage.py runserver
    ```

Your API should now be accessible at http://127.0.0.1:8000/.

**Notes**
- Ensure you have the necessary PDF manipulation libraries installed (e.g., PyPDF2).
- Adjust the CORS settings if your frontend is hosted on a different domain or port.
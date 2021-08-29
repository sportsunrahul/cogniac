# Image Tranformation

This project performs various image tranformations that are commonly used as a data preprocessing step in computer vision tasks. 
 - Image rotation
 - Gray 
 - Resize
 - Crop
 - Equalize
---
Instructions to run:
1. Build docker:
    ```
    docker build -t <name>:<tag> .
    ```
2. Run docker in detached mode:
    ```
    docker run -d -p 3000:3000 <name>
    ```

    This will run the docker container on port 3000. 
---
#### RESTful APIs:
- Image Roatation:
    ```
    GET: /tranform/rotate

    Request:
    files: 
        image: required
    params:
        angle: required
    ```
     
- Gray Image:
    ```
    GET: /tranform/gray
    
    Request:
    files: 
        image: required
    ```
- Image Resize:
    ```
    GET: /tranform/resize

    Request:
    files: 
        image: required
    params:
        size: required
    ```   
- Image Crop:
    ```
    GET: /tranform/crop

    Request:
    files: 
        image: required
    params:
        left : required
        up   : required
        right: required
        low  : required
    ```
- Image Equalization:
    ```
    GET: /tranform/equalize

    Request:
    files: 
        image: required
    ```

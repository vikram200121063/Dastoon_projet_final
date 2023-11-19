# Comic Strip Generator

Generate a comic strip with 10 panels by providing text for each panel using this Streamlit app. The comic strip is created using an external API.

## Getting Started

1. Install dependencies:
    ```bash
    pip install streamlit requests Pillow
    ```

2. Run the app:
    ```bash
    streamlit run index.py
    ```

3. Input text for each panel.

4. Click "Generate Comic Strip" to create the comic strip.

## API Configuration

Configure API URL and authentication token in your script:

```python
API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "image/png",
    "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
    "Content-Type": "application/json",
}
```


## Author

[Vikram Singh]


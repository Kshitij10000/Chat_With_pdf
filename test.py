import streamlit as st
import requests
from io import BytesIO
from PyPDF2 import PdfReader

st.title('SharePoint Document Text Extractor')

# Input for the SharePoint URL
url = st.text_input('Enter the SharePoint URL of the document:')
if st.button('Extract Text'):
    if url:
        try:
            # Here you would need the cookie/session data which isn't directly possible without API/OAuth.
            # This is a placeholder to demonstrate the logic:
            headers = {'Cookie': 'session=your_session_cookie_here'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                with BytesIO(response.content) as open_pdf:
                    reader = PdfReader(open_pdf)
                    text = ''
                    for page in reader.pages:
                        text += page.extract_text() or ''
                    st.text_area("Extracted Text", value=text, height=300, max_chars=None)
            else:
                st.error(f"Failed to fetch document, status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error('Please enter a URL')

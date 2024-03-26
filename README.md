# python-library : `getAbstrctFromWeb`

# What is this package used for?
- Fetching the Abstract contents of a thesis

- Install requirements modules 
  ```python 
  pip install -r requirements.txt
  ```    

- How to use?
    ```python
    import getAbstractFromWeb as abstract
    
    fetching_html_text = abstract.myrequests("<url>")

    text = abstract.html2text(fetching_html_text)

    abstract_content = abstract.abstract_content(text)

    print(abstract_content)
    ```


from bs4 import BeautifulSoup



from textwrap import dedent
def html_to_markdown(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the body content, if the body tag exists
    body_content = (soup.body if soup.body else soup)

    # Convert headings
    for h_tag in body_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = int(h_tag.name[1])
        h_tag.replace_with('#' * level + ' ' + h_tag.text + '\n')

    # Dedent the paragraphs
    for p_tag in body_content.find_all('p'):
        p_tag.string = dedent(p_tag.text)

    # Remove <p> tags but keep their content
    for p_tag in body_content.find_all('p'):
        p_tag.unwrap()

    # Remove scripts
    for script_tag in body_content.find_all('script'):
        script_tag.decompose()

    # Convert links to Markdown format
    for a_tag in body_content.find_all('a'):
        href = a_tag.get('href', '')
        text = a_tag.text
        markdown_link = f"[{text}]({href})"
        a_tag.replace_with(markdown_link)

    # Remove <br> tags
    for br_tag in body_content.find_all('br'):
        br_tag.replace_with('\n')

    # Remove <br> tags
    for br_tag in body_content.find_all('br'):
        br_tag.replace_with('\n')

    # Convert <pre> tags to Markdown code blocks
    for pre_tag in body_content.find_all('pre'):
        code_content = pre_tag.text
        pre_tag.replace_with('```\n' + code_content + '\n```')

    # Since <div> and <img> tags are to be kept as is, we don't process them here.

    #Get rid of divs that have no content
    for div in body_content.find_all('div'):
        if not div.text.strip():
            div.decompose()

    # Get rid of id='wrap' divs
    for div in body_content.find_all('div', id='wrap'):
        div.unwrap()
    for div in body_content.find_all('div', id='main'):
        div.unwrap()

    # Ged rid of divs that have only another div as content
    for div in body_content.find_all('div'):
        if len(div.find_all('div')) == 1 and not div.text.strip():
            div.unwrap()

    # change all of the images that are relative the url doesn't start
    # with http, to be relative to the current directory
    for img in body_content.find_all('img'):
        src = img.get('src')
        if not src.startswith('http'):
            img['src'] = './'+src.split('/')[-1]

    # Extract the body content as html
    md = str(body_content.prettify())

    # Strip off the opening <body> and closing </body>
    md = md.replace("<body>","").replace("</body>","")



    return md


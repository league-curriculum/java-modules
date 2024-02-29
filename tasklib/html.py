from bs4 import BeautifulSoup



from textwrap import dedent
def html_to_markdown(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the body content, if the body tag exists
    body_content = soup.body if soup.body else soup

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

    # Return the converted HTML to Markdown (as a string)
    return str(body_content)


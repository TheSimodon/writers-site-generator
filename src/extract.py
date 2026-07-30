
def extract_title(markdown: str):
    temp = markdown
    if temp.startswith('#'):
        mod_temp = temp.strip('#').strip(' ')
        return mod_temp
    raise Exception('The start of the markdown is not correct')

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, file):
    with open(path, 'w', encoding='utf-8') as f:
        return f.write(file)
from textwrap import dedent

def generate_git_script(id):
    script = f'''
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi
    '''

    text = dedent(script)
    return text.strip()

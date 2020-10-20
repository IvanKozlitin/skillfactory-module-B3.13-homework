class HTML:
    """Класс HTML файла"""
    def __init__(self, output):
        self.tag = "HTML"
        self.html_code = ""
        self.output = output

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        with open(self.output, 'w', encoding="utf-8") as result_file:
            self.html_code = "<{tag}>\n{html_code}\n</{tag}>".format(tag=self.tag, html_code=self.html_code)
            result_file.write(self.html_code)

    def __iadd__(self, other):
        self.html_code += str(other)

class TopLevelTag:
    """Класс TopLevelTag"""
    def __init__(self, tag):
        self.tag = tag
        self.html_code = ""
        self.attributes = {}
        self.toplevel = True

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __iadd__(self, other):
        self.html_code += str(other)

    def __str__(self):
        return "<{tag}>\n{html_code}\n</{tag}>".format(tag=self.tag, html_code=self.html_code)

class Tag:
    pass

# Исходник

with HTML(output="test.html") as doc:
    pass
    with TopLevelTag("head") as head:
    #     with Tag("title") as title:
    #         title.text = "hello"
    #         head += title
        doc += head

    # with TopLevelTag("body") as body:
    #     with Tag("h1", klass=("main-text",)) as h1:
    #         h1.text = "Test"
    #         body += h1

    #     with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
    #         with Tag("p") as paragraph:
    #             paragraph.text = "another test"
    #             div += paragraph

    #         with Tag("img", is_single=True, src="/icon.png" data_image="responsive") as img:
    #             div += img

    #         body += div

    #     doc += body
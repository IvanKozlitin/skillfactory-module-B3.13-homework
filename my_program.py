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
        return self
        

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
        return self

    def __str__(self):
        return "<{tag}>\n{html_code}\n</{tag}>\n".format(tag=self.tag, html_code=self.html_code)

class Tag:
    """Класс Tag"""
    def __init__(self, tag, is_single=False, klass=[], **attr):
        self.tag = tag
        self.html_code = ""
        self.text = ""
        self.attributes = attr
        self.klass = klass
        self.is_single = is_single

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __iadd__(self, other):
        self.html_code += str(other)
        return self

    def __str__(self):

        if self.klass != []:
            my_class = "class=\"{}\"".format(" ".join(self.klass))
        else:
            my_class = ""

        attrs = [my_class]
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.is_single == True:
            result_html = "<{tag} {attrs}/>\n".format(tag=self.tag, attrs=attrs, text=self.text, html_code=self.html_code)
        else:
            result_html = "<{tag} {attrs}>\n{text}\n{html_code}\n</{tag}>\n".format(tag=self.tag, attrs=attrs, text=self.text, html_code=self.html_code)
        return result_html


# Генерация HTML файла

if __name__ == "__main__":
    with HTML(output="test.html") as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                    div += img

                body += div

            doc += body
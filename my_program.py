# Разработанный код

class HTML():
    def __init__(self, output):
        self.output = output

    def __enter__(self):
        return self

class TopLevelTag():
    def __init__(self, top_level_tag_name):
        self.top_level_tag_name = top_level_tag_name
        self.attributes = {}

    def __enter__(self):
        return self

class Tag():
    def __init__(self, tag_name, is_single = False):
        self.tag_name = tag_name
        self.text = ""
        self.attributes = {}
        self.is_single = is_single

    def __enter__(self):
        return self

# Доработать классы и разобраться с тем как это всё работает!!!


# Исходник

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

            with Tag("img", is_single=True, src="/icon.png" data_image="responsive") as img:
                div += img

            body += div

        doc += body
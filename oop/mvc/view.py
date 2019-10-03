class OrderView:
    def render(self, data):
        return """
        <html>
        <body>
        {}
        </body>
        </html>""".format(data)
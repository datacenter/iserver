class LinuxHugePagesInfo():
    def __init__(self):
        self.huge_pages = None

    def get_huge_pages_info(self):
        if self.huge_pages is not None:
            return self.huge_pages
        self.huge_pages = self.get_huge_pages_cmd()
        return self.huge_pages

    def get_huge_pages(self):
        return self.get_huge_pages_info()

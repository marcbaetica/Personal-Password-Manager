class Credentials:
    def __init__(self, site, user, password):
        self.site = site
        self.user = user
        self.password = password

    def __repr__(self):
        return f'Credential({self.site}, {self.user}, {self.password})'

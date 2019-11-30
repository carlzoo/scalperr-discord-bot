from discord import Embed


class BotResponse(Embed):
    def __init__(self, title, event_id, colour):
        super().__init__(title=title, colour=colour)
        self.event_id = event_id
        self.title = title
        self.event_name = ''
        self.city = ''
        self.venue = ''
        self.url = ''
        self.datetime = ''
        self.em_colour = colour
        self.footer_msg = "Stock Checker made by ieatgoosefeces#2163"
        self.sections = []  # tuple of (section, count)
        self.total = 0

    def set_datetime(self, datetime):
        self.datetime = datetime

    def set_url(self, url):
        self.url = url

    def set_venue(self, venue):
        self.venue = venue

    def set_name(self, event_name):
        self.event_name = event_name

    def set_city(self, city):
        self.city = city

    def add_section(self, section_name, count):
        self.sections.append((section_name, count))
        self.total += count

    def build_display(self, is_help=False):
        if is_help:
            self.add_field(name=f'Commands',
                           value=f'!stock tm [event_id]\n!stock tmintl [event_id]\n!stock axs [event_id]',
                           inline=False)
            self.set_footer(text="Stock checker made by ieatgoosefeces#2163")
            return

        self.add_field(name=f'Event Info',
                       value=f'[{self.event_name}]({self.url})\n{self.venue} | {self.city}\n{self.datetime}',
                       inline=False)
        if self.total == 0:
            self.add_field(name=f'Error', value=f'No seats available', inline=False)
        else:
            values_list = ''
            for section in self.sections:
                values_list += f'\n**{section[0]}** ({section[1]})'
            self.add_field(name=f'Inventory', value=values_list, inline=True)
            self.add_field(name=f'Total Count', value=f'{self.total}', inline=True)
        self.set_footer(text="Stock checker made by ieatgoosefeces#2163")

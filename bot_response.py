from discord import Embed


class BotResponse(Embed):
    def __init__(self, title, colour):
        super().__init__(title=title, colour=colour)
        self.title_msg = title
        self.em_colour = colour
        self.footer_msg = "Stock Checker made by ieatgoosefeces#2163"

    def add_section(self, section_name, min_price, max_price, count):
        display_min_price = f'${min_price}'
        display_max_price = f'${max_price}'
        display_price = f'{display_min_price} - {display_max_price}'
        self.add_field(name=f'Section {section_name}', value=f'{display_price} Count: {count}', inline=False)

    def set_empty(self):
        self.add_field(name=f'Error', value=f'No seats available', inline=False)

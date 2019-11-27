from discord import Embed


class BotResponse(Embed):
    def __init__(self, title, event_id, colour):
        super().__init__(title=title, colour=colour)
        self.event_id = event_id
        self.title_msg = title
        self.em_colour = colour
        self.footer_msg = "Stock Checker made by ieatgoosefeces#2163"
        self.sections = []  # tuple of (section, count)
        self.total = 0

    def add_section(self, section_name, count):
        self.sections.append((section_name, count))
        self.total += count

    def build_display(self):
        self.add_field(name=f'Event Link',
                       value=f'[{self.event_id}](https://www1.ticketmaster.com/events/{self.event_id})',
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

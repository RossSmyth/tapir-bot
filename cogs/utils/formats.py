# formats messages

async def entry_to_code(bot, entries):
    """formats input into discord code format"""
    width = max(map(lambda t: len(t[0]), entries))
    output = ['```']
    fmt = '{0:<{width}}: {1}'
    for name, entry in entries:
        output.append(fmt.format(name, entry, width=width))
    output.append('```')
    await bot.say('\n'.join(output))
    
async def indented_entry_to_code(bot, entries):
    """formats input into discord code format with indents"""
    width = max(map(lambda t: len(t[0]), entries))
    output = ['```']
    fmt = '\u200b{0:>{width}}: {1}'
    for name, entry in entries:
        output.append(fmt.format(name, entry, width=width))
    output.append('```')
    await bot.say('\n'.join(output))

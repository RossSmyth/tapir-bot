from discord.ext import commands

"""
if you don't meet a permission to do a command, nothing really happens.
If you are the bot owner, you can run any command, anywhere, anytime.
"'it just works'
-todd howard"
-micheal scott
"""


async def check_permissions(ctx, perms, *, check=all):
    """does some permission checking"""
    is_owner = await ctx.bot.is_owner(ctx.author)
    if is_owner:
        return True

    resolved = ctx.permissions_for(ctx.author)
    return check(getattr(resolved, name, None) == value for name, value
                 in perms.items())


def has_permissions(*, check=all, **perms):
    """Command decorator for checking permissions"""
    async def pred(ctx):
        return await check_permissions(ctx, perms, check=check)
    return commands.check(pred)

async def check_guild_permissions(ctx, perms, *, check=all):
    """Checks for permissions in a specific guild"""
    is_owner = await ctx.bot.is_owner(ctx.author)
    if is_owner:
        return True

    if ctx.guild is None:
        return False

    resolved = ctx.author.guild_permissions
    return check(getattr(resolved, name, None) == value for name, value
                 in perms.items())


def has_guild_permissions(*, check=all, **perms):
    """Command decorator for checking guild permissions"""
    async def pred(ctx):
        return await check_guild_permissions(ctx, perms, check=check)
    return commands.check(pred)


# The following decorators do not account for channel overwrites
def is_mod():
    """Command decorator for checking for moderator permissions"""
    async def pred(ctx):
        return await check_guild_permissions(ctx, {'manage_guild': True})
    return commands.check(pred)


def is_admin():
    """Command decorator for checking for admin permissions"""
    async def pred(ctx):
        return await check_guild_permissions(ctx, {'administrator': True})
    return commands.check(pred)


def mod_or_permissions(**perms):
    """Command decorator for checking for moderator or other permissions"""
    perms['manage_guild'] = True
    async def predicate(ctx):
        return await check_guild_permissions(ctx, perms, check=any)
    return commands.check(predicate)


def admin_or_permissions(**perms):
    """Command decorator for checking for admin or other permissions"""
    perms['administrator'] = True
    async def predicate(ctx):
        return await check_guild_permissions(ctx, perms, check=any)
    return commands.check(predicate)


def is_in_guilds(*guild_ids):
    """Command decorator for if the command is in a specific guild"""
    def predicate(ctx):
        guild = ctx.guild
        if guild is None:
            return False
        return guild.id in guild_ids
    return commands.check(predicate)


from discord.ext import commands
import discord.utils

def is_owner_check(message):
    """"is it me?"""
    return message.author.id == '149281074437029890'

def is_owner():
    """is me but diffent"""
    return commands.check(lambda ctx: is_owner_check(ctx.message))

"""
There is now a permissions system!
if you don't meet a permission to do a command, nothing really happens
but if you are the owner or a so called bot mod you can do stuff
if you are the owner (treefroog) you can do any command
'it just works'
-todd howard
-micheal scott
"""

def check_permissions(ctx, perms):
    """does some permission checking. I can do anything"""
    msg = ctx.message
    if is_owner_check(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())
    
def role_or_permissions(ctx, check, **perms):
    """checks roles or permissions, since rolees can do some stuff"""
    if check_permissions(ctx, perms):
        return True

    ch = ctx.message.channel
    author = ctx.message.author
    if ch.is_private:
        return False # can't have roles in PMs

    role = discord.utils.find(check, author.roles)
    return role is not None
    
def mod_or_permissions(**perms):
    """checks if mod, or permissions to do stuff"""
    def predicate(ctx):
        return role_or_permissions(ctx, lambda r: r.name in ('Bot Mod', 'Bot Admin'), **perms)

    return commands.check(predicate)
    
def admin_or_permissions(**perms):
    """checks if admin, or if permission allows to do stuff"""
    def predicate(ctx):
        return role_or_permissions(ctx, lambda r: r.name == 'Bot Admin', **perms)

    return commands.check(predicate)
    
def is_in_servers(*server_ids):
    """if is in server"""
    def predicate(ctx):
        server = ctx.message.server
        if server is None:
            return False
        return server.id in server_ids
    return commands.check(predicate)
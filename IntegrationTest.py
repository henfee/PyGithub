#!/bin/env python

from github import Github
import GithubCredentials

g = Github( GithubCredentials.login, GithubCredentials.password )

def dumpUser( u ):
    print u.login, "(", u.name, ")"
    print "  Repos:"
    for r in u.get_repos():
        print "   ", r.name,
        if r.fork:
            print "<-", r.parent.owner.login + "/" + r.parent.name,
            print "<-", r.source.owner.login + "/" + r.source.name,
        print
    print "  Watched:", ", ".join( r.name for r in u.get_watched() )
    print "  Organizations:", ", ".join( o.login for o in u.get_orgs() )
    print "  Following:", ", ".join( f.login for f in u.get_following() )
    print "  Followers:", ", ".join( f.login for f in u.get_followers() )
    print

def dumpOrganization( o ):
    print o.login, "(", o.name, ")"
    print "  Members:", ", ".join( u.login for u in o.get_members() )
    print "  Repos:", ", ".join( r.name for r in o.get_repos() )
    print

def dumpRepository( r ):
    print r.owner.login + "/" + r.name
    print "  Collaborators:", ", ".join( u.login for u in r.get_collaborators() )
    print "  Contributors:", ", ".join( u.login for u in r.get_contributors() )
    print "  Watchers:", ", ".join( u.login for u in r.get_watchers() )
    print "  Forks:", ", ".join( f.owner.login + "/" + f.name for f in r.get_forks() )
    print

dumpUser( g.get_user() )
dumpUser( g.get_user( "nvie" ) )
dumpOrganization( g.get_organization( "github" ) )
dumpOrganization( g.get_organization( "BeaverSoftware" ) )
dumpRepository( g.get_user().get_repo( "C4Planner" ) )
dumpRepository( g.get_user( "nvie" ).get_repo( "gitflow" ) )
dumpRepository( g.get_organization( "BeaverSoftware" ).get_repo( "FatherBeaver" ) )

u = g.get_user()
# print "Bio before:", u.bio
# u.edit( bio = u.bio + "(Edited by PyGithub)" )
# print "Bio after:", u.bio

# u.remove_from_following( g.get_user( "Lyloa" ) )
# u.add_to_following( g.get_user( "Lyloa" ) )

# for r in g.get_user( "cjuniet" ).get_repos():
    # u.add_to_watched( r )
    # u.remove_from_watched( r )

o = g.get_organization( "BeaverSoftware" )
# o.edit( location = "Paris, France" )

# u.create_repos( name = "TestGithubApi" + str( len( u.get_repos() ) ), description = "Created by a Python script!" )

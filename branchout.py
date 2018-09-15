#!/usr/bin/env python

import subprocess
import os
gitBaseUrl="git@github.com"
projectFile='.projects'

def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout

with open(projectFile, 'r') as pf:
    projects = pf.read().splitlines()
    for line in projects:
        projectGroup, projectGitUrl = line.split(':')

        if not os.path.exists(projectGroup):
            subprocess.Popen(['mkdir', '-p', projectGroup], stdout=subprocess.PIPE)

        projectOrg, projectName = projectGitUrl.split('/')
        if not os.path.exists('%s/%s' % (projectGroup, projectName)):
            print('Cloning project from [%s:%s]' % (gitBaseUrl, projectGitUrl))
            subprocess_cmd('cd %s && git clone %s:%s' % (projectGroup, gitBaseUrl, projectGitUrl))
        else:
            print('Fetching project from [%s:%s]' % (gitBaseUrl, projectGitUrl))
            subprocess_cmd('cd %s/%s && git fetch origin' % (projectGroup, projectName))
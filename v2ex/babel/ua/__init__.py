# coding=utf-8

import re
import os
import logging

import user_agents

def detect(request):
    user_agent_string = request.headers['User-Agent']
    result = {}
    result['ua'] = user_agent_string

    user_agent = user_agents.parse(user_agent_string)
    result['ios'] = user_agent.os.family == 'iOS'
    return result

# -*- coding: utf-8 -*-
def nice_time(td):
    seconds = td.seconds
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30
    years = months / 12
    string = ''
    if minutes >= 1:
        if minutes > 1:
            string = str(int(minutes)) + ' minutes ago'
    if hours >= 1:
        if hours == 1:
            string = str(int(hours)) + ' hour ago'
        else:
            string = str(int(hours)) + ' hours ago'
    if days >= 1:
        if days == 1:
            string = str(int(days)) + ' day ago'
        else:
            string = str(int(days)) + ' days ago'
    if months >= 1:
        if months == 1:
            string = str(int(months)) + ' month ago'
        else:
            string = str(int(months)) + ' months ago'
    if years >= 1:
        if years == 1:
            string = str(int(years)) + ' year ago'
        else:
            string = str(int(years)) + ' years ago'
    return string


def nice_time_ar(td):
    seconds = td.seconds
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30
    years = months / 12
    string = ''
    if int(minutes) >= 1:
        string = str(int(minutes)) + ' دقيقة '
    if int(hours) >= 1:
        string = str(int(hours)) + ' ساعة '
    if int(days) >= 1:
        string = str(int(days)) + ' يوم '
    if int(months) >= 1:
        string = str(int(months)) + ' شهر'
    if int(years) >= 1:
        string = str(int(years)) + ' سنة '
    return string

import time
import urllib
import requests
from splinter import Browser
from selenium import webdriver

username = "taylordavidsonmiddlebrooks@yahoo.com"
password = "1p2p3p1p2p3p4p3p4p2p3p1p4p2p3p2["

executable_path = {"executable_path":r"C:/Users/msuch/Desktop/chromedriver.exe"}

# Set some default behaviors for our browser
options = webdriver.ChromeOptions()

# make sure the window is maximized
options.add_argument("--start-maximized")

# Make sure notifications are off
options.add_argument("--disable-notifications")

browser = Browser("chrome", **executable_path, headless=False, options = options)

browser.visit("https://www.facebook.com")

# find email element
username_box = browser.find_by_id("email")

# fill out email element
username_box.fill(username)

# find password element
password_box = browser.find_by_id("pass").fill(password)

# click the login button
submit = browser.find_by_id("u_0_2").first.click()
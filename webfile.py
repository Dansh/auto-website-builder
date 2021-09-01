import os
import subprocess
import pygame
import tkinter as tk
from tkinter import filedialog


class Webfile():
    def __init__(self, kind):
        self.kind = kind        
        self.draw()

    def draw(self):
        
        
        inputs = self.get_file_inputs()
        webfile_string = """
        <%@ Page Title="" Language="C#" MasterPageFile="~/master.Master" AutoEventWireup="true" CodeBehind="about.aspx.cs" Inherits="nadel_web.home" %>
        <asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
            <link rel="stylesheet" href="master.css"/>
        </asp:Content>
        <asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
            <link rel="stylesheet" href="about.css"/>
            <h1 dir="rtl" id="nice-to-meet-title">{}</h1>            
            <div id="nice_to_meet_text_div">
            <p id="nice_to_meet_des" dir="rtl">
                {}
            </p>
        <a href="contact.aspx" dir="rtl" style="text-decoration: none;" id="link3-btn">{}</a>

            </div>
        </asp:Content>
        """.format(inputs["main-title"], self.format_titles_paragraphs(inputs["description"]), inputs["contact-text"])
        self.save_file(webfile_string, "try.aspx")
        
    def get_file_inputs(self):
        file_inputs = {}       
        if self.kind == "normal":
            file_inputs["main-title"] = input("תישאר תרתוכ: ")
            #file_inputs["main-image"] = self.get_file_path(filetype="Images")
            file_inputs["description"] = []
            text_input = input("כותרת משנה: ")
            while text_input != "-1":
                file_inputs["description"].append(text_input)
                text_input = input("טקסט:  ")
                file_inputs["description"].append(text_input)
                text_input = input("כותרת משנה:  ")
            file_inputs["contact-text"] = input("טקסט לצור קשר: ")
        return file_inputs


    def get_file_path(self, file_type):
        root = tk.Tk()
        root.withdraw()     
        path = filedialog.askopenfilename(        
        )           
        filepath = file_type + filedialog.askopenfilename().split(file_type)[1]
        return filepath

    def format_titles_paragraphs(self, titles_paragraphs):
        subtitle_format = "<b style='font-size: 28px;'>{}<br /><br /></b>"
        paragraphs = titles_paragraphs[1::2]
        subtitles = titles_paragraphs[::2]
        string = ""
        for i, subtitle in enumerate(subtitles):
            string += subtitle_format.format(subtitle)
            string += paragraphs[i]
            string += "<br /><br />"
        return string
    
    def save_file(self, text, filename): # filename.txt
        with open(filename, 'w', encoding='utf-16') as f:
            f.write(text)
        


web = Webfile("normal")


#nadelprojects.com


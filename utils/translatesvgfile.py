#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:25:42 2024

@author: benny
"""
import shutil
import os
# prompt: Open a translation po file and convert it into a dictionary

def read_po_file(po_file_path):
  """
  Reads a PO file and converts it into a dictionary of translations.

  Args:
    po_file_path: The path to the PO file.

  Returns:
    A dictionary where keys are original strings and values are translations.
  """
  translations = {}
  msgid = None
  msgstr = None
  with open(po_file_path, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.strip()
      if line.startswith('msgid "'):
        msgid = line[7:-1]
      elif line.startswith('msgstr "'):
        msgstr = line[8:-1]
        if msgid and msgstr:
          translations[msgid] = msgstr
          msgid = None
          msgstr = None
  return translations

# prompt: python code to copy a file to new name

def copy_file(source_file_path, destination_file_path):
  """
  Copies a file to a new location with a new name.

  Args:
    source_file_path: The path to the original file.
    destination_file_path: The path to the new file location and name.
  """
  try:
    shutil.copy2(source_file_path, destination_file_path)
    #print(f"File copied successfully to: {destination_file_path}")
  except FileNotFoundError:
    print(f"Error: Source file not found: {source_file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

def delete_file(file_path):
  """
  Deletes a file from the specified path.

  Args:
    file_path: The path to the file to be deleted.
  """
  try:
    os.remove(file_path)
    #print(f"File '{file_path}' deleted successfully.")
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
  except Exception as e:
    print(f"An error occurred while deleting the file: {e}")

if __name__ == "__main__":
    svg_file_path = '../assets/img/planet/planet-v03.svg'
    po_file_path = 'translations_nl.po'
    translations_dict = read_po_file(po_file_path)
    filename_out = 'newfile.svg'
    filename_in = 'newfile_copy.svg'
    
    copy_file(svg_file_path, filename_out)

    # obtain all english text from longest text to shortest
    sorted_keys = sorted(translations_dict.keys(), key=len, reverse=True)
    for txten in sorted_keys:
        txtnl = translations_dict[txten]
        print (txten, '-->', txtnl)
        # make copy of old version first
        copy_file(filename_out, filename_in)
        # make new version of output file
        with open(filename_out, 'w') as file:
            file.write(open(filename_in).read().replace('>' + txten, '>' + txtnl))
    # fix error of DEL changed in OPL, but DELEN is Dutch
    copy_file(filename_out, filename_in)
    # make new version of output file
    with open(filename_out, 'w') as file:
        file.write(open(filename_in).read().replace('>OPLEN', '>DELEN'))
    
    #remove tmp file
    delete_file(filename_in)
    
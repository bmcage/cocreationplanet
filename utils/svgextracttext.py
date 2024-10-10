# prompt: Extract all tspan objects from an svg file

from xml.etree import ElementTree as ET

def extract_tspan_objects(svg_file_path):
  """
  Extracts all tspan objects from an SVG file.

  Args:
    svg_file_path: The path to the SVG file.

  Returns:
    A list of tspan elements.
  """
  tree = ET.parse(svg_file_path)
  root = tree.getroot()
  tspan_elements = root.findall('.//{http://www.w3.org/2000/svg}tspan')
  return tspan_elements 

# Example usage:
# svg_file_path = 'path/to/your/svg_file.svg'
# tspan_objects = extract_tspan_objects(svg_file_path)
# for tspan in tspan_objects:
#   print(tspan.text) 


# prompt: write out a dictionary as a po tranlation file with key the original language and value the translation

def write_po_file(translations, output_file_path):
  """
  Writes a dictionary of translations to a PO file.

  Args:
    translations: A dictionary where keys are original strings and values are
      translations.
    output_file_path: The path to the output PO file.
  """
  with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write('msgid ""\n')
    f.write('msgstr ""\n')
    f.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
    f.write('"Content-Transfer-Encoding: 8bit\\n"\n')
    for original, translated in translations.items():
      f.write('msgid "{}"\n'.format(original))
      f.write('msgstr "{}"\n'.format(translated))
 
if __name__ == "__main__":
    dict_to_translate = {}
    svg_file_path = '../assets/img/planet/planet-v03.svg'
    tspan_objects = extract_tspan_objects(svg_file_path)
    for tspan in tspan_objects:
        if not (tspan.text in [None, '']) and not (tspan.text.strip() == ''):
            try:
                int(tspan.text)
            except ValueError:
                if tspan.text not in dict_to_translate:
                    dict_to_translate[tspan.text.strip()] = ''
    list_words = list(dict_to_translate)
    for word in list_words:
        print(word)
    
    write_po_file(dict_to_translate, 'translations.po')

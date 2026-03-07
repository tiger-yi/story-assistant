import os
import re

def main():
    base_dir = r'd:\IdeaProjects\story-assistant'
    outline_path = os.path.join(base_dir, 'story', 'outline.md')
    chapters_dir = os.path.join(base_dir, 'chapters')
    export_dir = os.path.join(base_dir, 'export')
    
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    # 1. Read Metadata
    with open(outline_path, 'r', encoding='utf-8') as f:
        outline_content = f.read()
    
    title_match = re.search(r'\*\*故事名称：\*\*《(.*?)》', outline_content)
    title = title_match.group(1) if title_match else "未命名故事"
    
    # Extract intro more robustly
    intro = ""
    in_intro = False
    for line in outline_content.split('\n'):
        if '**故事简介：**' in line:
            in_intro = True
            continue
        if in_intro:
            if line.strip().startswith('**'): # Next section
                break
            if line.strip().startswith('>'):
                intro += line.replace('>', '').strip() + "\n"
            elif line.strip(): # plain text in intro
                intro += line.strip() + "\n"
    
    if not intro:
        intro = "暂无简介"

    # 2. Read Chapters
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.endswith('.md')])
    
    full_content = []
    full_content.append(f"书名：《{title}》\n")
    full_content.append(f"简介：\n{intro}\n")
    full_content.append("-" * 30 + "\n\n")
    
    for chapter_file in chapter_files:
        chapter_path = os.path.join(chapters_dir, chapter_file)
        with open(chapter_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            full_content.append(content)
            full_content.append("\n\n" + "-" * 30 + "\n\n")
            
    # 3. Write Export
    output_filename = f"《{title}》_全书完稿.txt"
    output_path = os.path.join(export_dir, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(full_content))
        
    print(f"Exported to: {output_path}")

if __name__ == "__main__":
    main()

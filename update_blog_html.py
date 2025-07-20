import os

# Where your blog HTML files are stored (main folder)
BLOG_FOLDER = '.'
BLOG_HTML = 'blog.html'

# List blog files (all .html except index and the blog page itself)
blog_files = [f for f in os.listdir(BLOG_FOLDER)
              if f.endswith('.html')
              and f != 'index.html'
              and f != BLOG_HTML]

# Optional: Sort with newest first
blog_files = sorted(blog_files, key=lambda x: os.path.getmtime(os.path.join(BLOG_FOLDER, x)), reverse=True)

def extract_title(filename):
    # Try to extract <title> from each HTML file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if "<title>" in line:
                    return line.strip().replace('<title>', '').replace('</title>', '')
    except:
        pass
    # Fallback: filename
    return filename.replace('.html', '').replace('-', ' ').title()

# Build the list of links
blog_links = ""
for f in blog_files:
    title = extract_title(f)
    blog_links += f'    <li><a href="{f}">{title}</a></li>\n'

# Write the updated blog.html file
with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n")
    f.write("  <meta charset=\"UTF-8\" />\n")
    f.write("  <title>HD Heed Blogs</title>\n")
    f.write("</head>\n<body>\n")
    f.write("  <h1>HD Heed Blog</h1>\n")
    f.write("  <ul>\n")
    f.write(blog_links)
    f.write("  </ul>\n")
    f.write("  <p><a href=\"index.html\">Back to Home</a></p>\n")
    f.write("</body>\n</html>\n")
